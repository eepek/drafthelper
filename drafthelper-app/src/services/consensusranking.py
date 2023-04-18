import os
import pandas as pd


class ConsensusRanking:

    def __init__(self):
        self.__data = pd.DataFrame()
        self.__player_names = []
        self.__directory = os.path.dirname(__file__)
        self.__file = os.path.join(self.__directory, '..', 'csv/rankings.csv')

    def generate_consensusranking(self):
        self.__data = pd.read_csv(self.__file)
        self.__data = self.__data.drop('TIERS', axis=1)

        self.__data['POS'] = self.__data['POS'].str[:2]
        self.__player_names = self.__data['PLAYER NAME'].tolist()

    def get_players(self, amount, full_positions: list):
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
        for player in self.__player_names:
            if player.lower() == name.lower():
                return True

        return False

    def take_a_player_by_name(self, name):
        try:
            position = self.__data[self.__data['PLAYER NAME']
                                == name]['POS'].values[0]
        except IndexError:
            return self.is_a_real_player(name)

        self.__data = self.__data.loc[self.__data['PLAYER NAME'] != name]
        self.__player_names.remove(name)

        return position

    def reset_indexes(self):
        self.__data = self.__data.reset_index(drop=True)
