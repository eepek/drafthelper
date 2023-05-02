# Draft Helper käyttöohje

Lataa ohjelman lähdekoodin viimeisin [release](https://github.com/eepek/drafthelper/releases/tag/viikko5)

## Ohjelman asennus ja käyttö

Kaikki seuraavat komennot tulee suorittaa drafthelper-app kansiossa

### Asennus ja suoritus:

Asenna riippuvuudet komennolla:

```bash
poetry install
```

Käynnistääksei graafisen käyttöliittymän version suorita komento:

```bash
poetry run invoke start
```

Jos haluat käyttää ohjelmaa tekstikäyttöliittymällä suorita komento

```bash
poetry run invoke start-txt
```

## Käyttö

Ohjelma kysyy aluksi sinulta liigasi koon ja oman varausvuorosi. Nämä tallennettuasi pääset käynnistämään draft tapahtuman.
Draft tapahtumassa omalla vuorollasi pääset valitsemaan ehdotetuista pelaajista omaan kokoonpanoosi pelaajan, tai tekstipohjaisessa
versiossa voit valita myös hakea pelaaja nimellä. Tietokonepelaajat valitsevat omalla vuorollaan parhaiksi arvioiduista pelaajista
omaan kokoonpanoonsa pelaajat simuloiden oikeaa draft tapahtumaa. Kun varaustilaisuus on saatu päätökseen, ohjelma näyttää sinulle
vielä kaikkien joukkueiden lopulliset kokoonpanot.