import time
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np 


#lista_kayttotiedot = []

def my_join(lista,sep):
  mystr = ''
  for elem in lista[0:-1]:
      mystr += str(elem) + str(sep)
  mystr += str(lista[-1])
  return(mystr)

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
    def sahkonkertyma(self):
      #lista_sahko = []
      #lista_sahko.append(self.sahko)
      #print(lista_sahko)#ainoastaan uusin merkintä tulee listalle, korjaaa!!!!
      df = pd.read_csv("kayttotiedot.csv")
      # Summataan sarakkeen "sähköntuotto" tiedot
      summa = df["sähköntuotto"].sum()
      self.sahko_yhteensa = summa
      #self.sahko_yhteensa = sum(lista_sahko)      
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
# Määräaikaishuollot ajoitetaan kesäkuulle, koska lämmön- ja sähköntarve
# on silloin pienimmillään.           
    def halytys3(self):
      if self.kk_vuosi[0] == "6":
        print("----------HÄLYTYS----------")
        print("Suorita mikroturbiinien vuosittainen määräaikaishuolto.")
        while True:
          kuittaus3 = int(input("Kuittaa hälytys syöttämällä 3: "))
          if kuittaus3 == 3:
            break      
            
                

# Muodosta kuvaaja vuotuisista tiedoista
class Vuotuisetkayttotiedot(Kuukausittaisetkayttotiedot):
    def __init__(self, sahko, lampo, ajo_aika, sahkontuotanto, lammontuotanto, vuoden_kayttoaika):
        super().__init__(sahko, lampo, ajo_aika)
        self.sahkontuotanto = sahkontuotanto
        self.lammontuotanto = lammontuotanto
        self.vuoden_kayttoaika = vuoden_kayttoaika
            


class Kokonaiskayttotiedot(Kuukausittaisetkayttotiedot):
    def __init__(self, kk_vuosi, sahko, lampo, syotettu_energia, kirjaus_aika, sahko_yhteensa, lampo_yhteensa, energia_yhteensa):
        super().__init__(kk_vuosi, sahko, lampo, syotettu_energia, kirjaus_aika)
        self.sahko_yhteensa = sahko_yhteensa
        self.lampo_yhteensa = lampo_yhteensa
        self.energia_yhteensa = energia_yhteensa
    def sahkonkertyma(self):
      lista_sahko = []
      lista_sahko.append(self.sahko)
      self.sahko_yhteensa = sum(lista_sahko)
              
        
       

# Tehdään käyttöliittymä ohjelmaan.
print("******************************************")
print("MIKROTURBIINIEN HUOLTO- JA TOIMINTAOHJELMA")
print("******************************************")
#while True:
  #salasana = str(input("Anna salasana: "))
  #if salasana == "Turbiini2938":
    #break
  #else:
    #print("Väärä salasana")


lista_kayttotiedot = [] 
while True:
  print("Mitä haluat tehdä:\n(1)Kirjaa käyttötiedot\n(2)Kirjaa huolto\
  \n(3)Kirjaa korjaus\n(4)Näytä kuvaaja käyttötiedoista\n(5)Lopeta")
  valinta = int(input("Valitse toimenpide: "))
  if valinta == 1: #rivit 44-59 tähän??
# Ohjelma kysyy ja kirjaa käyttötiedot sekä antaa tarvittaessa
# hälytykset luokkien ja olioiden avulla.    
    tiedot = Kuukausittaisetkayttotiedot('', 0, 0, 0, '')
    Kuukausittaisetkayttotiedot.kysy_kk_vuosi(tiedot)
    Kuukausittaisetkayttotiedot.kysy_sahko(tiedot)
    Kuukausittaisetkayttotiedot.kysy_lampo(tiedot)
    Kuukausittaisetkayttotiedot.kysy_energia(tiedot)
    Kuukausittaisetkayttotiedot.kirjauksen_ajankohta(tiedot)
    Kuukausittaisetkayttotiedot.sahkonkertyma(tiedot)#nyt näyttäs toimivan!
    tiedot.halytys1()
    tiedot.halytys2()
    tiedot.halytys3()
    #tiedot = Kokonaiskayttotiedot('', 0, 0, 0, '', 0, 0, 0)
    #Kokonaiskayttotiedot.sahkonkertyma(tiedot)
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
    #Muodosta hälytykset, käyty if lausetta     

  elif valinta == 2:
    pass

  elif valinta == 3:
    pass

# Ohjelma muodostaa käyttötiedoista kuvaajan pandas ja matplotlib
# kirjastojen avulla.
  elif valinta == 4:
    df = pd.read_csv("kayttotiedot.csv")
    x = df['kk/vuosi']
    y1 = df['sähköntuotto'] 
    y2 = df['lämmöntuotto']
    y3 = df['syötetty_energia']
    fig, ax = plt.subplots()
    ax.plot(x, y1, label='Sähköntuotto(MWh)')
    ax.plot(x, y2, label='Lämmöntuotto(MWh)')
    ax.plot(x, y3, label='Syötetty energia(MWh)')
    #ax.plot(x, y) 
    plt.title('TURBIININ KÄYTTÖTIEDOT')
    plt.xlabel('Käyttöajankohta(kk/vuosi)')
    #plt.ylabel('lämmöntuotto')
    ax.legend()
    plt.show()

  elif valinta == 5:
    print("Ohjelma suljetaan")
    break 

  else:
    print("Ilmoitit väärän valinnan.")                               