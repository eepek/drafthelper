from random import shuffle
from entities.roster import Roster
from entities.consensusranking import ConsensusRanking
from entities.settings import Settings
from services.draft import Draft
from ui.ui_text import TextUI


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
        team_names: Team names that will be chosen for the bot teams
        """


    def __init__(self):
        """Class constructor that creates a new interface class"""
        self.__draft_position = 0
        self.__league_size = 0
        self.__team_name = ""
        self.is_draft_done = False
        self._format_changes = False

        self.roster = Roster(self.__league_size, self.__draft_position, self.__team_name)
        self.consensusranking = ConsensusRanking()
        self.draft = Draft(self.roster, self.consensusranking)
        self.txt_ui = TextUI(self.draft, self.roster, self.consensusranking)

        self.rounds = 0
        self.current_round = 1
        self.rolling_draft_position = 1
        self.user_choices = []

        #Tekstikäyttöliittymää varten
        self.settings = Settings()

        self.team_names = ["DAKstreet Boys", "Russell Sprouts", "Baskin Dobbins",
                           "Baby Chark", "Judge Jeudy", "Waddle Vision", "Breakin’ T-Law",
                           "Obi-Wan Jakobi", "Brees Knees", "Aaron It Out", "Burrowito Bowl",
                           "Run CMC", "Aiyuken!", "Chark Week", "Fort Knox", "Kittle Corn",
                           "Boyds to Men", "Zeke and Destroy"]



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
        if self._format_changes:
            scoring, position_amounts = self.settings.get_changes()
            self.roster.set_positions(position_amounts)
            self.consensusranking.set_filename(scoring)
        shuffle(self.team_names)
        self.roster.set_team_names(self.team_names)
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

        #Tekstikäyttöliittymää varten
        self.settings.settings()
        self.__league_size = self.settings.get_league_size()
        self.__draft_position = self.settings.get_draft_position()
        self.__team_name = "Your Team"
        self.roster = Roster(self.__league_size, self.__draft_position, self.__team_name)
        self.roster.set_team_names(self.team_names)
        self.roster.initialize()
        self.consensusranking.generate_consensusranking()
        self.draft = Draft(self.roster, self.consensusranking)
        self.draft.set_draft_positon(self.__draft_position)
        self.draft.set_league_size(self.__league_size)
        self.txt_ui = TextUI(self.draft, self.roster, self.consensusranking)
        self.txt_ui.draft_start()

#GETTERS AND SETTERS

    def set_format_change(self, change: bool):
        """If user changes league settings via the option menu
        variable self._format_changes is set to True to indicate
        other functions to use those settings for scoring and
        position amounts instead of default values.

        Args:
            change (bool): Boolean that indicates if default or user set
            settings are used for scoring and position amounts.
        """
        self._format_changes = change


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
        team = self.team_names[self.rolling_draft_position]
        self.increase_counters()
        return self.draft.bot_turn(team)

    #After draft
    def save_draft(self):
        """After the draft when save button is clicked
        calls Roster class to save the current rosters

        Returns:
            str: Returns filename for saved .txt file
        """
        return self.roster.save_final_rosters()
