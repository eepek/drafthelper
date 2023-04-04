import unittest
from consensusranking import ConsensusRanking

class ConsensusrankingTest(unittest.TestCase):
    def setUp(self) -> None:
        self.cr = ConsensusRanking('/src/csv/rankings.csv')
        self.cr.get_cr()

    def test_is_a_real_player(self):
        test_set = ['Cooper Kupp', '12345', 'Definitely Not A Real Player', 'lAmAr JacKson']
        result_set = []
        for player in test_set:
            result_set.append(self.cr.is_a_real_player(player))
        correct_set = [True,False,False,True]
        if correct_set == result_set:
            return True
        else:
            return False