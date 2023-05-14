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

    def users_turn_gui(self):
        """Gets recommended players to be shown to user on their turn
        when using the graphical user interface.

        Returns:
            Tuple containing users current roster and the recommended players"""
        user_roster = self.roster.get_user_roster()
        recommended_players = self.get_recommended_players()
        return (user_roster, recommended_players)

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

        return chosen_player
