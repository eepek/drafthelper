# Changelog

## Viikko 3
- Consensusranking luokka lataa csv tiedostosta pelaajien tiedot pandas dataframeksi
- Interface luokassa käyttäjä pääsee määrittelemään liigansa koon ja oman draft vuoronsa
- Oman vuoron toiminnallisuutta tehty, mahdollista ottaa ehdotettu pelaaja, tai hakea nimellä
- Toisen varausvuorolla arvotaan automaattisesti joku top-5 pelaajista bottikokoonpanoon
- Roster luokka luotu pitämään kirjaa valituista pelaajista

## Viikko 4
- Ohjelma tarjoaa vain pelaajia, joiden pelipaikkoja ei ole täytetty
- Botin valintaa painotettu kohti viiden parhaan kärkipäätä

## Viikko 5
- Graafisen käyttöliittymän ensimmäinen versio
    - Draft tapahtuma toimii osittain graafisessa versiossa, mutta kaikki tekstikäyttöliittymän ominaisuudet eivät vielä käytössä
- Muutettu luokkien toimintaa graafisessa käyttöliittymässä
    - Eriytetty käyttöliittymää ja sovelluslogiikka. Interface luokka hoitaa pääasiallisen käyttöliittymä toiminnan.

## Viikko 6
- Graafista käyttöliittymää jatkokehitetty ja lisätty suurimmaksi osaksi samat toiminnallisuudet kuin tekstikäyttöliittymässä
    - Draft tapahtuma toimii, mutta pelaaja ei pysty vielä hakemaan nimellä

## Viikko 7
- Pelaajan pystyy hakemaan myös nimellä sekä graafisessa että tekstikäyttöliittymässä
- Käyttäjä voi valita oman liigansa pisteytysformaatin (vaikuttaa pelaajien suositusjärjestykseen) ja pelipaikkakohtaiset pelaajamäärät yleisimmistä vaihtoehdoista File valikosta löytyvästä ikkunasta.
- Varaustapahtuman jälkeen, tulokset voi tallentaa tekstitiedostoon, jonka voi avata ohjelmasta nappia painamalla
- Lisätty värit erottamaan eri pelipaikat varattujen pelaajien joukosta
