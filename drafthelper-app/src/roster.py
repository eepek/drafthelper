class Roster:

    def __init__(self, teams: int, user_draft_position: int):
        #Oman joukkueeen nimi
        self.user_team = 'YourOwnTeam'
        #Kaikki joukkueet
        self.teams = dict()
        #Tämä erillisenä, jotta positioiden muokkaus toiminnallisuus helpompi myöhemmin
        self.positions = ['QB','RB1','RB2','WR1','WR2','WR3','TE','K','DS']
        self.position_amounts = {'QB':1,'RB':2,'WR':3,'TE':1,'K':1,'DS':1}
        #Joukkuekohtaiset positiot tulee tästä listasta
        self.pos_dict = {'QB':'','RB1':'','RB2':'','WR1':'','WR2': '', 'WR3': '', 'TE':'','K':'','DS':''}
        #PositioCountteri per joukkue
        self.position_counter = dict()

        #Alustetaan dictionaryt, TEE TÄSTÄ OMA FUNKTIO    
        # for pos in self.positions:
        #     self.pos_dict[pos] = ''

        for i in range(0,teams+1):
            if i == user_draft_position:
                self.teams[self.user_team] = {'QB':'','RB1':'','RB2':'','WR1':'','WR2': '', 'WR3': '', 'TE':'','K':'','DS':''}
                self.position_counter[self.user_team] = {'QB':1,'RB':2,'WR':3,'TE':1,'K':1,'DS':1}
            else:
                if i < user_draft_position:
                    i = i+1
                    
                self.teams['User' + str(i)] = {'QB':'','RB1':'','RB2':'','WR1':'','WR2': '', 'WR3': '', 'TE':'','K':'','DS':''}
                self.position_counter['User' + str(i)] = {'QB':1,'RB':2,'WR':3,'TE':1,'K':1,'DS':1}

        

    def set_user_team_name(self, name:str):
        self.user_team = name

    def if_RB_or_WR(self, pos, team):
        if pos == 'RB':
            number = 3 - self.position_counter[team]['RB']
            pos = pos + str(number)
            if number >= 3:
                #TÄHÄN AIKANAAN RAJOITUS VALITTAVILLE PELAAJILLE (TAI PENKKIPAIKAT)
                pos = 'BN' + str(number-3)
            self.position_counter[team]['RB'] -= 1
        elif pos == 'WR':
            number = 4 - self.position_counter[team]['WR']
            pos = pos + str(number)
            if number >= 4:
                #TÄHÄN AIKANAAN RAJOITUS VALITTAVILLE PELAAJILLE (TAI PENKKIPAIKAT)
                pos = 'BN' + str(number-3)
            self.position_counter[team]['WR'] -= 1

        return pos

    def add_to_user_roster(self, name: str, pos: str):
        if pos in ['RB','WR']:
            pos = self.if_RB_or_WR(pos, self.user_team)
        if pos.startswith('K'):
            pos = 'K'    
        self.teams[self.user_team][pos] = name
        print(self.teams[self.user_team])

    def add_to_bot_roster(self, team, name, pos):
        if pos in ['RB','WR']:
            pos = self.if_RB_or_WR(pos, team)
        if pos.startswith('K'):
            pos = 'K'
        self.teams[team][pos] = name    
        

    def get_user_roster(self):
        return self.teams[self.user_team]
    
    def get_roster_size(self):
        return len(self.positions)
    

