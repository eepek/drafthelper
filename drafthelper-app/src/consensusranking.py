import pandas as pd

class ConsensusRanking:

    def __init__(self):
        pass
        self.get_cr()
        self.get_3()

    def get_cr(self):
        self.data = pd.read_csv('csv/rankings.csv')
        self.data = self.data.drop('TIERS', axis=1)

        self.data['POS'] = self.data['POS'].str[:2]
        self.player_names = self.data['PLAYER NAME'].tolist()

    def get_3(self):
        return self.data[['PLAYER NAME', 'TEAM', 'POS', 'RK']].head(3)

    def is_a_real_player(self, name):
        return name in self.player_names

    def take_a_player_by_name(self, name):
        pos = self.data[self.data['PLAYER NAME'] == name]['POS'].values[0]
        self.data = self.data.loc[self.data['PLAYER NAME'] != name]
        self.player_names.remove(name)
        return pos

    def take_a_player_by_id(self, id):
        name = self.player_names.pop(id)
        pos = self.data[self.data['PLAYER NAME'] == name]['POS'].values[0]
        self.data = self.data.drop(id)
        return (name, pos)
    
    def reset_indexes(self):
        self.data = self.data.reset_index(drop = True)



    # EI PANDASIA KÄYTTÄVÄT AIKAISEMMAT FUNKTIOT, JUST IN CASE

        # self.ranking = list()
        # self.players = dict()

    


    # def get_cr(self):
    #     #funktio joka lataa consensusrankingin ja tallentaa sen luokan muuttujiin
    #     with open('csv/rankings.csv') as rankings:
    #         file = csv.reader(rankings)

    #         for row in file:
    #             if row[0].isdigit():
    #                 self.ranking.append(row[2])
    #                 #0 - ranking, 2 - nimi, 
    #                 self.players[row[2]] = (row[0], row[4][0:2])
        
    #     #Tarkastetaan että tiedosto on saatu ladattua ja pelaajia on vähintään 200
    #     if len(self.ranking) == len(self.players) and len(self.ranking) > 200: 
    #         print('Ranking ladattu')
    #         print(self.players['Christian McCaffrey'])
    #     #Jos pelaajia alle 200 jotain mennyt pieleen
    #     else:
    #         print('Jotain meni pieleen tiedostoa ladatessa')

    # def get_rank(self):
    #     return self.ranking

    # def get_players(self):
    #     return self.players        

    # def get_3(self):
    #     return [self.ranking[i] for i in range(3)]
    
    # def take_suggested_player(self, index):
    #     self.ranking.pop(index)

    # def is_a_real_player(self, name):
    #     if name in self.players: return True
    #     return False

    # def take_another_player(self, name):
    #     index = self.players[name][0]
    #     self.ranking.pop(int(index)-1)
    #     return int(index) - 1
    
    # def get_position(self, name):
    #     return self.players[name][1]

