import unittest
from services.draft import Draft
from entities.roster import Roster
from entities.consensusranking import ConsensusRanking


class TestRoster(unittest.TestCase):
    def setUp(self):
        self.roster = Roster(10,2,'TeamName')
        self.consensusranking = ConsensusRanking()
        self.roster.initialize()
        self.consensusranking.generate_consensusranking()
        self.draft = Draft(self.roster, self.consensusranking)
        self.draft.roster = self.roster
        self.draft.consensusranking = self.consensusranking

    def test_set_league_size(self):
        self.draft.set_league_size(8)
        return self.assertEqual(self.draft.league_size, 8)

    def test_set_draft_position(self):
        self.draft.set_draft_positon(6)
        return self.assertEqual(self.draft.draft_position, 6)


    def test_choice_by_id_wrong_name(self):
        name = 'Not A Real Name'
        return self.assertFalse(self.draft.choice_by_id(name))

    def test_choice_by_id_real_name(self):
        name = 'Justin Jefferson'
        return self.assertTrue(self.draft.choice_by_id(name))

    def test_bot_choice(self):
        chosen = self.draft.bot_turn('User1')
        #Onko oikea pelaaja
        if self.consensusranking.is_a_real_player(chosen[0]):
            return chosen[1] in ['QB','RB','WR','TE','K','DS']

    def test_get_recommended_players(self):
        player_data = self.draft.get_recommended_players()
        if len(player_data) == 3:
            for player in player_data[0]:
                if not self.consensusranking.is_a_real_player(player):
                    return False
            if len(player_data[1]) == 3:
                return False
            for position in player_data[2]:
                if position not in ['QB','RB','WR','TE','K','DS']:
                    return False

        return True
