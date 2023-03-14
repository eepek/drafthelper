import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_on_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataaminen_toimii_oikein(self):
        self.maksukortti.lataa_rahaa(1000)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 20.00 euroa")

    def test_rahan_ottaminen_toimii_kun_saldoa_on(self):
        self.maksukortti.ota_rahaa(800)
        if self.maksukortti.saldo == 200:
            return True
        return False

    def test_rahan_ottaminen_ei_toimi_kun_saldo_ei_riita(self):
        self.maksukortti.ota_rahaa(1200)
        if self.maksukortti.saldo != 1000:
            return False
        return True
