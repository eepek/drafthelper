
# Vaatimusmäärittely    
    
## Sovelluksen tarkoitus

DrafHelper on apuväline NFL fantasy liigan varaustapahtumaan. Ohjelma tarjoaa omalla valintavuorolla FantasyPros sivuston konsensus arvioon perustuen kolme parasta pelaajavaihtoehtoa Full-PPR pistetytyksellä olevaan liigaan. DrafHelper ottaa huomioon jo täytetyt pelipaikat ja tarjoaa vain pelaajia pelipaikoille, jotka ovat täyttämättä. 

## Käyttäjä

Ohjelmassa on vain yksi käyttäjä tyyppi, peruskäyttäjä, joka pystyy säätämään kaikkia tarjolla olevia asetuksia.

## Toiminnallisuudet ensimmäisessä versiossa

### Ohjelman käynnistyttyä

Ohjelma avautuu asetus näkymään, jossa käyttäjä pääsee valitsemaan liigan koon ja oman varausvuoron.

### Varausnäkymä

- Kun ei ole käyttäjän varausvuoro:

  ~~Ohjelma näyttää konsensuslistan 10 korkeimmalle sijoitettua pelaajaa, joita ei ole vielä valittu, sekä hakuruudun.~~
    
  ~~Käyttäjä poistaa valitun pelaajan listalta, joko painamalla valitun pelaajan nimeä, tai hakemalla valitun pelaajan.~~

  * Ohjelma valitsee satunnaisen pelaajan rankinglistan viiden parhaan joukosta simuloiden aitoa varaustilaisuutta.
    
- Käyttäjän varausvuoro:

  * Ohjelma näyttää 3 parhaimmaksi arvioitua pelaajaa, ottaen huomioon käyttäjän jo täytetyt pelipaikat.
    
  * Ohjelma tarjoaa myös hakuruudun, jolloin käyttäjä voi valita kokoonpanoonsa pelaajan, joka ei ole näkyvissä.
    
  * Käyttäjän valitessa pelaajan, pelaaja poistuu konsensuslistalta ja siirtyy käyttäjän kokoonpanoon.
    
### Varaustilaisuuden päätyttyä

Ohjelma näyttää käyttäjälle hänen valitsemansa kokoonapanon.

## Jatkokehitys ideoita

- Käyttäjä voi valita oman liigansa pelipaikat ja pistetytystyypin

- Ohjelma näyttää tarjottujen pelaajien kohdalla:

  * Viime vuonna tehdyt aktuaalit fantasy pisteet
  
  * Edellisvuoden aktuaalin varausnumeron (ADP) ja konsensuarvion eron (ECR)
  
  * Pelaajan kuvan ja joukkueen logon
