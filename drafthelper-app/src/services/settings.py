
class Settings:
    def __init__(self):
        self.__league_size = int()
        self.__draft_position = int()
        self.settings()

    def settings(self):
        # Määritetään liigan koko

        while self.__league_size < 6 or self.__league_size > 14:
            self.__league_size = int(input('Liigan koko (6-14 joukkuetta): '))

        # Määritetään draft positio

        while True:
            self.__draft_position = int(input('Millä numerolla pääset varaamaan: '))
            if self.__draft_position < 0 or self.__draft_position >= self.__league_size:
                print()
                print(f'Anna numero välillä 1 - {self.__league_size}')
            else:
                break

    def get_league_size(self):
        return self.__league_size

    def get_draft_position(self):
        return self.__draft_position
