import unittest
from services.draft import Draft
from services.roster import Roster
from services.consensusranking import ConsensusRanking


class TestRoster(unittest.TestCase):
    def setUp(self):
        self.roster = Roster(10,2,'TeamName')
        self.consensusranking = ConsensusRanking()
        self.roster.initialize()
        self.consensusranking.generate_consensusranking()
        self.draft = Draft(self.roster, self.consensusranking)

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