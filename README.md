# projektityo
TYÖN LÄHTÖKOHDAT:
Mikroturbiinien huolto ohjelma: peinteinen ohjelmointityö, ei sisällä koneoppimista.
Tämä projekti työ käsittelee mikroturbiinilaitoksen huoltoa, korjausta ja kustannusten laskentaa. Siinä käytetään pandas kirjastoa tiedon tallentamisessa, mathplotlip kirjastoa tiedon visualisointiin ja time kirjastoa tietojen annon ajankohdan muodostamiseen. Lisäksi käytetään itse tehtyä kuvaajat kirjastoa, jonka avulla pääohjelma tekee kaikki kuvaajat.
TYÖN TAVOITTEET:
Työn tavoitteena on lisätä sähkön- ja lämmöntuotannon taloudellista kannattavuutta. Tämä tapahtuu optimoimalla turbiinin eri komponettien huoltovälit. Pyritään vähentämään turbiinien korjaustarvetta ja lisäämään niiden käyttöikää. Oikein ajoitetuilla ja kohdistetuilla huolloilla varmistetaan myös polttoaineen käytölle mahdollisimman suuri hyöty eli käytännössä  sähkön- ja lämmöntuotannon hyötysuhde pidetään mahdollisimman korkeana.
OHJELMAN TOIMINTA:
Turbiinin käyttötiedot tallennetaan CSV-tiedostoon. Tiedoista muodostetaan kuvaaja. Käyttötietojen perusteella annetaan tarvittaessa hälytykset, jotka muistuttavat huoltotarpeesta. Ohjelma laskee huoltovälit eri komponenteille. Ongelmakohtia jotka ohjelma erityisesti huomioi ovat: lämmönsiirrin, kompressori, laakerit, polttoaineen syöttöputkistot. Lisäksi ohjelma tallentaa käyttäjän antamat huoltotiedot omaan CSV-tiedostoon. 