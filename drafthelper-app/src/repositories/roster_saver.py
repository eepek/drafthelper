import os

class RosterRepository:
    """Class used for saving results of the draft in text file.

    Attributes:
        teams (dict): Dictionary containing rosters for all the
        teams participating in the draft
        filename (str): Filename for text file to be saved
        """
    def __init__(self, teams: dict, filename: str):
        """Constructs a RosterRepository class

        Args:
            teams (dict): Dictionary containing rosters for all the
        teams participating in the draft
            filename (str): Filename for text file to be saved
        """
        self.__teams = teams
        self.__filename = filename

    def save_rosters(self):
        """Method that saves the rosters in to the text file

        Returns:
            str: File path of the saved file
        """
        directory = os.path.dirname(__file__)
        path = os.path.join(directory, '../../data/save_files')
        with open(path + self.__filename +'.txt', 'w', encoding='UTF-8') as save_file:
            for team, roster in self.__teams.items():
                save_file.write('--------------- \n')
                save_file.write(f'{team} \n')
                save_file.write('--------------- \n')
                for position, player in roster.items():
                    save_file.write(f'{position}:  {player} \n')
        return path + self.__filename + '.txt'
