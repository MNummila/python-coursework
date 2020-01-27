# CT60A0201 Ohjelmoinnin perusteet 2017 ohjelmien otsikkotiedot.
# Tekijä: Mikko Nummila
# Opiskelijanumero: 0506303
# Päivämäärä:
# Yhteistyö ja lähteet, nimi ja yhteistyön muoto:
# HUOM! KAIKKI KURSSIN TEHTÄVÄT OVAT HENKILÖKOHTAISIA!
######################################################################
import sys
####################################
#####     LUONNOS VERSIO    ########
####################################
class taxi():
    lähtöaika = 0
    nimi = ''

def tiedostonluku(lista):
    lista.clear()
    laskuri = 0
    tiedosto = input('Anna ensimmäinen matkadataa sisältävän tiedoston nimi: ')
    nimi = input('Anna datalle kuvaava nimi: ')
    try:
        tiedosto1 = open(tiedosto,'r',encoding='utf-8')
    except:
        print('Virhe lopetetaan')
        sys.exit(0)
    while True:
        rivi = tiedosto1.readline()[:-1]
        if rivi == '':
            break
        else:
            laskuri = laskuri + 1
            auto = taxi()
            tietueet = rivi.split(',')
            tietue = tietueet[1][11:13]
            if tietue.isalnum() == True:
                auto.lähtöaika = tietue
            else:
                continue
            auto.nimi = nimi
            lista.append(auto)
    print('Tiedostosta luettu, rivejä',laskuri)
    tiedosto1.close()
    return lista

def lisäätiedosto(lista):
    laskuri = 0
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
            laskuri = laskuri + 1
            auto = taxi()
            tietueet = rivi.split(',')
            tietue = tietueet[1][11:13]
            if tietue.isalnum()==True:
                auto.lähtöaika = tietue
            else:
                continue
            auto.nimi = nimi
            lista.append(auto)
    print('Tiedostosta luettu, rivejä', laskuri)
    tiedosto1.close()
    return lista

def kirjoitatiedosto(lista):
    tiedosto = input('Anna kirjoitettavan frekvenssi CSV-tiedoston nimi: ')
    try:
        tiedosto1 = open(tiedosto,'w',encoding='utf-8')
    except:
        print('Virhe lopetetaan.')
        sys.exit(0)
    for i in lista:

        print('kirjoita')

def piirrä():
    print('piirrä')

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

def testi(lista):
    #laskuri = 0
    for i in lista:
     #   laskuri = laskuri + 1
        print(i.nimi)



def paaohjelma():
    taksilista = []
    while True:
        valinta=valikko()
        if valinta == 0:
            break
        elif valinta == 1:
            tiedostonluku(taksilista)
        elif valinta == 2:
            lisäätiedosto(taksilista)
        elif valinta == 3:
            kirjoitatiedosto(taksilista)
        elif valinta == 4:
            piirrä()
        elif valinta == 9:
            testi(taksilista)
        else:
            print('Väärä syöte.')

paaohjelma()
######################################################################
# eof