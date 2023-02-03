import matplotlib.pyplot as plt  #Kuvaajien tekemiseen
import pandas as pd  #CSV-tiedostojen lukemiseen.


def kuvaaja1():
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
    plt.title('TURBIININ KÄYTTÖTIEDOT KUUKAUSITTAIN')
    plt.xlabel('Käyttöajankohta(kk/vuosi)')
    plt.ylabel('MWh')
    ax.legend()
    labels = df['kk/vuosi']
    plt.xticks(x, labels, rotation=90)    
    plt.show()


def kuvaaja2():
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
    plt.title('TURBIININ KÄYTTÖTIETOJEN KERTYMÄ KOKO KÄYTTÖAJALTA')
    plt.xlabel('Käyttöajankohta(kk/vuosi)')
    plt.ylabel('MWh')
    ax.legend()
    labels = df['kk/vuosi']
    plt.xticks(x, labels, rotation=90)    
    plt.show()


def kuvaaja3(): 
    while True:
      print("Minkä vuoden tietojen kertymästä haluat kuvaajan?")
      vuosi_valinta = str(input("Anna vuosi(2021-2032),0 lopettaa kuvaajien tarkastelun: "))
      if vuosi_valinta == "2021":
        df = pd.read_csv("kayttotiedot.csv")
        x = df.loc[df.index[0:12], 'kk/vuosi']
        y1 = df.loc[df.index[0:12], 'sähkö_vuodessa'] 
        y2 = df.loc[df.index[0:12], 'lämpö_vuodessa']
        y3 = df.loc[df.index[0:12], 'energia_vuodessa']
        fig, ax = plt.subplots()
        ax.plot(x, y1, label='Sähköntuoton 2021 kertymä(MWh)')
        ax.plot(x, y2, label='Lämmöntuoton 2021 kertymä(MWh)')
        ax.plot(x, y3, label='Syötetyn energian 2021 kertymä(MWh)') 
        plt.title('TURBIININ KÄYTTÖTIETOJEN KERTYMÄ 2021')
        plt.xlabel('Käyttöajankohta(kk/vuosi)')
        plt.ylabel('MWh')
        ax.legend()
        plt.show()

      elif vuosi_valinta == "2022":
        df = pd.read_csv("kayttotiedot.csv")
        x = df.loc[df.index[12:24], 'kk/vuosi']
        y1 = df.loc[df.index[12:24], 'sähkö_vuodessa'] 
        y2 = df.loc[df.index[12:24], 'lämpö_vuodessa']
        y3 = df.loc[df.index[12:24], 'energia_vuodessa']
        fig, ax = plt.subplots()
        ax.plot(x, y1, label='Sähköntuoton 2022 kertymä(MWh)')
        ax.plot(x, y2, label='Lämmöntuoton 2022 kertymä(MWh)')
        ax.plot(x, y3, label='Syötetyn energian 2022 kertymä(MWh)') 
        plt.title('TURBIININ KÄYTTÖTIETOJEN KERTYMÄ 2022')
        plt.xlabel('Käyttöajankohta(kk/vuosi)')
        ax.legend()
        plt.show()

      elif vuosi_valinta == "2023":
        df = pd.read_csv("kayttotiedot.csv")
        x = df.loc[df.index[24:36], 'kk/vuosi']
        y1 = df.loc[df.index[24:36], 'sähkö_vuodessa'] 
        y2 = df.loc[df.index[24:36], 'lämpö_vuodessa']
        y3 = df.loc[df.index[24:36], 'energia_vuodessa']
        fig, ax = plt.subplots()
        ax.plot(x, y1, label='Sähköntuoton 2023 kertymä(MWh)')
        ax.plot(x, y2, label='Lämmöntuoton 2023 kertymä(MWh)')
        ax.plot(x, y3, label='Syötetyn energian 2023 kertymä(MWh)') 
        plt.title('TURBIININ KÄYTTÖTIETOJEN KERTYMÄ 2023')
        plt.xlabel('Käyttöajankohta(kk/vuosi)')
        plt.ylabel('MWh')
        ax.legend()
        plt.show()

      elif vuosi_valinta == "2024":
        df = pd.read_csv("kayttotiedot.csv")
        x = df.loc[df.index[36:48], 'kk/vuosi']
        y1 = df.loc[df.index[36:48], 'sähkö_vuodessa'] 
        y2 = df.loc[df.index[36:48], 'lämpö_vuodessa']
        y3 = df.loc[df.index[36:48], 'energia_vuodessa']
        fig, ax = plt.subplots()
        ax.plot(x, y1, label='Sähköntuoton 2024 kertymä(MWh)')
        ax.plot(x, y2, label='Lämmöntuoton 2024 kertymä(MWh)')
        ax.plot(x, y3, label='Syötetyn energian 2024 kertymä(MWh)') 
        plt.title('TURBIININ KÄYTTÖTIETOJEN KERTYMÄ 2024')
        plt.xlabel('Käyttöajankohta(kk/vuosi)')
        plt.ylabel('MWh')
        ax.legend()
        plt.show() 

      elif vuosi_valinta == "2025":
        df = pd.read_csv("kayttotiedot.csv")
        x = df.loc[df.index[48:60], 'kk/vuosi']
        y1 = df.loc[df.index[48:60], 'sähkö_vuodessa'] 
        y2 = df.loc[df.index[48:60], 'lämpö_vuodessa']
        y3 = df.loc[df.index[48:60], 'energia_vuodessa']
        fig, ax = plt.subplots()
        ax.plot(x, y1, label='Sähköntuoton 2025 kertymä(MWh)')
        ax.plot(x, y2, label='Lämmöntuoton 2025 kertymä(MWh)')
        ax.plot(x, y3, label='Syötetyn energian 2025 kertymä(MWh)') 
        plt.title('TURBIININ KÄYTTÖTIETOJEN KERTYMÄ 2025')
        plt.xlabel('Käyttöajankohta(kk/vuosi)')
        plt.ylabel('MWh')
        ax.legend()
        plt.show()

      elif vuosi_valinta == "2026":
        df = pd.read_csv("kayttotiedot.csv")
        x = df.loc[df.index[60:72], 'kk/vuosi']
        y1 = df.loc[df.index[60:72], 'sähkö_vuodessa'] 
        y2 = df.loc[df.index[60:72], 'lämpö_vuodessa']
        y3 = df.loc[df.index[60:72], 'energia_vuodessa']
        fig, ax = plt.subplots()
        ax.plot(x, y1, label='Sähköntuoton 2026 kertymä(MWh)')
        ax.plot(x, y2, label='Lämmöntuoton 2026 kertymä(MWh)')
        ax.plot(x, y3, label='Syötetyn energian 2026 kertymä(MWh)') 
        plt.title('TURBIININ KÄYTTÖTIETOJEN KERTYMÄ 2026')
        plt.xlabel('Käyttöajankohta(kk/vuosi)')
        plt.ylabel('MWh')
        ax.legend()
        plt.show()

      elif vuosi_valinta == "2027":
        df = pd.read_csv("kayttotiedot.csv")
        x = df.loc[df.index[72:84], 'kk/vuosi']
        y1 = df.loc[df.index[72:84], 'sähkö_vuodessa'] 
        y2 = df.loc[df.index[72:84], 'lämpö_vuodessa']
        y3 = df.loc[df.index[72:84], 'energia_vuodessa']
        fig, ax = plt.subplots()
        ax.plot(x, y1, label='Sähköntuoton 2027 kertymä(MWh)')
        ax.plot(x, y2, label='Lämmöntuoton 2027 kertymä(MWh)')
        ax.plot(x, y3, label='Syötetyn energian 2027 kertymä(MWh)') 
        plt.title('TURBIININ KÄYTTÖTIETOJEN KERTYMÄ 2027')
        plt.xlabel('Käyttöajankohta(kk/vuosi)')
        plt.ylabel('MWh')
        ax.legend()
        plt.show()

      elif vuosi_valinta == "2028":
        df = pd.read_csv("kayttotiedot.csv")
        x = df.loc[df.index[84:96], 'kk/vuosi']
        y1 = df.loc[df.index[84:96], 'sähkö_vuodessa'] 
        y2 = df.loc[df.index[84:96], 'lämpö_vuodessa']
        y3 = df.loc[df.index[84:96], 'energia_vuodessa']
        fig, ax = plt.subplots()
        ax.plot(x, y1, label='Sähköntuoton 2028 kertymä(MWh)')
        ax.plot(x, y2, label='Lämmöntuoton 2028 kertymä(MWh)')
        ax.plot(x, y3, label='Syötetyn energian 2028 kertymä(MWh)') 
        plt.title('TURBIININ KÄYTTÖTIETOJEN KERTYMÄ 2028')
        plt.xlabel('Käyttöajankohta(kk/vuosi)')
        plt.ylabel('MWh')
        ax.legend()
        plt.show()

      elif vuosi_valinta == "2029":
        df = pd.read_csv("kayttotiedot.csv")
        x = df.loc[df.index[96:108], 'kk/vuosi']
        y1 = df.loc[df.index[96:108], 'sähkö_vuodessa'] 
        y2 = df.loc[df.index[96:108], 'lämpö_vuodessa']
        y3 = df.loc[df.index[96:108], 'energia_vuodessa']
        fig, ax = plt.subplots()
        ax.plot(x, y1, label='Sähköntuoton 2029 kertymä(MWh)')
        ax.plot(x, y2, label='Lämmöntuoton 2029 kertymä(MWh)')
        ax.plot(x, y3, label='Syötetyn energian 2029 kertymä(MWh)') 
        plt.title('TURBIININ KÄYTTÖTIETOJEN KERTYMÄ 2029')
        plt.xlabel('Käyttöajankohta(kk/vuosi)')
        plt.ylabel('MWh')
        ax.legend()
        plt.show()

      elif vuosi_valinta == "2030":
        df = pd.read_csv("kayttotiedot.csv")
        x = df.loc[df.index[108:120], 'kk/vuosi']
        y1 = df.loc[df.index[108:120], 'sähkö_vuodessa'] 
        y2 = df.loc[df.index[108:120], 'lämpö_vuodessa']
        y3 = df.loc[df.index[108:120], 'energia_vuodessa']
        fig, ax = plt.subplots()
        ax.plot(x, y1, label='Sähköntuoton 2030 kertymä(MWh)')
        ax.plot(x, y2, label='Lämmöntuoton 2030 kertymä(MWh)')
        ax.plot(x, y3, label='Syötetyn energian 2030 kertymä(MWh)') 
        plt.title('TURBIININ KÄYTTÖTIETOJEN KERTYMÄ 2030')
        plt.xlabel('Käyttöajankohta(kk/vuosi)')
        plt.ylabel('MWh')
        ax.legend()
        plt.show()

      elif vuosi_valinta == "2031":
        df = pd.read_csv("kayttotiedot.csv")
        x = df.loc[df.index[120:132], 'kk/vuosi']
        y1 = df.loc[df.index[120:132], 'sähkö_vuodessa'] 
        y2 = df.loc[df.index[120:132], 'lämpö_vuodessa']
        y3 = df.loc[df.index[120:132], 'energia_vuodessa']
        fig, ax = plt.subplots()
        ax.plot(x, y1, label='Sähköntuoton 2031 kertymä(MWh)')
        ax.plot(x, y2, label='Lämmöntuoton 2031 kertymä(MWh)')
        ax.plot(x, y3, label='Syötetyn energian 2031 kertymä(MWh)') 
        plt.title('TURBIININ KÄYTTÖTIETOJEN KERTYMÄ 2031')
        plt.xlabel('Käyttöajankohta(kk/vuosi)')
        plt.ylabel('MWh')
        ax.legend()
        plt.show()

      elif vuosi_valinta == "2032":
        df = pd.read_csv("kayttotiedot.csv")
        x = df.loc[df.index[132:144], 'kk/vuosi']
        y1 = df.loc[df.index[132:144], 'sähkö_vuodessa'] 
        y2 = df.loc[df.index[132:144], 'lämpö_vuodessa']
        y3 = df.loc[df.index[132:144], 'energia_vuodessa']
        fig, ax = plt.subplots()
        ax.plot(x, y1, label='Sähköntuoton 2032 kertymä(MWh)')
        ax.plot(x, y2, label='Lämmöntuoton 2032 kertymä(MWh)')
        ax.plot(x, y3, label='Syötetyn energian 2032 kertymä(MWh)') 
        plt.title('TURBIININ KÄYTTÖTIETOJEN KERTYMÄ 2032')
        plt.xlabel('Käyttöajankohta(kk/vuosi)')
        plt.ylabel('MWh')
        ax.legend()
        plt.show()            

      elif vuosi_valinta == "0":
        break
      else:
        print("Väärä valinta. Ilmoita uusi numero.")