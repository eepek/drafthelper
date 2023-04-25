from services.roster import Roster
from services.consensusranking import ConsensusRanking
from services.settings import Settings
from services.draft import Draft


class App:
    def __init__(self):
        self.__settings = Settings()
        self.__draft_position = 0
        self.__league_size = 0
        self.__team_name = ""

        self.__roster = Roster(self.__league_size, self.__draft_position)
        self.__cr = ConsensusRanking()

        self.draft = Draft(self.__settings, self.__roster, self.__cr)

    def set_draft_position(self, position: int):
        self.__draft_position = position
    
    def set_league_size(self, size: int):
        self.__league_size = size

    def set_team_name(self, name: str):
        self.__team_name = name


if __name__ == '__main__':
    App()
