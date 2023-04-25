import unittest
from services.interface import App
from services.roster import Roster
from services.consensusranking import ConsensusRanking
from services.draft import Draft
from services.settings import Settings

class TestRoster(unittest.TestCase):
    def setUp(self):
        self.interface = App()

    def test_is_it_users_turn_wrong_postion(self):
        self.interface.set_draft_position(5)
        self.interface.rolling_draft_position = 8
        return self.assertFalse(self.interface.is_it_users_turn())

    def test_increase_counters_next_round_rolling_resets(self):
        self.interface.__league_size = 6
        self.interface.rolling_draft_position = 7
        self.interface.increase_counters()
        return self.assertEqual(1, self.interface.rolling_draft_position)
