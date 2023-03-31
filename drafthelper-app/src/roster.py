import pandas as pd

class Roster:

    def __init__(self, teams: int, userDrafPos: int):
        #Oman joukkueeen nimi
        self.userTeam = 'YourOwnTeam'
        #Kaikki joukkueet
        self.teams = dict()
        #Tämä erillisenä, jotta positioiden muokkaus toiminnallisuus helpompi myöhemmin
        self.positions = ['QB','RB1','RB2','WR1','WR2','WR3','TE','K','DEF','IDP']
        self.positionAmounts = {'QB':1,'RB':2,'WR':3,'TE':1,'K':1,'DEF':1,'IDP':1}
        #Joukkuekohtaiset positiot tulee tästä listasta
        self.posDict = {'QB':'','RB1':'','RB2':'','WR1':'','WR2': '', 'WR3': '', 'TE':'','K':'','DEF':''}
        #PositioCountteri per joukkue
        self.positionCounter = dict()

        #Alustetaan dictionaryt, TEE TÄSTÄ OMA FUNKTIO    
        # for pos in self.positions:
        #     self.posDict[pos] = ''

        for i in range(0,teams+1):
            if i == userDrafPos:
                self.teams[self.userTeam] = {'QB':'','RB1':'','RB2':'','WR1':'','WR2': '', 'WR3': '', 'TE':'','K':'','DEF':''}
                self.positionCounter[self.userTeam] = {'QB':1,'RB':2,'WR':3,'TE':1,'K':1,'DEF':1,'IDP':1}
            else:
                if i < userDrafPos:
                    i = i+1
                    
                self.teams['User' + str(i)] = {'QB':'','RB1':'','RB2':'','WR1':'','WR2': '', 'WR3': '', 'TE':'','K':'','DEF':''}
                self.positionCounter['User' + str(i)] = {'QB':1,'RB':2,'WR':3,'TE':1,'K':1,'DEF':1,'IDP':1}

        

    def setUserTeamName(self, name:str):
        self.userTeam = name

    def ifRBorWR(self, pos, team):
        if pos == 'RB':
            number = 3 - self.positionCounter[team]['RB']
            pos = pos + str(number)
            if number >= 3:
                #TÄHÄN AIKANAAN RAJOITUS VALITTAVILLE PELAAJILLE (TAI PENKKIPAIKAT)
                pos = 'BN' + str(number-3)
            self.positionCounter[team]['RB'] -= 1
        elif pos == 'WR':
            number = 4 - self.positionCounter[team]['WR']
            pos = pos + str(number)
            if number >= 4:
                #TÄHÄN AIKANAAN RAJOITUS VALITTAVILLE PELAAJILLE (TAI PENKKIPAIKAT)
                pos = 'BN' + str(number-3)
            self.positionCounter[team]['WR'] -= 1

        return pos

    def addToUserRoster(self, name: str, pos: str):
        if pos in ['RB','WR']:
            pos = self.ifRBorWR(pos, self.userTeam)    
        self.teams[self.userTeam][pos] = name
        print(self.teams[self.userTeam])

    def addToBotRoster(self, team, name, pos):
        if pos in ['RB','WR']:
            pos = self.ifRBorWR(pos, team)
        self.teams[team][pos] = name
        print(self.teams[team])    
        

    def getUserRoster(self):
        return self.teams[self.userTeam]
    
    def getRosterSize(self):
        return len(self.positions)
    

