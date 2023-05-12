
class Settings:
    """Class that is used text based interface to get the number of teams
    in the league and draft position from the user. Stores the league size
    (number of teams) and users draft position and in GUI is used to store
    the user selected scoring format and roster position amounts.

    Attributes:
        league_size (int): Number of teams in the league
        draft_position (int): Turn number for users turn
        scoring (str): User chosing scoring format
        position_amounts (dict): Keys are players and their values are maximum
        amounts of players for given key
    """
    def __init__(self):
        """Constructs a new Settings class
        """
        self.__league_size = int()
        self.__draft_position = int()
        self._scoring = str()
        self._position_amounts = dict()

    def settings(self):
        """In text based user interface gets league size and draft position
        from the user.
        """
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
        """Returns number of teams in the league

        Returns:
            int: Number of teams in the league
        """
        return self.__league_size

    def get_draft_position(self):
        """Returns user draft position

        Returns:
            int: User draft position
        """
        return self.__draft_position

    def set_changes(self, scoring: str, position_amounts: dict):
        """Sets the scoring and position_amounts variables
        to user given values

        Args:
            scoring (str): User given scoring format (PPR, Half-PPR, Standard)
            position_amounts (dict): User given number of players for each position
        """
        self._scoring = scoring
        self._position_amounts = position_amounts

    def get_changes(self):
        """Returns scoring format and position amount values

        Returns:
            str, dict: Scoring format, amount of players in each position
        """
        return self._scoring, self._position_amounts
