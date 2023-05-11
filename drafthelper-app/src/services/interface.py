from services.roster import Roster
from services.consensusranking import ConsensusRanking
from services.draft import Draft
from services.settings import Settings


class App:
    """Class that works as interface between Draft, Roster,
    Consensusranking and UI classes. Gets and relays information
    the classes need and information that is shown to the users

    Attributes:
        draft_position: Users turn number during the draft
        league_size: Number of teams that participate in the draft event. User + bot teams
        team_name: Name of the users team that user has entered
        is_draft_done: Boolean that is used to indicate if all the rounds
        and turns of the draft have been done

        roster: Roster object used by interface, that contains all the infomation about users team
        consensusranking: Consensusranking object, that contains all the player
        availeable for the draft and their ranking
        draft: Draft object that contains most of the methods needed during the draft

        rounds: number of rounds in the draft
        current_round: current round going on during the draft
        rolling_draft_position: shows currently whose turn it is during the draft
        user_choices: list that contains players that are
        represented to the user during his/her turn
        """


    def __init__(self):
        """Class constructor that creates a new interface class"""
        self.__draft_position = 0
        self.__league_size = 0
        self.__team_name = ""
        self.is_draft_done = False

        self.roster = Roster(self.__league_size, self.__draft_position, self.__team_name)
        self.consensusranking = ConsensusRanking()
        self.draft = Draft(self.roster, self.consensusranking)

        self.rounds = 0
        self.current_round = 1
        self.rolling_draft_position = 1
        self.user_choices = []

        #Tekstikäyttöliittymää varten
        self.settings = Settings()



    #Graafinen käyttöliittymä
    def start(self):
        """Relays league_size, draft_position and team name information
        that user has entered in the settings to the Roster class.
        Calls roster class to initialize the roster with given information
        and retrieves round information based on the settings.
        Calls for Consensusranking to create new accessible ranking list of players.
        Relays Consensusranking and updated roster information to Draft class.
        """
        self.roster = Roster(self.__league_size, self.__draft_position, self.__team_name)
        self.roster.initialize()
        self.rounds = self.roster.get_roster_size()
        self.consensusranking.generate_consensusranking()

        self.draft = Draft(self.roster, self.consensusranking)

    #Tekstipohjainen käyttöliittymä
    def start_txt(self):
        """Does necessary intialization that text-based user interface needs.
        Calls for Settings class that retrivies setting information
        from user. Relays necessary information to Roster and Draft classes
        and sets up Consensusranking for use.
        """
        self.__league_size = self.settings.get_league_size()
        self.__draft_position = self.settings.get_draft_position()
        self.roster = Roster(self.__league_size, self.__draft_position, self.__team_name)
        self.roster.initialize()
        self.consensusranking.generate_consensusranking()
        self.draft = Draft(self.roster, self.consensusranking)
        self.draft.set_draft_positon(self.__draft_position)
        self.draft.set_league_size(self.__league_size)
        self.draft.draft_start()

#GETTERS AND SETTERS


    def set_draft_position(self, position: int):
        """Sets the draft position to position user has given.

        Args:
            position: Number of position user has for the draft
        """
        self.__draft_position = position


    def get_draft_position(self):
        """Returns current rolling draft position

        Returns:
            Returns current rolling draft position as int
        """
        return self.rolling_draft_position

    def get_current_round(self):
        """Returns current round during draft

        Returns:
            Current round during draft as int
        """
        return self.current_round


    def set_league_size(self, size: int):
        """Sets league_size to user entered value

        Args:
            size: the number of teams that participate in the draft
        """
        self.__league_size = size


    def get_league_size(self):
        """Returns number of teams participating in the draft

        Returns:
            Number of teams participating in draft as int
        """
        return self.__league_size


    def set_team_name(self, name: str):
        """Sets team name to value given by user

        Args:
            name: Name user has given for their team"""
        self.__team_name = name


    def get_all_teams(self):
        """Gets all the teams and their rosters from Roster class

        Returns:
            Returns dictionary of all the teams in the draft.
            Each dictionary key has that teams roster as dictionary as their value.
        """
        return self.roster.teams

    def get_team_names(self):
        """Returns names for all the teams

        Returns:
            Returns all the team names as list
        """
        return self.roster.teams.keys()


# TURN RELATED METHODS

    def is_it_users_turn(self):
        """Checks if current turn in draft is users turn

        Returns:
            Boolean - True if it is users turn, otherwise False
        """
        return self.rolling_draft_position == self.__draft_position

    def increase_counters(self):
        """Increases rolling_draft_position counter after each pick.
        If it is the last pick of the round, resets rolling_draft_position to 1 and
        increases current_round. At the end of draft,
        sets is_draft_done to True to indicate that draft is complete."""

        if self.rolling_draft_position < self.__league_size:
            self.rolling_draft_position += 1
        else:
            self.rolling_draft_position = 1
            self.current_round += 1
        if self.current_round > self.roster.get_roster_size():
            self.is_draft_done = True

    def users_turn(self):
        """Gets players to choose from the user on his/her turn from Draft class.
        Calls increase_counters method for next pick.

        Returns:
            List containing three listst Player names, Teams and Positions
        """
        self.user_choices = self.draft.users_turn_gui()[1]
        self.increase_counters()
        return self.user_choices

    # def player_chosen_by_user(self, ident: int):
    #     """Gets the player chosen by the user from user interface
    #     and relays it to Roster class to be saved into users roster."""
    #     player = self.user_choices[0][ident]
    #     position = self.user_choices[2][ident]
    #     self.draft.choose_player(player)
    #     self.roster.add_to_roster(self.__team_name, player, position)

    def find_player_by_name(self, name: str):
        """Adds player by name to users roster
        """
        chosen = self.draft.choose_player(name)
        if chosen is not None:
            self.roster.add_to_roster(self.__team_name, chosen[0], chosen[1])
        return chosen

    def bot_turn(self):
        """Checks the current bot users name. Calls the increase counters
        and gets randomized choice for bot player that is relayed to the user interface

        Returns:
            Player chosen by bot user as tuple containing player name and position"""
        team = 'User' + str(self.rolling_draft_position)
        self.increase_counters()
        return self.draft.bot_turn(team)

    #After draft
    def save_draft(self):
        return self.roster.save_final_rosters()




# if __name__ == '__main__':
#     App()
