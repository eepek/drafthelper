from random import choices
from entities.roster import Roster
from entities.consensusranking import ConsensusRanking



class Draft:
    """"Class that contains functions that are needed during the draft event
    and are used to pick players or retrieve recommended players for user.
    Contains also the user interface functionality that is used in the text-based user interface.

    Attributes:
        roster: Roster object that has access to all the team rosters
        consensusranking: Consensusranking object, access to consensusranking and it's methods
        league_size: number of teams in the league, used solely by text-based interface
        draft_position: users draft position, used solely by text-based interface"""

    def __init__(self, roster: Roster, consensusranking: ConsensusRanking):
        """Class constructor that creates new Draft class

        Args:
            roster: Roster object relayed by App class
            consensusranking: Consensusranking object relayed by App class
        """

        self.roster = roster
        self.consensusranking = consensusranking


        #Tekstikäyttöliittymää varten
        self.league_size = int
        self.draft_position = int

    def set_league_size(self, size: int):
        """Sets the league size to number value specified by user. Only used by text UI

        Args:
            size: Number of teams participating in draft event as int
        """
        self.league_size = size

    def set_draft_positon(self, position:int):
        """Sets the users draft position to value specified by user. Only used by text UI

        Args:
            position: Users teams draft position as int"""
        self.draft_position = position

        self.consensusranking.generate_consensusranking()

    def draft_start(self):
        """Method that runs the text-based interface draft event.
        Runs until draft is completed. With each pick a new player is chosen
        to current team picking. On each pick calls appropriate methods
        depending if it is users or bots turn to choose.
        """
        rounds = self.roster.get_roster_size()

        current_round = 1
        rolling_draft_position = 1

        while current_round <= rounds:
            self.consensusranking.reset_indexes()

            if rolling_draft_position == self.draft_position:
                self.users_turn()

                print(self.roster.get_user_roster())

            else:
                team = 'User' + str(rolling_draft_position)
                self.bot_turn(team)

            if rolling_draft_position < self.league_size:
                rolling_draft_position += 1
            else:
                rolling_draft_position = 1
                current_round += 1

        self.roster.return_all_the_rosters()

    def users_turn_gui(self):
        """Gets recommended players to be shown to user on their turn
        when using the graphical user interface.

        Returns:
            Tuple containing users current roster and the recommended players"""
        user_roster = self.roster.get_user_roster()
        recommended_players = self.get_recommended_players()
        return (user_roster, recommended_players)

    def users_turn(self):
        """Handles the users turn during text-based draft event. Gets recommended players,
        takes users choice and returns it. Only used in text based UI.
        Returns:
            Player chosen by user as tuple with player name and position
        """
        recommend_players_df = self.user_turn_info()
        while True:
            print()
            print('Valitse pelaajan numero tai -1, jos haluat varata muun pelaajan')
            try:
                choice = int(input('Valintasi: '))
            except ValueError:
                print('Virheellinen valinta!')
                continue

            if choice in [-1, 0, 1, 2, 3, 4]:
                if choice == -1:
                    chosen_player = self.get_player_from_user()
                else:
                    player_name = recommend_players_df.at[choice, 'PLAYER NAME']
                    chosen_player = self.choose_player(player_name)
                self.roster.add_to_roster(
                    self.roster.user_team, chosen_player[0], chosen_player[1])

                if chosen_player is False or chosen_player[1] is False:
                    print('Jotain meni vikaan, valitse pelaaja uudelleen')
                    continue

                return chosen_player

    def user_turn_info(self):
        """Shows the information shown on users every turn. Shows users current roster.
        Gets recommended players form Consensusranking object and prints the player
        information for user. Only used in text-based UI.

        Returns:
            Pandas dataframe containing recommended players"""
        print()
        print('Sinun varausvuorosi!')
        print()
        print('Joukkueesi kokoonpano:')
        print(self.roster.get_user_roster())
        print()
        print(self.roster.check_full_positions(self.roster.user_team))
        full_positions = self.roster.check_full_positions(
            self.roster.user_team)
        recommend_players_df = self.consensusranking.get_players(3, full_positions)
        if recommend_players_df is False:
            print("Suositeltuja pelaajia ei tarjolla, ole hyvä ja valitse -1")
            return recommend_players_df
        print(recommend_players_df)
        return recommend_players_df

    def get_player_from_user(self):
        """Used in text interface to get name of the player chosen from the user

        Returns:
            tuple: (players name, playing position)
        """
        while True:
            player = input('Anna pelaajan nimi: ')
            chosen_player = self.choose_player(player)
            if chosen_player is None:
                print(f'Pelaajaa {chosen_player} ei löytynyt')
                continue
            print(f'{chosen_player} valittu')
            return chosen_player


    def get_recommended_players(self):
        """Gets recommended players for the users, taking into account the positions
        that have already been filled in users roster.

        Returns:
            Returns list containing lists for player names, teams and positions
        """
        full_positions = self.roster.check_full_positions(
        self.roster.user_team)
        recommend_players_df = self.consensusranking.get_players(3, full_positions)
        player_names = recommend_players_df['PLAYER NAME'].to_list()
        player_positions = recommend_players_df['POS'].to_list()
        player_teams = recommend_players_df['TEAM'].to_list()
        return [player_names, player_teams, player_positions]

    def choose_player(self, chosen_player: str):
        """Passes chosen players name to consensusranking method that finds the player
        and returns player name and position, if valid request. If player is not found
        or is already taken to a roster, the consensusranking method returns False and
        None is returned

        Args:
            chosen_player (str): Name of the player that has been chosen

        Returns:
            tuple: (Player name, playing position)
        """
        name_and_position = self.consensusranking.take_a_player_by_name(chosen_player.lower())
        if name_and_position is False:
            return None
        return name_and_position

    def bot_turn(self, team_name: str):
        """Method used during bots turn. Gets bot teams name and
        chooses a random player from top 5 players taking into account
        positions that have been filled in the bot teams roster.

        Args:
            team_name: String value for team's name in question

        Returns:
            tuple: (Player name, playing position)
        """

        filled_roster_spots = self.roster.check_full_positions(team_name)
        players_dataframe = self.consensusranking.get_players(
            5, filled_roster_spots)

        # Arvotaan valinta
        possibilities = [0, 1, 2, 3, 4]
        probabilities = [0.4, 0.2, 0.2, 0.1, 0.1]
        choice_id = choices(possibilities, probabilities)[0]

        # Haetaan pelajaa ja lisätään rosteriin
        chosen_player_name = players_dataframe.at[choice_id, 'PLAYER NAME']
        chosen_player = self.consensusranking.take_a_player_by_name(
            chosen_player_name.lower())
        self.roster.add_to_roster(
            team_name, chosen_player[0], chosen_player[1])
        print(f'{team_name} valitsi pelaajan: {chosen_player[0]}')

        return chosen_player
