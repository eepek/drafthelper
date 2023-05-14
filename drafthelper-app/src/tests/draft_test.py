import unittest
from entities   .roster import Roster
from entities.consensusranking import ConsensusRanking
from services.interface import App


class DraftTest(unittest.TestCase):
    def setUp(self):
        self.app = App()
        self.app.set_league_size(10)
        self.app.set_draft_position(2)
        self.app.set_team_name('Test Team')
        self.app.start()

    def test_users_turn_gui(self):
        team = self.app.roster.teams['Test Team'] = {'QB': 'Test QB'}
        result = self.app.draft.users_turn_gui()
        return self.assertEqual(result[0], team)

    def test_set_league_size(self):
        self.app.draft.set_league_size(8)
        return self.assertEqual(self.app.draft.league_size, 8)

    def test_set_draft_position(self):
        self.app.draft.set_draft_positon(6)
        return self.assertEqual(self.app.draft.draft_position, 6)


    def test_choice_by_id_wrong_name(self):
        name = 'Not A Real Name'
        return self.assertFalse(self.app.draft.choose_player(name))

    def test_choice_by_id_real_name(self):
        name = 'Justin Jefferson'
        return self.assertTrue(self.app.draft.choose_player(name))

    def test_bot_choice(self):
        chosen = self.app.draft.bot_turn(self.app.roster.team_names[1])
        #Onko oikea pelaaja
        if self.app.consensusranking.is_a_real_player(chosen[0]):
            return chosen[1] in ['QB','RB','WR','TE','K','DS']

    def test_get_recommended_players(self):
        player_data = self.app.draft.get_recommended_players()
        if len(player_data) == 3:
            for player in player_data[0]:
                if not self.app.consensusranking.is_a_real_player(player):
                    return False
            if len(player_data[1]) == 3:
                return False
            for position in player_data[2]:
                if position not in ['QB','RB','WR','TE','K','DS']:
                    return False

        return True
