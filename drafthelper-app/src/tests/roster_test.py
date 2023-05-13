import unittest
import datetime
from services.interface import App

class TestRoster(unittest.TestCase):
    def setUp(self):
        self.app = App()
        self.app.set_league_size(10)
        self.app.set_draft_position(2)
        self.app.set_team_name('Test Team')
        self.app.start()
        self.roster = self.app.roster

    def test_creates_empty_rosters(self):

        return self.assertEqual(len(self.roster.teams),10) and self.assertEqual(len(self.roster.position_counter),10)

    def test_set_user_team_name_works(self):
        self.roster.set_user_team_name('Testname')
        return self.assertEqual(self.roster.user_team, 'Testname')

    def test_number_the_position_correct_input(self):
        team = 'Test team'
        self.roster.position_counter[team] = {'RB': 2, 'WR': 3}
        rb_position = self.roster.number_the_position('RB', team)
        wr_position = self.roster.number_the_position('WR', team)
        return self.assertEqual(rb_position,'RB1') and self.assertEqual(wr_position,'WR1')

    def test_number_the_position_when_position_filled(self):
        team = 'Test Team'
        self.roster.position_counter[team] = {'RB':0, 'WR':0}
        rb_position = self.roster.number_the_position('RB', team)
        wr_position = self.roster.number_the_position('WR', team)
        return self.assertEqual(rb_position,'BN1') and self.assertEqual(wr_position,'BN2')

    def test_save_final_rosters(self):
        self.assertTrue(self.roster.save_final_rosters().endswith('.txt'))

    def test_get_positions(self):
        positions = ['QB', 'RB1', 'RB2',
                            'WR1', 'WR2', 'WR3', 'TE', 'K', 'DS']
        position_amounts = {'QB': 1, 'RB': 2,
                                    'WR': 3, 'TE': 1, 'K': 1, 'DS': 1}
        return self.assertEqual(self.roster.get_positions(), (positions, position_amounts))

    def test_set_positions(self):
        position_amounts = {'QB': 1, 'RB': 2,
                                    'WR': 2, 'TE': 0, 'K': 1, 'DS': 1}
        correct_positions = ['QB','RB1','RB2','WR1','WR2','K','DS']
        self.roster.set_positions(position_amounts)
        return self.assertEqual(self.roster.positions, correct_positions) and self.assertTrue(self.roster.format_change)
