# Määrittelydokumentti

### Yleistä

Opinto-ohjelma: Tietojenkäsittelytieteen kandidaatti

Dokumentaatiossa käytetty kieli: Suomi

### Ohjelmointikieli

Tarkoitus on käyttää Python-kieltä. Optiona
vaihto Julia tai C++ -kieleen jos näyttää siltä että Python on liian hidas.

Myös C, C#, Java ja Javascript ovat tuttuja kieliä.

### Algoritmit ja tietorakenteet

Tason pohjaksi
luodaan aluksi hieman tähän tarkoitukseen 
parhaiten sopivaksi muokattuja Primin, Kruskalin ja muita sokkeloiden generointialgoritmeja ,satunnaisavaimesta riippuen vaihdellen, käyttäen kartta jossa on alku ja loppupiste. 

Sen jälkeen satunnaisuutta avuksi käyttäen etsitään n määrä hieman erilaisia reittejä joita
pitkin pääsee alkupisteestä loppupisteeseen. Erilaisuus 
reitille tulee jo siitä että odottaa jossain pisteessä x,y
z sekuntia ja tietenkin erilaisista satunnaisista
tilassa kulkevista reittivaihtoehdoista. Reittien määrä riippuu siitä kuinka helppo tai vaikea halutaan tason olevan. 

Käytetään vaihdellen erilaisia tunnettuja sokkelonratkaisualgoritmeja [2] ja niistä tähän tarkoitukseen muokattuja versioita.

Kun reitit on kartoitettu lisätään karttaan viholliset,
liikuteltavat kivet ja muu sisältö. Vihollisten 
ja muiden esineiden määrä on myös riippuvainen
tasosta. Aina kun yritetään
lisätä uusi vihollinen tai muu sisältö ajetaan kaikki 
toimivat reitit läpi ja varmistetaan ettei vihollinen 
osu pelaajaan tämän kulkemalla reitillä. Jos tulee osuma hylätään lisäys kyseiseen kohtaan, merkataan tämä paikka
huonoksi ja yritetään satunnaisesti
jonnekin muualle kunnes kaikki halutut sisällöt on lisätty
tai tehtävässä on epäonnistuttu jolloin yritetään alusta 
kasvattamalla satunnaislukugeneraattorin avainta yhdellä ja jatketaan näin x kertaa kunnes joko onnistutaan löytämään
sopiva kartta tai luovutaan tehtävästä mahdottomana.

### Syöte ja tuloste

Algoritmi saa syötteenä satunnaisgeneraattorille annettavan 
luvun, tason leveyden ja korkeuden ja vaikeustason joka tasolla halutaan olevan. 

Algoritmi palauttaa generoidun luolaston omana luokkarakenteenaan jossa useampia kaksiulotteisia taulukoita sisältäen 
seiniä, ovia, avaimia, vihollisia, kiviä, mahdollisesti muita esineitä ja
alku ja loppupisteet.

## Aika ja tilavaativuudet

Tilavaatimus on luokkaa O(n) luvun n ollessa 
vaikeustasosta käänteisesti riippuva mahdollisten reittien
määrä. Eli esimerkikis helpoimmalla tasolla 0 halutaan 
että mahdollisia reittijä on runsaasti kun taas tasolla 100
reittien määrä voi olla hyvin pieni.

Aikavaatimus on luokkaa O(k^n) luvun n ollessa vaikeustasosta käänteisestä riippuva mahdollisten reittien
määrä ja k tasoon lisättävien vihollisten ja objektien 
määrä jotka on testattava aina jokaisen reitin suhteen alusta loppuun. 

### Lähteet

[1] Sokkelon generointialgoritmit https://en.wikipedia.org/wiki/Maze_generation_algorithm

[2] Sokkelonratkaisualgoritmit https://en.wikipedia.org/wiki/Maze-solving_algorithm

[3] Dandy Atari 8-bit https://www.youtube.com/watch?v=pT8grHJweO4

[4] Boulder Dash C64 https://www.youtube.com/watch?v=FiEVfa1OK_o&t=128s


