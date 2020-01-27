# CT60A0201 Ohjelmoinnin perusteet 2017 ohjelmien otsikkotiedot.
# Tekijä: Mikko Nummila
# Opiskelijanumero: 0506303
# Päivämäärä: 6.12.2017
# Yhteistyö ja lähteet, nimi ja yhteistyön muoto: -
# HUOM! KAIKKI KURSSIN TEHTÄVÄT OVAT HENKILÖKOHTAISIA!
######################################################################
import sys
import matplotlib.pyplot as plt
import numpy
def tiedostonluku(kirja):
    kirja.clear()
    lista = []
    laskuri = 0
    tiedosto = input('Anna ensimmäinen matkadataa sisältävän tiedoston nimi: ')
    nimi = input('Anna datalle kuvaava nimi: ')
    try:
        tiedosto1 = open(tiedosto, 'r', encoding='utf-8')
    except:
        print('Virhe lopetetaan')
        sys.exit(0)
    while True:
        rivi = tiedosto1.readline()[:-1]
        if rivi == '':
            break
        else:
            tietueet = rivi.split(',')
            tietue = tietueet[1][11:13]
            if tietue.isalnum() == True:
                auto = int(tietue)
                laskuri = laskuri + 1
            else:
                continue

            lista.append(auto)
    kirja[nimi] = lista
    print('Tiedosto luettu, rivejä', laskuri)
    tiedosto1.close()
    return kirja


def lisäätiedosto(kirja):
    laskuri = 0
    lista = []
    tiedosto = input('Anna seuraava matkadataa sisältävän tiedoston nimi: ')
    nimi = input('Anna datalle kuvaava nimi: ')
    try:
        tiedosto1 = open(tiedosto, 'r', encoding='utf-8')
    except:
        print('Virhe lopetetaan')
        sys.exit(0)
    while True:
        rivi = tiedosto1.readline()[:-1]
        if rivi == '':
            break
        else:
            tietueet = rivi.split(',')
            tietue = tietueet[1][11:13]
            if tietue.isalnum() == True:
                auto = int(tietue)
                laskuri = laskuri + 1
            else:
                continue

            lista.append(auto)
    kirja[nimi] = lista
    print('Tiedosto luettu, rivejä', laskuri)
    tiedosto1.close()
    return kirja


def kirjoitatiedosto(kirja):
    kirja2 = kirja.copy()
    try:
        tiedosto = input('Anna kirjoitettavan frekvenssi CSV-tiedoston nimi: ')
        tiedosto1 = open(tiedosto, 'w')
    except:
        print('Virhe lopetetaan.')
        sys.exit(0)
    for avain in kirja:
        määrälista = []
        lista = kirja.get(avain,)
        for o in range(0,24):
            määrä = lista.count(o)
            määrälista.append(määrä)
        kirja2[avain]= määrälista
    for avain2 in kirja2:
        tiedosto1.write(';'+avain2)
        if avain2 == '' or avain2==0:
            tiedosto1.write('\n')
            break
    tiedosto1.write('\n')
    for i in range(0,24):
        tiedosto1.write(str(i))
        for avain3 in kirja2:
            tiedosto1.write(';'+str(kirja2[avain3][i]))
        tiedosto1.write('\n')
    tiedosto1.close()
    return kirja2

def piirrä(kirja):
    leveys = 0.2
    laskuri = 0
    x=[x for x in range(0,24)]
    x2 = numpy.arange(len(x))
    for avain in kirja:
        laskuri = laskuri + 1
        plt.bar(x2+ leveys*laskuri,kirja[avain],label=avain,width=leveys)
    plt.xticks(x2 +leveys*(laskuri/2),x)
    plt.xlabel('Kellonaika')
    plt.ylabel('Matkamäärä')
    plt.title('Matkoja eri kellonaikoina')
    plt.legend()
    plt.show()

def valikko():
    print('Anna haluamasi toiminnon numero seuraavasta valikosta:')
    print('1) Lue ensimmäinen matkadatatiedosto')
    print('2) Lisää matkadatatiedosto')
    print('3) Kirjoita csv')
    print('4) Piirrä kuvaaja')
    print('0) Lopeta')
    try:
        valinta = int(input('Valintasi: '))
    except ValueError:
        print('Väärä syöte, lopetetaan.')
        return 0
    return valinta

def paaohjelma():
    taksikirja = {}
    taksikirja2 = {}
    while True:
        valinta = valikko()
        if valinta == 0:
            break
        elif valinta == 1:
            tiedostonluku(taksikirja)
        elif valinta == 2:
            lisäätiedosto(taksikirja)
        elif valinta == 3:
            taksikirja2 = kirjoitatiedosto(taksikirja)
        elif valinta == 4:
            piirrä(taksikirja2)
        else:
            print('Väärä syöte.')


paaohjelma()
print('Kiitos ohjelman käytöstä.')
######################################################################
# eof