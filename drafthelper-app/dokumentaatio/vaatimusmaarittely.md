
# Vaatimusmäärittely

## Sovelluksen tarkoitus

DrafHelper on apuväline NFL fantasy liigan varaustapahtuman harjoitteluun. Ohjelma tarjoaa omalla valintavuorolla FantasyPros sivuston konsensus arvioon perustuen kolme parasta pelaajavaihtoehtoa. Käyttäjä pääsee valitsemaan haluamansa pisteytysformaatin (PPR, Half-PPR, Standard) sekä pelipaikkakohtaiset pelaajamäärät. DrafHelper ottaa huomioon jo täytetyt pelipaikat ja tarjoaa vain pelaajia pelipaikoille, jotka ovat täyttämättä.

## Käyttäjä

Ohjelmassa on vain yksi käyttäjä tyyppi, peruskäyttäjä, joka pystyy säätämään kaikkia tarjolla olevia asetuksia.

## Toiminnallisuudet

### Ohjelman käyttöliittymät

Ohjelma on käytettävissä joko englanninkielisen graafisen- tai suomenkielisen tekstikäyttöliittymän kautta. Tekstikäyttöliittymä toimii oletus pisteytyksellä (PPR) ja oletus kokoonpanolla (QB, RB, RB, WR, WR, WR, TE, K, DS).

### Ohjelman käynnistyttyä

Ohjelman avauduttua käyttäjän on valittava joukkueensa nimi (ei txt-versiossa), joukkueiden määrä sekä oma varausnumeronsa.
Graafisessa käyttöliittymässä käyttäjä pääseee myös options valikon kautta valitsemaan haluamansa pisteytyksen ja pelipaikkakohtaisest pelaajamäärät.

### Varausnäkymä

- Simuloiden varausvuoron kohdalla

  * Ohjelma valitsee satunnaisen pelaajan kunkin simulaatio joukkueen kokoonpanoon rankinglistan viiden parhaan joukosta mallintaen aitoa varaustilaisuutta.

- Käyttäjän ollessa varausvuorossa:

  * Ohjelma näyttää 3 parhaimmaksi arvioitua pelaajaa, ottaen huomioon käyttäjän jo täytetyt pelipaikat.

  * Ohjelma tarjoaa hakuruudun, jolloin käyttäjä voi valita kokoonpanoonsa pelaajan, joka ei ole näkyvissä.

  * Pelaaja lisätään käyttäjän joukkueen kokoonpanoon

### Varaustilaisuuden päätyttyä

- Ohjelma näyttää kaikkien joukkueiden kokoonpanot
- Tarjolla on mahdollisuus tallentaa varaustilaisuuden joukkueiden kokoonpanot tekstitiedostoon
- Tallennettu tekstitiedosto on mahdollista avata suoraan ohjelmasta nappia painamalla

## Jatkokehitys ideoita

- Ohjelma näyttää tarjottujen pelaajien kohdalla:

  * Viime vuonna tehdyt aktuaalit fantasy pisteet

  * Edellisvuoden aktuaalin varausnumeron (ADP) ja konsensuarvion eron (ECR)

  * Pelaajan kuvan ja joukkueen logon

- Oman ranking tiedoston tuominen ohjelman perusdataksi

- Simuloidut "persoonat", jotka painottavat erilaisia varaustyylejä

- Txt tiedoston sijasta, luodaan HTML-tiedosto, joka antaa paremman graafisen kuvan varaustilaisuuden lopputuloksesta
