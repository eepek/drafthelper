# Draft Helper

Draft helper on ohjelma, jonka tarkoitus on auttaa käyttäjää harjoittelemaan ja kokeilemaan erilaisia skenaarioita NFL:n fantasia liigan varaustilaisuutta varten. Ohjelma mahdollistaa 6-14 joukkueen Full-PPR liigojen varaustilaisuuden mallinnuksen. Käyttäjän tueksi ohjelmisto tarjoaa Fantasy Pros sivuston useamman asiantuntijan arvioista koostaman konsensus arvion kolme parasta pelaajaa, jokaisella käyttäjän varausvuorolla. Käyttäjä voi myös valita muun pelaajan kirjoittamalla pelaajan nimen. Muitten varausvuorolla, ohjelmisto valitsee kyseisen vuoron joukkueeseen pelaajan konsensulistan kärkiviisikosta.

Ohjelma on Helsingin Yliopiston Tietojenkäsittelytieteen Ohjelmistotekniikan kurssin harjoitustyö.

### Ensimmäisen version toiminnallisuudet 4.4.2023
- Ohjelma toimii tekstipohjaisessa käyttöliittymässä. Graafinen käyttöliittymä toteutetaan myöhemmin.

- Bottipelaajat osaavat valita satunnaisen pelaajan omalla varausvuorollaan.

- Pelaaja voi omalla vuorollaan valita ehdotetun pelaajan, tai hakea nimellä muuta pelaajaa.

### Dokumentaatio:

[Changelog](https://github.com/eepek/drafthelper/blob/main/drafthelper-app/dokumentaatio/changelog.md)

[Vaatimusmäärittely](https://github.com/eepek/drafthelper/blob/main/drafthelper-app/dokumentaatio/vaatimusmaarittely.md)

[Tuntikirjanpito](https://github.com/eepek/drafthelper/blob/main/drafthelper-app/dokumentaatio/tuntikirjanpito.md)

### Asennus ja suoritus:

Asenna riippuvuudet komennolla:

```bash
poetry install
```

Suorita ohjelma:

```bash
poetry run invoke start
```

Testit ajetaan komennolla:


```bash
poetry run invoke test
```

Coverage raportti html muodossa muodostetaan komennolla (raportti löytyy _htmlcov_ hakemistosta):


```bash
poetry run invoke coverage-report
```
