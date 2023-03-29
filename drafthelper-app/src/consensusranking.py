import csv

class ConsensusRanking:

    def __init__(self) -> None:
        self.ranking = list()
        self.players = dict()

    def get_cr(self):
        #funktio joka lataa consensusrankingin ja tallentaa sen luokan muuttujiin
        with open('csv/rankings.csv') as rankings:
            file = csv.reader(rankings)

            for row in file:
                if row[0].isdigit():
                    self.ranking.append(row[2])
                    self.players[row[2]] = (row[0], row[4][0:2])
        
        #Tarkastetaan että tiedosto on saatu ladattua ja pelaajia on vähintään 200
        if len(self.ranking) == len(self.players) and len(self.ranking) > 200: 
            print('Ranking ladattu')
        #Jos pelaajia alle 200 jotain mennyt pieleen
        else:
            print('Jotain meni pieleen rankingia ladatessa')

    def get_rank(self):
        return self.ranking

    def get_players(self):
        return self.players        
