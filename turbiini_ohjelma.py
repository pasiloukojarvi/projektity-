import time
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 


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
      print("Anna kuukausi ja vuosi muodossa kk/vuosi. Esim. 1/23")
      self.kk_vuosi = str(input("Minkä kuukauden tietoja olet antamassa?(kk/vuosi): "))    
    def kysy_sahko(self):
      self.sahko = int(input("Anna kuukauden sähköntuotanto(MWh):"))
    def kysy_lampo(self):  
      self.lampo = int(input("Anna kuukauden lämmöntuotanto(MWh):"))
    def kysy_energia(self):  
      self.syotettu_energia = int(input("Anna turbiinille syötetty energiamäärä(MWh):"))  
    def kirjauksen_ajankohta(self):
      self.kirjaus_aika = time.strftime("%X %x")
          
# Ohjelmaan antaa hälytykset huoltotarpeesta.
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
      #current_time = time.gmtime() 
      #current_year = current_time.tm_year
      current_year = 2022
      # Summataan sarakkeen "sähköntuotto" tiedot jokaiselta vuodelta erikseen.
      if current_year == 2022:
        summa = df.loc[df.index[0:11], "sähköntuotto"].sum() + self.sahko  
        self.sahko_vuodessa = summa
      elif current_year == 2023:       
        summa = df.loc[12:23, "sähköntuotto"].sum() + self.sahko  
        self.sahko_vuodessa = summa            
      elif current_year == 2024:
        summa = df.loc[24:35, "sähköntuotto"].sum() + self.sahko  
        self.sahko_vuodessa = summa
      elif current_year == 2025:       
        summa = df.loc[36:47, "sähköntuotto"].sum() + self.sahko  
        self.sahko_vuodessa = summa
      elif current_year == 2026:       
        summa = df.loc[48:59, "sähköntuotto"].sum() + self.sahko  
        self.sahko_vuodessa = summa            
      elif current_year == 2027:
        summa = df.loc[60:71, "sähköntuotto"].sum() + self.sahko  
        self.sahko_vuodessa = summa
      elif current_year == 2028:       
        summa = df.loc[72:83, "sähköntuotto"].sum() + self.sahko  
        self.sahko_vuodessa = summa
      elif current_year == 2029:       
        summa = df.loc[84:95, "sähköntuotto"].sum() + self.sahko  
        self.sahko_vuodessa = summa
      elif current_year == 2030:       
        summa = df.loc[96:107, "sähköntuotto"].sum() + self.sahko  
        self.sahko_vuodessa = summa            
      elif current_year == 2031:
        summa = df.loc[108:119, "sähköntuotto"].sum() + self.sahko  
        self.sahko_vuodessa = summa
      elif current_year == 2032:       
        summa = df.loc[120:131, "sähköntuotto"].sum() + self.sahko  
        self.sahko_vuodessa = summa 

    def lampovuodessa(self):
      df = pd.read_csv("kayttotiedot.csv")
      #current_time = time.gmtime() 
      #current_year = current_time.tm_year
      current_year = 2022
      # Summataan sarakkeen "lämmöntuotto" tiedot jokaiselta vuodelta erikseen.
      if current_year == 2022:
        summa = df.loc[0:11, "lämmöntuotto"].sum() + self.lampo   
        self.lampo_vuodessa = summa
      elif current_year == 2023:       
        summa = df.loc[12:23, "lämmöntuotto"].sum() + self.lampo  
        self.lampo_vuodessa = summa            
      elif current_year == 2024:
        summa = df.loc[24:35, "lämmöntuotto"].sum() + self.lampo  
        self.lampo_vuodessa = summa
      elif current_year == 2025:       
        summa = df.loc[36:47, "lämmöntuotto"].sum() + self.lampo  
        self.lampo_vuodessa = summa
      elif current_year == 2026:       
        summa = df.loc[48:59, "lämmöntuotto"].sum() + self.lampo  
        self.lampo_vuodessa = summa            
      elif current_year == 2027:
        summa = df.loc[60:71, "lämmöntuotto"].sum() + self.lampo  
        self.lampo_vuodessa = summa
      elif current_year == 2028:       
        summa = df.loc[72:83, "lämmöntuotto"].sum() + self.lampo  
        self.lampo_vuodessa = summa
      elif current_year == 2029:       
        summa = df.loc[84:95, "lämmöntuotto"].sum() + self.lampo  
        self.lampo_vuodessa = summa
      elif current_year == 2030:       
        summa = df.loc[96:107, "lämmöntuotto"].sum() + self.lampo  
        self.lampo_vuodessa = summa            
      elif current_year == 2031:
        summa = df.loc[108:119, "lämmöntuotto"].sum() + self.lampo  
        self.lampo_vuodessa = summa
      elif current_year == 2032:       
        summa = df.loc[120:131, "lämmöntuotto"].sum() + self.lampo  
        self.lampo_vuodessa = summa  

    def energiavuodessa(self):
      df = pd.read_csv("kayttotiedot.csv")
      current_time = time.gmtime() 
      #current_year = current_time.tm_year
      current_year = 2022
      # Summataan sarakkeen "syötetty_energia" tiedot jokaiselta vuodelta erikseen.
      if current_year == 2022:
        summa = df.loc[0:11, "syötetty_energia"].sum() + self.syotettu_energia  
        self.lampo_vuodessa = summa
      elif current_year == 2023:       
        summa = df.loc[12:23, "syötetty_energia"].sum() + self.syotettu_energia  
        self.lampo_vuodessa = summa            
      elif current_year == 2024:
        summa = df.loc[24:35, "syötetty_energia"].sum() + self.syotettu_energia  
        self.lampo_vuodessa = summa
      elif current_year == 2025:       
        summa = df.loc[36:47, "syötetty_energia"].sum() + self.syotettu_energia  
        self.lampo_vuodessa = summa
      elif current_year == 2026:       
        summa = df.loc[48:59, "syötetty_energia"].sum() + self.syotettu_energia  
        self.lampo_vuodessa = summa            
      elif current_year == 2027:
        summa = df.loc[60:71, "syötetty_energia"].sum() + self.syotettu_energia  
        self.lampo_vuodessa = summa
      elif current_year == 2028:       
        summa = df.loc[72:83, "syötetty_energia"].sum() + self.syotettu_energia  
        self.lampo_vuodessa = summa
      elif current_year == 2029:       
        summa = df.loc[84:95, "syötetty_energia"].sum() + self.syotettu_energia  
        self.lampo_vuodessa = summa
      elif current_year == 2030:       
        summa = df.loc[96:107, "syötetty_energia"].sum() + self.syotettu_energia  
        self.lampo_vuodessa = summa            
      elif current_year == 2031:
        summa = df.loc[108:119, "syötetty_energia"].sum() + self.syotettu_energia  
        self.lampo_vuodessa = summa
      elif current_year == 2032:       
        summa = df.loc[120:131, "syötetty_energia"].sum() + self.syotettu_energia  
        self.lampo_vuodessa = summa 

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
       

