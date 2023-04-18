from services.roster import Roster
from services.consensusranking import ConsensusRanking
from services.settings import Settings
from services.draft import Draft


class App:
    def __init__(self):
        self.__settings = Settings()
        self.__draft_position = self.__settings.get_draft_position()
        self.__league_size = self.__settings.get_league_size()
        self.__roster = Roster(self.__league_size, self.__draft_position)
        self.__cr = ConsensusRanking()

        self.draft = Draft(self.__settings, self.__roster, self.__cr)


if __name__ == '__main__':
    App()
