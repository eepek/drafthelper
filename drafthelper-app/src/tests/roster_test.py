import unittest
from services.roster import Roster

class TestRoster(unittest.TestCase):
    def setUp(self):
        self.roster = Roster(10,2)

    def test_creates_empty_rosters(self):
        return self.assertEqual(len(self.roster.teams),10) and self.assertEqual(len(self.roster.position_counter),10)

    def test_set_user_team_name_works(self):
        self.roster.set_user_team_name('Testname')
        return self.assertEqual(self.roster.user_team, 'Testname')

    def test_if_rb_or_wr_correct_input(self):
        team = 'Test team'
        self.roster.position_counter[team] = {'RB': 2, 'WR': 3}
        rb_position = self.roster.if_rb_or_wr('RB', team)
        wr_position = self.roster.if_rb_or_wr('WR', team)
        return self.assertEqual(rb_position,'RB1') and self.assertEqual(wr_position,'WR1')

    def test_if_rb_or_wr_non_rbwr_input(self):
        position = self.roster.if_rb_or_wr('K','Test team')
        return self.assertEqual(position, 'K')

    def test_if_rb_or_wr_when_position_filled(self):
        team = 'Test Team'
        self.roster.position_counter[team] = {'RB':0, 'WR':0}
        rb_position = self.roster.if_rb_or_wr('RB', team)
        wr_position = self.roster.if_rb_or_wr('WR', team)
        return self.assertEqual(rb_position,'BN1') and self.assertEqual(wr_position,'BN2')

if __name__ == "__main__":
    unittest.main()