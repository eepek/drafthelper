import os
import pandas as pd


class ConsensusRanking:
    """Class that contains the ranking of players loaded from CSV file as a Pandas Dataframe.
    Keeps the list updated during the draft event, by removing chosen players and returning
    only players that could be selected to users roster.

    Attributes:
        data: Initial ranking of players as a dataframe
        player_names: list of players names
        directory: current working directory, used to load the CSV file
        file: path for CSV file
    """
    def __init__(self):
        """Creates a new consensusranking"""
        self.__data = pd.DataFrame()
        self.__player_names = []
        self.__directory = os.path.dirname(__file__)
        self.__file = os.path.join(self.__directory, '..', 'csv/rankings.csv')

    def generate_consensusranking(self):
        """Reads the given CSV file and saves it as a pandas dataframe.
        This format is used for future features, to easily access extra
        information that can be given to the user
        """
        self.__data = pd.read_csv(self.__file)
        self.__data = self.__data.drop('TIERS', axis=1)

        self.__data['POS'] = self.__data['POS'].str[:2]
        self.__player_names = self.__data['PLAYER NAME'].tolist()

    def get_players(self, amount: int, full_positions: list):
        """Based on given attributes gets players from dataframe and returns
        the amount of players requested from the top of dataframe

        Args:
            amount: Number of players to be returned
            full_positions: List of positions that are filled in current teams roster

        Returns:
            Dataframe containing given amount of top players, with positions not yet
            filled in current teams roster"""
        if amount < 1:
            #Jos annettu negatiivinen arvo, otetaan oletusarvo 5
            amount = 5

        if len(full_positions) == 6:
            return False

        if len(full_positions) > 0:
            top_of_dataframe = self.__data[~self.__data['POS'].isin(full_positions)]
        else:
            top_of_dataframe = self.__data
        top_of_dataframe = top_of_dataframe.reset_index(drop=True)
        return top_of_dataframe[['PLAYER NAME', 'TEAM', 'POS', 'RK']].head(amount)

    def is_a_real_player(self, name):
        """Checks if given player actually exists in dataframe

        Args:
            name: Players name to be checked

        Returns:
            True if given player is elligble for a pick, otherwise False"""
        for player in self.__player_names:
            if player.lower() == name.lower():
                return True

        return False

    def take_a_player_by_name(self, name):
        """Removes selected player from the dataframe and returns the players position

        Args:
            name: Name of the player to be removed from dataframe

        Returns:
            If player is in dataframe returns the position of the player,
            otherwise refers players name to be checked if it exists"""
        try:
            position = self.__data[self.__data['PLAYER NAME']
                                == name]['POS'].values[0]
        except IndexError:
            return self.is_a_real_player(name)

        self.__data = self.__data.loc[self.__data['PLAYER NAME'] != name]
        self.__player_names.remove(name)

        return position

    def reset_indexes(self):
        """After removing a player from the dataframe, resets the indexes
        so there are no gaps between indexes"""
        self.__data = self.__data.reset_index(drop=True)