# Tehdään käyttöliittymä ohjelmaan. Testausvaiheen ajaksi salasanan kysyminen
# on kytketty pois päältä.
print("******************************************")
print("MIKROTURBIINIEN HUOLTO- JA TOIMINTAOHJELMA")
print("******************************************")
#while True:
  #salasana = str(input("Anna salasana: "))
  #if salasana == "Turbiini2938":
    #break
  #else:
    #print("Väärä salasana")

lista_huoltotiedot = []
lista_kayttotiedot = [] 
while True:
  print("Mitä haluat tehdä:\n(1)Kirjaa käyttötiedot\n(2)Kirjaa huolto\
  \n(3)Kirjaa korjaus\n(4)Näytä kuvaaja käyttötiedoista\n(5)Lopeta")
  valinta = int(input("Valitse toimenpide: "))
  if valinta == 1: 
# Ohjelma kysyy ja kirjaa käyttötiedot sekä antaa tarvittaessa
# hälytykset luokkien ja olioiden avulla.    
    tiedot = Kuukausittaisetkayttotiedot('', 0, 0, 0, '')
    Kuukausittaisetkayttotiedot.kysy_kk_vuosi(tiedot)
    Kuukausittaisetkayttotiedot.kysy_sahko(tiedot)
    Kuukausittaisetkayttotiedot.kysy_lampo(tiedot)
    Kuukausittaisetkayttotiedot.kysy_energia(tiedot)
    Kuukausittaisetkayttotiedot.kirjauksen_ajankohta(tiedot)
    Kokonaiskayttotiedot.sahkonkertyma(tiedot)#nyt näyttäs toimivan.
    Kokonaiskayttotiedot.lammonkertyma(tiedot)
    Kokonaiskayttotiedot.energian_syotto(tiedot)
    Vuotuisetkayttotiedot.sahkovuodessa(tiedot)
    Vuotuisetkayttotiedot.lampovuodessa(tiedot)
    #Vuotuisetkayttotiedot.energiavuodessa(tiedot) 
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

  elif valinta == 2:
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

  elif valinta == 3:
    pass

