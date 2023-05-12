import unittest
from entities.consensusranking import ConsensusRanking


class ConsensusrankingTest(unittest.TestCase):
    def setUp(self) -> None:
        self.consensusranking = ConsensusRanking()
        self.consensusranking.generate_consensusranking()

    def test_is_a_real_player(self):
        test_list = ['Cooper Kupp', '12345',
                    'Definitely Not A Real Player', 'lAmAr JacKson']
        result_list = []
        for player in test_list:
            result_list.append(self.consensusranking.is_a_real_player(player))
        correct_set = [True, False, False, True]
        return self.assertEqual(correct_set,result_list)

    def test_get_players_correct_values(self):
        #Haetaan dataframe, jossa ei pitäisi olla yhtään riviä jonka POS sarakkeen arvo on RB
        player_dataframe = self.consensusranking.get_players(5,['RB'])
        #Otetaan dataframeen mukaan vain rivit joitten POS arvo on erisuuri kuin RB
        player_dataframe = player_dataframe.loc[player_dataframe['POS'] != 'RB']
        #Katsotaan että dataframe on 5x4 kokoinen
        return self.assertEqual(player_dataframe.size,20)

    def test_get_players_if_positions_filled(self):
        full_positions = ['QB','RB','WR','TE','K','DS']
        player_dataframe = self.consensusranking.get_players(5,full_positions)
        return self.assertFalse(player_dataframe)

    def test_get_players_with_negative_amount(self):
        full_positions = []
        player_dataframe = self.consensusranking.get_players(-4,full_positions)
        return self.assertEqual(len(player_dataframe.index),5)

    def test_take_player_by_name_removes_player_from_player_names(self):
        player = 'Austin Ekeler'
        self.consensusranking.take_a_player_by_name(player)
        #Katsotaan onko pelaajaa enää olemassa
        return self.assertFalse(self.consensusranking.is_a_real_player(player))

    def test_take_player_by_name_removes_player_from_dataframe(self):
        player = 'Justin Jefferson'
        self.consensusranking.take_a_player_by_name(player)
        return self.assertFalse(self.consensusranking.take_a_player_by_name(player))

    def test_take_player_by_name_with_wrong_name(self):
        return self.assertFalse(self.consensusranking.take_a_player_by_name('Matti Meikäläinen'))

if __name__ == "__main__":
    unittest.main()