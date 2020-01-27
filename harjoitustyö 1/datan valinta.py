# 20171023 HT1DatanValinta.py un
####################################################################

tdsto = open("Tieliikenne 5.0.csv", "r")
tdsto2 = open("OPHTData2.csv", "w")
rivi = tdsto.readline()
tdsto2.write(rivi)
for rivi in tdsto:
    if (rivi[0:2] == "M1"): # henkilÃ¶auto
        tietueet = rivi.split(";")
        if (tietueet[1] != ""): # tarkistus puuttuvan datan varalta
            kayttoonottovuosi = int(tietueet[1][0:4])
        else:
            kayttoonottovuosi = 0
        if (tietueet[33] != ""):  # tarkistus puuttuvan datan varalta
            CO2 = int(tietueet[33])
        else:
            CO2 = -1
        if ((CO2 > -1) and (2010 <= kayttoonottovuosi <= 2010)):
            tdsto2.write(rivi)
tdsto.close()
tdsto2.close()

####################################################################
# eof