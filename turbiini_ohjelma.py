import time  #Käytetään nykyisen ajan saamiseen tietojen kirjauksen yhteydessä.
import pandas as pd  #CSV-tiedostojen lukemiseen.
import csv  #CSV-tiedoston vierheellisen käyttötiedon kiinni ottamiseen.
import kuvaajat #Itse tehty moduuli kuvaajien tekoa varten.


def my_join(lista,sep):
  mystr = ''
  for elem in lista[0:-1]:
      mystr += str(elem) + str(sep)
  mystr += str(lista[-1])
  return(mystr)

#Tämä luokka kysyy käyttäjältä tiedot ja antaa hälytykset.
class Kuukausittaisetkayttotiedot:
    def __init__(self, kk_vuosi, sahko, lampo, syotettu_energia, kirjaus_aika):
        self.kk_vuosi = kk_vuosi
        self.sahko = sahko
        self.lampo = lampo
        self.syotettu_energia = syotettu_energia
        self.kirjaus_aika = kirjaus_aika

#Ohjelma kysyy turbiinin käyttötiedot.        
    def kysy_kk_vuosi(self):
      while True:
       print("Anna kuukausi ja vuosi muodossa kk/vuosi. Esim. 1/23")
       self.kk_vuosi = str(input("Minkä kuukauden tietoja olet antamassa?(kk/vuosi): "))
       with open("kayttotiedot.csv", "r") as file:
         lukija = csv.reader(file)
         for rivi in lukija:
          viimeinen_rivi = rivi
       if self.kk_vuosi == viimeinen_rivi[0][:4]:
        print("Virhe: Annoit saman kuukauden ja vuoden kuin viimeksikin!")
       else:
        break    
    def kysy_sahko(self):
      self.sahko = int(input("Anna kuukauden sähköntuotanto(MWh):"))
    def kysy_lampo(self):  
      self.lampo = int(input("Anna kuukauden lämmöntuotanto(MWh):"))
    def kysy_energia(self):  
      self.syotettu_energia = int(input("Anna turbiinille syötetty energiamäärä(MWh):"))  
    def kirjauksen_ajankohta(self):
      self.kirjaus_aika = time.strftime("%X %x")
          
# Ohjelma antaa hälytykset huoltotarpeesta.
# Turbiinien lämpö tulee sähköntuoton sivutuotteena. Kun tiedetään molempien
# optimitilanteen hyötysuhteet, niin voidaan päätellä, että lämmönvaihtimet
# ovat likaantuneet, jos suhteellinen lämmöntuotto laskee liian alas.      
    def halytys1(self):
      if (self.sahko * 1.5) > self.lampo:
        print("----------HÄLYTYS----------")
        print("Mirkoturbiinien suhteellinen lämmöntuotanto on alle ohjearvon.")
        print("Tarkista/huolla lämmönvaihtimet!")
        while True:
          kuittaus1 = int(input("Kuittaa hälytys syöttämällä 1: "))
          if kuittaus1 == 1:
            break

# Toisessa hälytysmallissa sähköntuottoa verrataan syötettyyn energiamäärään.
# Jos suhteellinen sähköntuotto laskee alle optimitason, niin tarkastetaan
# sähköntuottoon oleellisimmin vaikuttavat komponentit.     
    def halytys2(self):
      if self.syotettu_energia > (self.sahko * 3):
        print("----------HÄLYTYS----------")
        print("Mikroturbiinien suhteellinen sähköntuotto on alle ohjearvon.")
        print("Tarkista/huolla kompressori, laakerit ja polttoaineen syöttöputkistot!")
        while True:
          kuittaus2 = int(input("Kuittaa hälytys syöttämällä 2: "))
          if kuittaus2 == 2:
            break

# Kolmannessa hälytysmallissa annetaan muistutus Määräaikaishuollon tarpeesta.
# Määräaikaishuollot ajoitetaan kesäkuulle, koska lämmön- ja sähköntarveon silloin pienimmillään.           
    def halytys3(self):
      if self.kk_vuosi[0] == "6":
        print("----------HÄLYTYS----------")
        print("Suorita mikroturbiinien vuosittainen määräaikaishuolto.")
        while True:
          kuittaus3 = int(input("Kuittaa hälytys syöttämällä 3: "))
          if kuittaus3 == 3:
            break      
            
