class Roster:
    """Class that keeps record of all the players selected by teams and which
    roster spots have been filled in each team

    Attributes:
        teams_amount: Number of teams entering the draft
        user_draft_position: Position where users team picks
        bench_counter: Counter used for naming bench positions
        user_team: Users selected team name
        teams: Dictionary containing all the team rosters
        positions: Positions for players in team rosters
        position_amounts: Dictionary containing amount of players in each position to be chosen
        position_counter: Dictionary counting how many players can be chosen to each position
        for each team."""
    def __init__(self, teams: int, user_draft_position: int, user_team_name: str):
        """Creates a new Roster class

        Attributes:
            teams: Number of teams in draft event
            user_draft_position: Users turn number
            user_team_name: Name the user has picked for their team
        """
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
        """Defines positions in rosters and amount of players at each position.
        Calls method to create empty rosters for each team."""
        # Kaikki joukkueet
        # Tämä erillisenä, jotta positioiden muokkaus toiminnallisuus helpompi myöhemmin
        self.positions = ['QB', 'RB1', 'RB2',
                          'WR1', 'WR2', 'WR3', 'TE', 'K', 'DS']
        self.position_amounts = {'QB': 1, 'RB': 2,
                                 'WR': 3, 'TE': 1, 'K': 1, 'DS': 1}

        self.create_empty_rosters()

    def create_empty_rosters(self):
        """Creates empty rosters and position counts for each team"""
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
        """Sets users team name to given value.

        Args:
            name: Given user team name
        """
        self.user_team = name

    def if_rb_or_wr(self, pos, team):
        """If chosen players position is RB or WR, converts the position to wanted
        string format that separates different running backs and wide receivers in team roster

        Args:
            pos: Position of the player (either RB or WR)
            team: Team that chose current player

        Returns:
            Returns position with index added.
            If that position is filled, labels them as bench players with index (BN)
        """
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

    def add_to_roster(self, team: str, name: str, pos: str):
        """Adds chosen player to given teams roster and updates that teams position counter

        Args:
            team: Team choosing the player
            name: Name of the player being chosen
            pos: Playing position of chosen player
        """
        if pos.startswith('K'):
            pos = 'K'
        if pos in ['RB', 'WR']:
            pos = self.if_rb_or_wr(pos, team)
        else:
            self.position_counter[team][pos] -= 1

        self.teams[team][pos] = name

    def check_full_positions(self, team):
        """Returns positions from teams roster that have been filled

        Args:
            team: name of the team requested

        Returns:
            List of positions that are filled for team in question
        """
        return [position for position, amount in self.position_counter[team].items() if amount <= 0]

    def get_user_roster(self):
        """Returns users current roster

        Returns:
            Dictionary containing users currently selected players
        """
        return self.teams[self.user_team]

    def get_roster_size(self):
        """Returns number of positions to be filled during draft

        Returns:
            Integral value of number of positions in roster
        """
        return len(self.positions)

    def return_all_the_rosters(self):
        """"Prints rosters for all the teams    """
        for team, lineup in self.teams.items():
            print(team)
            print('----------------')
            for position, players in lineup.items():
                print(f' {position}: {players}')