# Ohjelma muodostaa käyttötiedoista kuvaajan pandas ja matplotlib
# kirjastojen avulla.
  elif valinta == 4:
    #Ensin tehdään kuvaaja jokaisen kuukauden tiedoista.
    df = pd.read_csv("kayttotiedot.csv")
    x = df['kk/vuosi']
    y1 = df['sähköntuotto'] 
    y2 = df['lämmöntuotto']
    y3 = df['syötetty_energia']
    fig, ax = plt.subplots()
    ax.plot(x, y1, label='Sähköntuotto(MWh)')
    ax.plot(x, y2, label='Lämmöntuotto(MWh)')
    ax.plot(x, y3, label='Syötetty energia(MWh)') 
    plt.title('TURBIININ KÄYTTÖTIEDOT')
    plt.xlabel('Käyttöajankohta(kk/vuosi)')
    plt.ylabel('MWh')
    ax.legend()
    plt.show()
    #Toiseksi tehdään kuvaaja koko turbiinin käyttöiän kumulatiivisistä arvoista. 
    df = pd.read_csv("kayttotiedot.csv")
    x = df['kk/vuosi']
    y1 = df['sähkö_yhteensä'] 
    y2 = df['lämpö_yhteensä']
    y3 = df['energia_yhteensä']
    fig, ax = plt.subplots()
    ax.plot(x, y1, label='Sähköntuoton kertymä(MWh)')
    ax.plot(x, y2, label='Lämmöntuoton kertymä(MWh)')
    ax.plot(x, y3, label='Syötetyn energian kertymä(MWh)') 
    plt.title('TURBIININ KÄYTTÖTIETOJEN KERTYMÄ')
    plt.xlabel('Käyttöajankohta(kk/vuosi)')
    plt.ylabel('MWh')
    ax.legend()
    plt.show()
    #Kolmanneksi tehdään kuvaajat eri vuosien kumulatiivisistä tiedoista. Tämä vielä teon alla.
    while True:
      print("Minkä vuoden tietojen kertymästä haluat kuvaajan?")
      vuosi_valinta = int(input("Anna vuosi(2022-2032),0 lopettaa kuvaajien tarkastelun: "))
      if vuosi_valinta == 2022:
        df = pd.read_csv("kayttotiedot.csv")
        x = df.loc[df.index[0:12], 'kk/vuosi']
        y1 = df.loc[df.index[0:12], 'sähkö_vuodessa'] 
        y2 = df.loc[df.index[0:12], 'lämpö_vuodessa']
        y3 = df.loc[df.index[0:12], 'energia_vuodessa']
        fig, ax = plt.subplots()
        ax.plot(x, y1, label='Sähköntuoton 2022 kertymä(MWh)')
        ax.plot(x, y2, label='Lämmöntuoton 2022 kertymä(MWh)')
        ax.plot(x, y3, label='Syötetyn energian 2022 kertymä(MWh)') 
        plt.title('TURBIININ ENERGIANTUOTON KERTYMÄ 2022')
        plt.xlabel('Käyttöajankohta(kk/vuosi)')
        plt.ylabel('MWh')
        ax.legend()
        plt.show() 
      elif vuosi_valinta == 0:
        break
      else:
        print("Väärä valinta. Ilmoita uusi numero.")               

  elif valinta == 5:
    print("Ohjelma suljetaan")
    break 

  else:
    print("Ilmoitit väärän valinnan.")                               