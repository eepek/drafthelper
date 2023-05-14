import unittest
from services.interface import App
from entities.roster import Roster
from entities.consensusranking import ConsensusRanking

class TestInterface(unittest.TestCase):
    def setUp(self):
        self.interface = App()
        self.interface.roster = Roster(10,5,'Team')
        self.interface.consensusranking = ConsensusRanking()


    def test_is_it_users_turn_wrong_postion(self):
        self.interface.set_draft_position(5)
        self.interface.rolling_draft_position = 8
        return self.assertFalse(self.interface.is_it_users_turn())

    def test_increase_counters_next_round_rolling_resets(self):
        self.interface.__league_size = 6
        self.interface.rolling_draft_position = 7
        self.interface.increase_counters()
        return self.assertEqual(1, self.interface.rolling_draft_position)

    #Test getters and setters

    def test_get_all_teams(self):
        test_teams = {'Test Team': {'QB': 'Tester', 'RB': 'Testy McTestFace'}}
        self.interface.roster.teams =  test_teams
        return self.assertEqual(self.interface.get_all_teams(),test_teams)

    def test_set_changes(self):
        self.interface.set_format_change(True)

    def test_set_draft_postion(self):
        self.interface.set_draft_position(1)
        return self.assertTrue(self.interface.is_it_users_turn())

    def test_get_draft_position(self):
        return self.assertEqual(1, self.interface.get_draft_position())

    def test_get_current_round(self):
        return self.assertEqual(1, self.interface.get_current_round())

    def test_set_league_size(self):
        self.interface.set_league_size(10)
        return self.assertEqual(10, self.interface.get_league_size())

    def test_get_league_size(self):
        self.interface.set_league_size(5)
        return self.assertNotEqual(10, self.interface.get_league_size())

    def test_set_team_name(self):
        self.interface.set_team_name('TestTeam')
        for name in self.interface.get_team_names():
            if self.assertEqual('TestTeam', name):
                return True

        return False

    def test_format_changes(self):
        self.test_set_changes()
        self.interface.settings.set_changes('PPR', {})
        self.interface.start()
        return self.assertTrue(self.interface.roster.format_change)
