# ukol-12: Vizualizace
# Histogram platů

# Načti si data do tabulky a vytvoř histogram. Nastav vhodně hranice skupin histogramu (parametr bins), aby byl graf přehledný a snadno interpretovatelný.
import requests
import matplotlib.pyplot as plt
import pandas as pd
import datetime


platy = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/platy_2021_02.csv")
open("platy_2021_02.csv", "wb").write(platy.content)

platy = pd.read_csv('/Users/user/Desktop/programovani/platy_2021_02.csv')

# platy.hist(['plat'], bins=[30000, 35000,40000, 45000, 50000, 55000, 60000])

# Dobrovolný doplněk
# Vyzkoušej si vytvořit podgrafy. pandas a matplotlib to umí poměrně jednoduše a to pomocí parametru by metody hist(). Jako parametr vlož sloupec, podle kterého chceš data do podgrafů rozdělit. Musíš vložit sloupec ve formě dat, nikoli pouze jeho název.

# Vytvoř pro zadaná data podgrafy pro jednotlivá města. Načti si informace o městě, ve kterém jednotliví pracovníci pracují (to jsme již dělali v minulém úkolu). Následně sloupec mesto použij na rozdělení podgrafů.

# Teplota ve městech
# Vrať se k práci se souborem temperature.csv, který obsahuje informace o průměrné teplotě v různých městech v listopadu 2017.

teplo = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/temperature.csv")
open("temperature.csv", "wb").write(teplo.content)

temperature = pd.read_csv('/Users/user/Desktop/programovani/temperature.csv')

# Vytvoř tabulku, která bude obsahovat údaje o teplotě za města Helsinki, Miami Beach a Tokyo.
# Vytvoř krabicový graf a porovnej rozsah teplot v těchto městech.

city1 = temperature.loc[temperature["City"] == "Helsinki"]
Helsinki = city1.loc[:,'AvgTemperature']

city2 = temperature.loc[temperature["City"] == "Miami Beach"]
Miami_Beach = city2.loc[:,'AvgTemperature']
city3 = temperature.loc[temperature["City"] == "Tokyo"]
Tokyo = city3.loc[:,'AvgTemperature']

cities = pd.concat([Helsinki,Miami_Beach, Tokyo], axis='columns', ignore_index=True)
cities.to_csv('citiesHelMBTok.csv')
print(cities)
cities.plot(kind='box', whis=[0, 100])





plt.show()