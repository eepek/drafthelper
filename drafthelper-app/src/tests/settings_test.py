import unittest
from services.interface import App

class TestRoster(unittest.TestCase):
    def setUp(self):
        self.app = App()
        self.scoring_format = "Test-Format"
        self.position_amounts = {}


    def test_set_changes(self):
        self.app.settings.set_changes(self.scoring_format, self.position_amounts)

    def test_get_changes(self):
        self.test_set_changes()
        return self.assertEqual(self.app.settings.get_changes(), (self.scoring_format, self.position_amounts))