# Tämä luokka laskee kunkin vuoden kumulatiivisen kertymän kuukausittaisten
# käytötietojen perusteella. Tämä luokka vielä testausvaiheessa.                
class Vuotuisetkayttotiedot(Kuukausittaisetkayttotiedot):
    def __init__(self, kk_vuosi, sahko, lampo, syotettu_energia, kirjaus_aika, sahko_vuodessa, lampo_vuodessa, energia_vuodessa):
        super().__init__(kk_vuosi, sahko, lampo, syotettu_energia, kirjaus_aika)
        self.sahko_vuodessa = sahko_vuodessa
        self.lampo_vuodessa = lampo_vuodessa
        self.energia_vuodessa = energia_vuodessa

    def sahkovuodessa(self):
      df = pd.read_csv("kayttotiedot.csv")
      current_time = time.gmtime() 
      current_year = current_time.tm_year
      # Summataan sarakkeen "sähköntuotto" tiedot jokaiselta vuodelta erikseen.
      if current_year == 2021:
        summa = df.loc[df.index[0:11], "sähköntuotto"].sum() + self.sahko  
        self.sahko_vuodessa = summa
      elif current_year == 2022:       
        summa = df.loc[12:23, "sähköntuotto"].sum() + self.sahko  
        self.sahko_vuodessa = summa            
      elif current_year == 2023:
        summa = df.loc[24:35, "sähköntuotto"].sum() + self.sahko  
        self.sahko_vuodessa = summa
      elif current_year == 2024:       
        summa = df.loc[36:47, "sähköntuotto"].sum() + self.sahko  
        self.sahko_vuodessa = summa
      elif current_year == 2025:       
        summa = df.loc[48:59, "sähköntuotto"].sum() + self.sahko  
        self.sahko_vuodessa = summa            
      elif current_year == 2026:
        summa = df.loc[60:71, "sähköntuotto"].sum() + self.sahko  
        self.sahko_vuodessa = summa
      elif current_year == 2027:       
        summa = df.loc[72:83, "sähköntuotto"].sum() + self.sahko  
        self.sahko_vuodessa = summa
      elif current_year == 2028:       
        summa = df.loc[84:95, "sähköntuotto"].sum() + self.sahko  
        self.sahko_vuodessa = summa
      elif current_year == 2029:       
        summa = df.loc[96:107, "sähköntuotto"].sum() + self.sahko  
        self.sahko_vuodessa = summa            
      elif current_year == 2030:
        summa = df.loc[108:119, "sähköntuotto"].sum() + self.sahko  
        self.sahko_vuodessa = summa
      elif current_year == 2031:       
        summa = df.loc[120:131, "sähköntuotto"].sum() + self.sahko  
        self.sahko_vuodessa = summa 
      elif current_year == 2032:       
        summa = df.loc[132:143, "sähköntuotto"].sum() + self.sahko  
        self.sahko_vuodessa = summa      

    def lampovuodessa(self):
      df = pd.read_csv("kayttotiedot.csv")
      current_time = time.gmtime() 
      current_year = current_time.tm_year
      # Summataan sarakkeen "lämmöntuotto" tiedot jokaiselta vuodelta erikseen.
      if current_year == 2021:
        summa = df.loc[0:11, "lämmöntuotto"].sum() + self.lampo   
        self.lampo_vuodessa = summa
      elif current_year == 2022:       
        summa = df.loc[12:23, "lämmöntuotto"].sum() + self.lampo  
        self.lampo_vuodessa = summa            
      elif current_year == 2023:
        summa = df.loc[24:35, "lämmöntuotto"].sum() + self.lampo  
        self.lampo_vuodessa = summa
      elif current_year == 2024:       
        summa = df.loc[36:47, "lämmöntuotto"].sum() + self.lampo  
        self.lampo_vuodessa = summa
      elif current_year == 2025:       
        summa = df.loc[48:59, "lämmöntuotto"].sum() + self.lampo  
        self.lampo_vuodessa = summa            
      elif current_year == 2026:
        summa = df.loc[60:71, "lämmöntuotto"].sum() + self.lampo  
        self.lampo_vuodessa = summa
      elif current_year == 2027:       
        summa = df.loc[72:83, "lämmöntuotto"].sum() + self.lampo  
        self.lampo_vuodessa = summa
      elif current_year == 2028:       
        summa = df.loc[84:95, "lämmöntuotto"].sum() + self.lampo  
        self.lampo_vuodessa = summa
      elif current_year == 2029:       
        summa = df.loc[96:107, "lämmöntuotto"].sum() + self.lampo  
        self.lampo_vuodessa = summa            
      elif current_year == 2030:
        summa = df.loc[108:119, "lämmöntuotto"].sum() + self.lampo  
        self.lampo_vuodessa = summa
      elif current_year == 2031:       
        summa = df.loc[120:131, "lämmöntuotto"].sum() + self.lampo  
        self.lampo_vuodessa = summa 
      elif current_year == 2032:       
        summa = df.loc[132:143, "lämmöntuotto"].sum() + self.lampo  
        self.lampo_vuodessa = summa         

    def energiavuodessa(self):
      df = pd.read_csv("kayttotiedot.csv")
      current_time = time.gmtime() 
      current_year = current_time.tm_year
      # Summataan sarakkeen "syötetty_energia" tiedot jokaiselta vuodelta erikseen.
      if current_year == 2021:
        summa = df.loc[0:11, "syötetty_energia"].sum() + self.syotettu_energia  
        self.energia_vuodessa = summa
      elif current_year == 2022:       
        summa = df.loc[12:23, "syötetty_energia"].sum() + self.syotettu_energia  
        self.energia_vuodessa = summa            
      elif current_year == 2023:
        summa = df.loc[24:35, "syötetty_energia"].sum() + self.syotettu_energia  
        self.energia_vuodessa = summa
      elif current_year == 2024:       
        summa = df.loc[36:47, "syötetty_energia"].sum() + self.syotettu_energia  
        self.energia_vuodessa = summa
      elif current_year == 2025:       
        summa = df.loc[48:59, "syötetty_energia"].sum() + self.syotettu_energia  
        self.energia_vuodessa = summa            
      elif current_year == 2026:
        summa = df.loc[60:71, "syötetty_energia"].sum() + self.syotettu_energia  
        self.energia_vuodessa = summa
      elif current_year == 2027:       
        summa = df.loc[72:83, "syötetty_energia"].sum() + self.syotettu_energia  
        self.energia_vuodessa = summa
      elif current_year == 2028:       
        summa = df.loc[84:95, "syötetty_energia"].sum() + self.syotettu_energia  
        self.energia_vuodessa = summa
      elif current_year == 2029:       
        summa = df.loc[96:107, "syötetty_energia"].sum() + self.syotettu_energia  
        self.energia_vuodessa = summa            
      elif current_year == 2030:
        summa = df.loc[108:119, "syötetty_energia"].sum() + self.syotettu_energia  
        self.energia_vuodessa = summa
      elif current_year == 2031:       
        summa = df.loc[120:131, "syötetty_energia"].sum() + self.syotettu_energia  
        self.energia_vuodessa = summa
      elif current_year == 2032:   
        summa = df.loc[132:143, "syötetty_energia"].sum() + self.syotettu_energia  
        self.energia_vuodessa = summa        

