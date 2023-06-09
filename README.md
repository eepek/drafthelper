# Draft Helper

Draft helper on ohjelma, jonka tarkoitus on auttaa käyttäjää harjoittelemaan ja kokeilemaan erilaisia skenaarioita NFL:n fantasia liigan varaustilaisuutta varten. Ohjelma mahdollistaa 6-12 joukkueen liigojen varaustilaisuuden mallinnuksen. Valittavana on useita kokoonpano vaihtoehtoja, sekä yleisimmät pisteytyformaatit (PPR, Half-PPR ja Standard). Käyttäjän tueksi ohjelmisto tarjoaa [Fantasy Pros](https://www.fantasypros.com) sivuston useamman asiantuntijan arvioista koostaman konsensus arvion kolme parasta pelaajaa, jokaisella käyttäjän varausvuorolla. Käyttäjä voi myös valita muun pelaajan kirjoittamalla pelaajan nimen. Muitten varausvuorolla, ohjelmisto valitsee kyseisen vuoron joukkueeseen pelaajan konsensulistan kärkiviisikosta.

Ohjelma on Helsingin Yliopiston Tietojenkäsittelytieteen Ohjelmistotekniikan kurssin harjoitustyö.

## Dokumentaatio:

[Changelog](https://github.com/eepek/drafthelper/blob/main/drafthelper-app/dokumentaatio/changelog.md)

[Vaatimusmäärittely](https://github.com/eepek/drafthelper/blob/main/drafthelper-app/dokumentaatio/vaatimusmaarittely.md)

[Tuntikirjanpito](https://github.com/eepek/drafthelper/blob/main/drafthelper-app/dokumentaatio/tuntikirjanpito.md)

[Arkkitehtuurikuvaus](https://github.com/eepek/drafthelper/blob/main/drafthelper-app/dokumentaatio/arkkitehtuuri.md)

[Käyttöohje](https://github.com/eepek/drafthelper/blob/main/drafthelper-app/dokumentaatio/kayttoohje.md)

[Testausdokumentti](https://github.com/eepek/drafthelper/blob/main/drafthelper-app/dokumentaatio/testaus.md)

[Release 25.4](https://github.com/eepek/drafthelper/releases/tag/viikko5)

[Release 2.5](https://github.com/eepek/drafthelper/releases/tag/Viikko6)

[Release 14.5](https://github.com/eepek/drafthelper/releases/tag/loppupalautus)

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


