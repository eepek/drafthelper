import pandas as pd
import os

class ConsensusRanking:

    def __init__(self, file='/src/csv/rankings.csv'):
        #TODO-listalla fiksata tää folderista lataus kuntoon. Toimii nyt kuitenkin invoken kautta, vaikka on aika purkka    
        self.__file = file
        self.__dir = os.getcwd()
        if self.__dir.endswith('src') and self.__file == '/src/csv/rankings.csv':
            self.__file = '/csv/rankings.csv'
        self.__file = self.__dir + self.__file
        
    def get_cr(self):
        self.__data = pd.read_csv(self.__file)
        self.__data = self.__data.drop('TIERS', axis=1)

        self.__data['POS'] = self.__data['POS'].str[:2]
        self.__player_names = self.__data['PLAYER NAME'].tolist() 

    def get_3(self):
        return self.__data[['PLAYER NAME', 'TEAM', 'POS', 'RK']].head(3)

    def is_a_real_player(self, name):
        return name in self.__player_names

    def take_a_player_by_name(self, name):
        pos = self.__data[self.__data['PLAYER NAME'] == name]['POS'].values[0]
        self.__data = self.__data.loc[self.__data['PLAYER NAME'] != name]
        self.__player_names.remove(name)
        return pos

    def take_a_player_by_id(self, id):
        name = self.__player_names.pop(id)
        pos = self.__data[self.__data['PLAYER NAME'] == name]['POS'].values[0]
        self.__data = self.__data.drop(id)
        return (name, pos)
    
    def reset_indexes(self):
        self.__data = self.__data.reset_index(drop = True)