# Tämä luokka laskee jokaiselle kuulle käyttötietojen kertymän koko
# turbiinin käyttöiän ajalta.                              
class Kokonaiskayttotiedot(Kuukausittaisetkayttotiedot):
    def __init__(self, kk_vuosi, sahko, lampo, syotettu_energia, kirjaus_aika, sahko_yhteensa, lampo_yhteensa, energia_yhteensa):
        super().__init__(kk_vuosi, sahko, lampo, syotettu_energia, kirjaus_aika)
        self.sahko_yhteensa = sahko_yhteensa
        self.lampo_yhteensa = lampo_yhteensa
        self.energia_yhteensa = energia_yhteensa


    def sahkonkertyma(self):
      df = pd.read_csv("kayttotiedot.csv")
      # Summataan sarakkeen "sähköntuotto" tiedot. Summan lisätään self.sahko, koska
      # muuten jättää pois laskusta juuri annetun kuukauden tiedot.
      summa = df["sähköntuotto"].sum() + self.sahko
      self.sahko_yhteensa = summa 

    def lammonkertyma(self): 
      df = pd.read_csv("kayttotiedot.csv")
      # Summataan sarakkeen "lämmöntuotto" tiedot
      summa = df["lämmöntuotto"].sum() + self.lampo
      self.lampo_yhteensa = summa 

    def energian_syotto(self):
      df = pd.read_csv("kayttotiedot.csv")
      # Summataan sarakkeen "syötetty_energia" tiedot
      summa = df["syötetty_energia"].sum() + self.syotettu_energia
      self.energia_yhteensa = summa  

