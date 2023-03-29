class Roster:
    def __init__(self):
        self.roster = dict()
        #Tämä erillisenä jotta toiminnalisuus rosterin muuttamiseen helpompi tulevaisuudessa
        self.positions = ['QB','RB','RB','WR','WR','WR','TE','K','DEF', 'IDP']

    def newRoster(self):
        for pos in self.positions:
            self.roster[pos] = ''
        
        return True
    
    def getRosterSize(self):
        return len(self.positions)