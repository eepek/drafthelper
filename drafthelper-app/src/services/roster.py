class Roster:

    def __init__(self, teams: int, user_draft_position: int, user_team_name: str):
        self.teams_amount = teams
        self.user_draft_position = user_draft_position
        self.bench_counter = 1

        # Oman joukkueeen nimi
        self.user_team = user_team_name

        #initialize
        self.teams = {}
        self.positions = {}
        self.position_amounts = {}
        self.position_counter = {}


    def initialize(self):
        # Kaikki joukkueet
        # Tämä erillisenä, jotta positioiden muokkaus toiminnallisuus helpompi myöhemmin
        self.positions = ['QB', 'RB1', 'RB2',
                          'WR1', 'WR2', 'WR3', 'TE', 'K', 'DS']
        self.position_amounts = {'QB': 1, 'RB': 2,
                                 'WR': 3, 'TE': 1, 'K': 1, 'DS': 1}
        # PositioCountteri per joukkue
        self.position_counter = {}

        self.create_empty_rosters()

    def create_empty_rosters(self):
        for i in range(1, self.teams_amount+1):
            if i == self.user_draft_position:
                team_name = self.user_team

            else:
                team_name = f'User{str(i)}'

            for position in self.positions:
                if team_name in self.teams:
                    self.teams[team_name][position] = ''
                else:
                    self.teams[team_name] = {position: ''}

            for position, amount in self.position_amounts.items():
                if team_name in self.position_counter:
                    self.position_counter[team_name][position] = amount
                else:
                    self.position_counter[team_name] = {position: amount}

    def set_user_team_name(self, name: str):
        self.user_team = name

    def if_rb_or_wr(self, pos, team):
        if pos == 'RB':
            number = 3 - self.position_counter[team]['RB']
            pos = pos + str(number)
            if number >= 3:
                # TÄHÄN AIKANAAN RAJOITUS VALITTAVILLE PELAAJILLE (TAI PENKKIPAIKAT)
                pos = 'BN' + str(self.bench_counter)
                self.bench_counter += 1
            self.position_counter[team]['RB'] -= 1
        elif pos == 'WR':
            number = 4 - self.position_counter[team]['WR']
            pos = pos + str(number)
            if number >= 4:
                # TÄHÄN AIKANAAN RAJOITUS VALITTAVILLE PELAAJILLE (TAI PENKKIPAIKAT)
                pos = 'BN' + str(self.bench_counter)
                self.bench_counter += 1
            self.position_counter[team]['WR'] -= 1

        return pos

    def add_to_roster(self, team, name, pos: str):
        if pos.startswith('K'):
            pos = 'K'
        if pos in ['RB', 'WR']:
            pos = self.if_rb_or_wr(pos, team)
        else:
            self.position_counter[team][pos] -= 1

        self.teams[team][pos] = name

    def check_full_positions(self, team):
        return [position for position, amount in self.position_counter[team].items() if amount <= 0]

    def get_user_roster(self):
        return self.teams[self.user_team]

    def get_roster_size(self):
        return len(self.positions)

    def return_all_the_rosters(self):
        for team, lineup in self.teams.items():
            print(team)
            print('----------------')
            for position, players in lineup.items():
                print(f' {position}: {players}')