class Huollon_kirjaus:
    def __init__(self, tekija, yritys, komponentti, ajankohta):
        self.tekija = tekija
        self.yritys = yritys
        self.komponetti = komponentti
        self.ajankohta = ajankohta 
    def kysy_tekija(self):
      self.tekija = str(input("Anna huollon tekijän nimi: ")) 
    def kysy_yritys(self):
      self.yritys = str(input("Anna yrityksen nimi: ")) 
    def huollon_kohde(self):
      self.komponetti = str(input("Mikä/mitkä komponetit huollettiin?: ")) 
    def huollon_ajankohta(self):
      self.ajankohta = time.strftime("%x")        
       

# Tehdään käyttöliittymä ohjelmaan. 
print("******************************************")
print("MIKROTURBIINIEN HUOLTO- JA TOIMINTAOHJELMA")
print("******************************************")
while True:
  salasana = str(input("Anna salasana: "))
  if salasana == "Turbiini2938":
    break
  else:
    print("Väärä salasana")

lista_huoltotiedot = []
lista_kayttotiedot = [] 
while True:
  print("Mitä haluat tehdä:\n(1)Kirjaa käyttötiedot\n(2)Kirjaa huolto\
  \n(3)Näytä kuvaaja käyttötiedoista\n(0)Lopeta")
  valinta = str(input("Valitse toimenpide: "))
  if valinta == "1": 
# Ohjelma kysyy ja kirjaa käyttötiedot sekä antaa tarvittaessa
# hälytykset luokkien ja olioiden avulla.    
    tiedot = Kuukausittaisetkayttotiedot('', 0, 0, 0, '')
    Kuukausittaisetkayttotiedot.kysy_kk_vuosi(tiedot)
    Kuukausittaisetkayttotiedot.kysy_sahko(tiedot)
    Kuukausittaisetkayttotiedot.kysy_lampo(tiedot)
    Kuukausittaisetkayttotiedot.kysy_energia(tiedot)
    Kuukausittaisetkayttotiedot.kirjauksen_ajankohta(tiedot)
    Kokonaiskayttotiedot.sahkonkertyma(tiedot)
    Kokonaiskayttotiedot.lammonkertyma(tiedot)
    Kokonaiskayttotiedot.energian_syotto(tiedot)
    Vuotuisetkayttotiedot.sahkovuodessa(tiedot)
    Vuotuisetkayttotiedot.lampovuodessa(tiedot)
    Vuotuisetkayttotiedot.energiavuodessa(tiedot) 
    tiedot.halytys1()
    tiedot.halytys2()
    tiedot.halytys3()
    lista_kayttotiedot.append(tiedot)
    kahva = open("kayttotiedot.csv", "a")
    for tieto in lista_kayttotiedot:
      lista = []
      for nimi, arvot in tieto.__dict__.items():
        lista.append(arvot)
      line = my_join(lista,',') + '\n'
      kahva.write(line)
    kahva.close()
    lista_kayttotiedot.pop()     

  elif valinta == "2":
    huollot = Huollon_kirjaus('', '', '', '')
    Huollon_kirjaus.kysy_tekija(huollot)
    Huollon_kirjaus.kysy_yritys(huollot)
    Huollon_kirjaus.huollon_kohde(huollot)
    Huollon_kirjaus.huollon_ajankohta(huollot)
    lista_huoltotiedot.append(huollot)
    kahva = open("huoltotiedot.csv", "a")
    for tieto in lista_huoltotiedot:
      lista = []
      for nimi, arvot in tieto.__dict__.items():
        lista.append(arvot)
      line = my_join(lista,',') + '\n'
      kahva.write(line)
    kahva.close()
    lista_huoltotiedot.pop()

# Ohjelma muodostaa käyttötiedoista kuvaajan pandas ja matplotlib
# kirjastojen avulla. Kuvaajien teko on aputiedostossa.
  elif valinta == "3":
    # Kuvaaja1 näyttää koko käyttöajan kuukausi kohtaiset tiedot.
        kuvaajat.kuvaaja1()
    # Kuvaaja2 näyttää koko käyttöajan kertymän.    
        kuvaajat.kuvaaja2()
    # Kuvaaja3 näyttää halutun vuoden käyttötietojen kertymän.    
        kuvaajat.kuvaaja3()
               

  elif valinta == "0":
    print("****************************************************")
    print("SULJETAAN MIKROTURBIINIEN HUOLTO- JA TOIMINTAOHJELMA")
    print("****************************************************")
    break 

  else:
    print("Ilmoitit väärän valinnan.")                               