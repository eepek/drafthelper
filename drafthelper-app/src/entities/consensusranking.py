import os
import pandas as pd
from repositories.ranking_loader import ConsensusrankingRepository


class ConsensusRanking:
    """Class that contains the ranking of players loaded from CSV file as a Pandas Dataframe.
    Keeps the list updated during the draft event, by removing chosen players and returning
    only players that could be selected to users roster.

    Attributes:
        data: Initial ranking of players as a dataframe
        player_names: list of players names
        file_name: File name for chosen scoring format, default is PPR
    """
    def __init__(self):
        """Constructs a new consensusranking class"""
        self.__data = pd.DataFrame()
        self.__player_names = []
        self.__filename = 'PPR.csv'

    def generate_consensusranking(self):
        """Reads the given CSV file via ConsensusrankingRepository and saves it
        as a pandas dataframe. This format is used for future features, to easily access extra
        information that can be given to the user
        """
        new_ranking_data = ConsensusrankingRepository(self.__filename)
        self.__data = new_ranking_data.get_dataframe()
        self.__player_names = self.__data['PLAYER NAME'].tolist()
        for i, player in enumerate(self.__player_names):
            self.__player_names[i] = player.lower()
        self.__data['LOWERCASE NAME'] = self.__player_names

    def set_filename(self, scoring_format: str):
        """Sets the filename for the file used for consensusranking according
        to user chosen scoring format. Defaul value is PPR.csv

        Args:
            scoring_format (str): User chosen scoring format as str
        """
        self.__filename = scoring_format + '.csv'

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
        for i,player in enumerate(self.__player_names):
            if player.startswith(name):
                return i
        return -1

    def take_a_player_by_name(self, name):
        """Removes selected player from the dataframe and returns the players position

        Args:
            name: Name of the player to be removed from dataframe

        Returns:
            If player is in dataframe returns the position of the player,
            otherwise refers players name to be checked if it exists"""
        index_number = self.is_a_real_player(name)
        if index_number >= 0:
            try:
                position = self.__data.iloc[index_number]['POS']
                name_correctly_spelt = self.__data.iloc[index_number]['PLAYER NAME']
            except IndexError:
                return False
            self.__data = self.__data.loc[self.__data['LOWERCASE NAME']
                                          != self.__player_names[index_number]]
            self.reset_indexes()
            self.__player_names.pop(index_number)
            return (name_correctly_spelt, position)

        return False

    def reset_indexes(self):
        """After removing a player from the dataframe, resets the indexes
        so there are no gaps between indexes"""
        self.__data = self.__data.reset_index(drop=True)
