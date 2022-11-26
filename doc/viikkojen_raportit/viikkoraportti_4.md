# Viikkoraportti 4

## Tehtyjä asioita

* suunnittelua
* määrittelin testien onnistumiskriteerit tarkemmin. suunnitellut visualisointia tekstimuodossa sekä isommille kartoille bitmap-kuvina. suunnitellut tietorakenteita. harkitsin jos käyttäisi tietorakenteena graafia jolloin myös muut kuin 2-ulotteiset sokkelot olisivat mahdollisia. luultavasti kuitenkin pitäydyn tämän projektin puitteissa mahdollisimman yksinkertaisessa ja tehokkaassa ( sekä laskennallisesti että muistin käytön suhteen ) tietorakenteessa. myös tehokkaassa tietorakenteessa on kaksi mahdollisuutta esittää seiniä - joko jokaisessa solussa määritelty kaikki 4 viereistä seinää jolloin seinät määritellään aina kahdesti kun vieressä on toinen solu. tai sitten jokaisessa solussa määritellään yksi vaakasuora ja pystysuora seinä, jolloin tarvitaan yksi ylimääräinen vaaka- ja pystyrivi. jonkinlainen tehokkuusero näissä luultavasti on. kumpaa tapaa käytän on vieläkin kahden vaiheilla, eli luultavasti kahden seinän rakennetta koska siinä ei samaa tietoa tarvitse päivittää kahteen eri sijaintiin. mahdollisesti teen yhden toteutuksen molemmilla vertailun vuoksi.

## Miten ohjelma on edistynyt

* puoliksi valmis

## Mitä opin

* tietorakenteista

## Mahdollisia epäselvyyksiä, vaikeuksia

* ei mainittavia.

## Mitä seuraavaksi

tänään lauantaina 26.11.2022 en ole lisännyt vielä mitään koodia viime viikosta mutta huomenna sunnuntaina olisi tarkoitus lähes koko päivä koodata yksi generaattori ja yksi pathfinder-algoritmi valmiiksi.

roadmap loppuprojektille: 
1. sunnuntai
    1.  yksi generointi algoritmi valmiiksi. (dfs)
    2. yksi pathfinder algoritmi valmiiksi. (A-Star)
    3. unittestaus ja performance testaus toimimaan näiden kanssa.
1. pari generointi ja pathfinder algoritmia lisää.
1. testit uusille algoritmeille.
1. visualisointi bitmap-kuvien avulla isoille kartoille.
1. ( lisää uusia algoritmeja, hybriditoteutuksia ja edistyneempiä ominaisuuksia resurssien (aika) mukaan. )

