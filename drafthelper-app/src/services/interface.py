from services.roster import Roster
from services.consensusranking import ConsensusRanking
from services.draft import Draft
from services.settings import Settings


class App:
    def __init__(self):
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



    #Graafinen käyttöliittymä
    def start(self):

        self.roster = Roster(self.__league_size, self.__draft_position, self.__team_name)
        self.roster.initialize()
        self.rounds = self.roster.get_roster_size()
        self.consensusranking.generate_consensusranking()

        self.draft = Draft(self.roster, self.consensusranking)

    #Tekstipohjainen käyttöliittymä
    def start_txt(self):
        self.settings = Settings() #Pylint errori tiedossa, mutta en vielä keksinyt tapaa korjata
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
        self.__draft_position = position

    def get_draft_position(self):
        return self.rolling_draft_position

    def get_initial_draft_position(self):
        return self.__draft_position

    def get_current_round(self):
        return self.current_round

    def set_league_size(self, size: int):
        self.__league_size = size

    def get_league_size(self):
        return self.__league_size

    def set_team_name(self, name: str):
        self.__team_name = name


# TURN RELATED METHODS

    def is_it_users_turn(self):
        return self.rolling_draft_position == self.__draft_position

    def increase_counters(self):
        if self.rolling_draft_position < self.__league_size:
            self.rolling_draft_position += 1
        else:
            self.rolling_draft_position = 1
            self.current_round += 1
        if self.current_round > self.roster.get_roster_size():
            self.is_draft_done = True

    def users_turn(self):
        self.user_choices = self.draft.users_turn_gui()[1]
        self.increase_counters()
        return self.user_choices

    def player_chosen_by_user(self, ident: int):
        player = self.user_choices[0][ident]
        position = self.user_choices[2][ident]
        self.draft.choice_by_id(player)
        self.roster.add_to_roster(self.__team_name, player, position)

    def bot_turn(self):
        team = 'User' + str(self.rolling_draft_position)
        self.increase_counters()
        return self.draft.bot_turn(team)


if __name__ == '__main__':
    App()
