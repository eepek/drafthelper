import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):

    def setUp(self):
        self.kassa = Kassapaate()
        

    def test_myydyt_lounaat_ja_rahat_tasmaa(self):
        lounaat = self.kassa.maukkaat + self.kassa.edulliset
        
        if self.kassa.kassassa_rahaa == 100000 and lounaat == 0:
            return True
        
        return False
    
    def test_kateisella_maukkaasti(self):
        kassa = Kassapaate()
        palautus = kassa.syo_maukkaasti_kateisella(500)

        if palautus == 100 and kassa.kassassa_rahaa == 100400:
            return True
        
        return False
    
    def test_kateisella_edullisesti(self):
        kassa = Kassapaate()
        palautus = kassa.syo_edullisesti_kateisella(300)

        if palautus == 50 and kassa.kassassa_rahaa == 100250:
            return True
        
        return False
    
    def test_maksu_ei_riittava_edullisesti(self):
        if self.kassa.syo_edullisesti_kateisella(100) == 100 and self.kassa.kassassa_rahaa == 10000: return True

        return False
    
    def test_maksu_ei_riittava_maukkaasti(self):
        if self.kassa.syo_maukkaasti_kateisella(100) == 100 and self.kassa.kassassa_rahaa == 100000: return True
        
        return False
    
    def test_korttimaksu_toimii_oikein_edullisesti(self):
        kortti = Maksukortti(1000)
        kassa = Kassapaate()

        if kassa.syo_edullisesti_kortilla(kortti) and kortti.saldo == 750 and kassa.edulliset == 1 and kassa.kassassa_rahaa == 100000:
            return True
        return False
    
    def test_korttimaksu_maukkaasti_ei_rahaa(self):
        kortti = Maksukortti(0)
        kassa = Kassapaate()

        if not kassa.syo_maukkaasti_kortilla(kortti) and kortti.saldo == 0 and kassa.maukkaat == 0 and kassa.kassassa_rahaa == 100000:
            return True
        return False
    
    def test_korttimaksu_edullisesti_ei_rahaa(self):
        kortti = Maksukortti(0)
        kassa = Kassapaate()

        if not kassa.syo_edullisesti_kortilla(kortti) and kortti.saldo == 0 and kassa.edulliset == 0 and kassa.kassassa_rahaa == 100000:
            return True
        return False
    
    def test_korttimaksu_toimii_oikein_maukkaasti(self):
        kortti = Maksukortti(1000)
        kassa = Kassapaate()

        if kassa.syo_maukkaasti_kortilla(kortti) and kortti.saldo == 600 and kassa.edulliset == 1 and kassa.kassassa_rahaa == 100000:
            return True
        return False

    def test_kortille_lataus_toimii(self):
        kortti = Maksukortti(0)
        kassa = Kassapaate()
        kassa.lataa_rahaa_kortille(kortti, 100)

        if kortti.saldo == 100 and kassa.kassassa_rahaa == 100000 - 100:
            return True
        return False
    
    def test_negatiivinen_kortille_lataus(self):
        kortti = Maksukortti(100)

        if not self.kassa.lataa_rahaa_kortille(kortti, -10):
            return True
        return False