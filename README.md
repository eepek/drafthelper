# Draft Helper

Draft helper on ohjelma, jonka tarkoitus on auttaa käyttäjää harjoittelemaan ja kokeilemaan erilaisia skenaarioita NFL:n fantasia liigan varaustilaisuutta varten. Ohjelma mahdollistaa 6-14 joukkueen Full-PPR liigojen varaustilaisuuden mallinnuksen. Käyttäjän tueksi ohjelmisto tarjoaa Fantasy Pros sivuston useamman asiantuntijan arvioista koostaman konsensus arvion kolme parasta pelaajaa, jokaisella käyttäjän varausvuorolla. Käyttäjä voi myös valita muun pelaajan kirjoittamalla pelaajan nimen. Muitten varausvuorolla, ohjelmisto valitsee kyseisen vuoron joukkueeseen pelaajan konsensulistan kärkiviisikosta.

Ohjelma on Helsingin Yliopiston Tietojenkäsittelytieteen Ohjelmistotekniikan kurssin harjoitustyö.

## Toiminnallisuudet (25.4.2023)
- Ohjelmasta on sekä tekstipohjainen että graafinen käyttöliittymä

- Tekstipohjainen versio sisältää kaikki vaatimusmäärittelyn mukaiset toiminnot.

- Graafinen käyttöliittymä on vielä kehitysvaiheessa ja tarjoaa vain osittaiset ominaisuudet.

- Tekstikäyttöliittymässä pelaaja voi omalla vuorollaan valita ehdotetun pelaajan, tai hakea nimellä muuta pelaajaa. Graafisessa käyttöliittymässä on tällä hetkellä vain mahdollisuus valita ehdotetuista vaihtoehdoista.

- Graafinen käyttöliittymä ei näytä varaustilaisuuden päätyttyä omaa kokoonpanoa, mutta ominaisuus löytyy tekstipohjaisesta versiosta.

## Dokumentaatio:

[Changelog](https://github.com/eepek/drafthelper/blob/main/drafthelper-app/dokumentaatio/changelog.md)

[Vaatimusmäärittely](https://github.com/eepek/drafthelper/blob/main/drafthelper-app/dokumentaatio/vaatimusmaarittely.md)

[Tuntikirjanpito](https://github.com/eepek/drafthelper/blob/main/drafthelper-app/dokumentaatio/tuntikirjanpito.md)

[Arkkitehtuurikuvaus](https://github.com/eepek/drafthelper/blob/main/drafthelper-app/dokumentaatio/arkkitehtuuri.md)

[Release](https://github.com/eepek/drafthelper/releases/tag/viikko5)

## Ohjelman asennus, käyttö ja testaus

Kaikki seuraavat komennot tulee suorittaa drafthelper-app kansiossa

### Asennus ja suoritus:

Asenna riippuvuudet komennolla:

```bash
poetry install
```

Suorita ohjelma graafisessa käyttöliittymässä komennolla:

```bash
poetry run invoke start
```

Ohjelman voi suorittaa myös tekstikäyttöliittymällä kommennolla:

```bash
poetry run invoke start-txt
```

### Testikomennot

Testit ajetaan komennolla:


```bash
poetry run invoke test
```

Coverage raportti html muodossa muodostetaan komennolla (raportti löytyy _htmlcov_ hakemistosta):


```bash
poetry run invoke coverage-report
```

Pylint tarkistuksen voi ajaa kommennolla:

```bash
poetry run invoke lint
```


