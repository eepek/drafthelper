import unittest
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):

    def setUp(self) -> None:
        self.kassa = Kassapaate()
        

    def myydyt_lounaat_ja_rahat_tasmaa(self):
        lounaat = self.kassa.maukkaat + self.kassa.edulliset
        
        if self.kassa.kassassa_rahaa == 100000 and lounaat == 0:
            return True
        
        return False