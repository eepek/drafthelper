import os
import pandas as pd

class ConsensusrankingRepository:
    """Repository class used for reading the given csv file and loading it as Pandas Dataframe
    which is passed into Consensusranking class

    Attributes:
        data: Dataframe in which information from CSV file is stored
        directory: Current working directory
        filename: Given filename defining which CSV file will be loaded
        file: Path to the desired file
    """

    def __init__(self, filename: str):
        """Constructs a ConsensusRankingRepository class

        Args:
            filename (str): Name of the CSV file to be fetched
        """
        self.__data = pd.DataFrame()
        self.__directory = os.path.dirname(__file__)
        self.__filename = filename
        self.__file = os.path.join(self.__directory, '../../data/csv/', self.__filename)

    def get_dataframe(self):
        """Reads the csv file and removes tiers column and reformats Position column values

        Returns:
            DataFrame: Pandas Dataframe with ranking to ConsensusRanking class
        """
        self.__data = pd.read_csv(self.__file)
        self.__data = self.__data.drop('TIERS', axis=1)
        self.__data['POS'] = self.__data['POS'].str[:2]

        return self.__data
