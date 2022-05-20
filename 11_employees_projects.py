# ukol-11: Zaměstnanci a Projekty
# Zaměstnanci
# Uvažuj, že zpracováváš analýzu pro softwarovou firmu. Firma má kanceláře v Praze, Plzni a Liberci. Seznam zaměstnanců pro jednotlivé kanceláře najdeš v souborech zam_praha.csv, zam_plzeň.csv a zam_liberec.csv.

import requests

emp_praha = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/zam_praha.csv")
open("zam_praha.csv", "wb").write(emp_praha.content)

emp_plzen = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/zam_plzeň.csv")
open("zam_plzeň.csv", "wb").write(emp_plzen.content)

emp_liberec = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/zam_liberec.csv")
open("zam_liberec.csv", "wb").write(emp_liberec.content)

platy = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/platy_2021_02.csv")
open("platy_2021_02.csv", "wb").write(platy.content)


# Načti data o zaměstnancích z CSV souborů do tabulek (DataFrame). Ke každé tabulce přidej nový sloupec mesto, které bude obsahovat informaci o tom, ve kterém městě zaměstnanec pracuje.
import pandas
emp_praha = pandas.read_csv('zam_praha.csv')
emp_plzen = pandas.read_csv('zam_plzeň.csv')
emp_liberec = pandas.read_csv('zam_liberec.csv')

emp_praha['city'] = 'Praha'
emp_plzen['city'] = 'Plzeň'
emp_liberec['city'] = 'Liberec'
#print(emp_praha)

# Vytvoř novou tabulku zamestnanci a ulož do ní informace o všech zaměstnancích.
employees = pandas.concat([emp_praha, emp_plzen, emp_liberec], ignore_index=True)
#print(employees)

# Ze souboru platy_2021_02.csv načti platy zaměstnanců za únor 2021. Propoj tabulku (operace join) s platy a tabulku se zaměstnanci pomocí sloupce cislo_zamestnance.
payment_feb = pandas.read_csv('platy_2021_02.csv')
#print(payment_feb)
employees_payment = pandas.merge(employees, payment_feb)
#print(employees_payment)

# Porovnej rozměry tabulek před spojením a po spojení. Pokud nemá některý zaměstnanec plat za únor, znamená to, že v naší firmě již nepracuje.
print(employees.shape)
print(employees_payment.shape)
# Spočti průměrný plat zaměstnanců v jednotlivých kancelářích.
print(employees_payment.groupby('city')['plat'].mean())

# Dobrovolný doplněk
# Ulož do proměnné počet zaměstnaců, kteří v naší firmě již nepracují.
employees_payment_2 = pandas.merge(employees, payment_feb, how="outer")
#print(employees_payment_2)

# V rámci úspory se IT oddělení rozhodlo prověřit licence přidělené zaměstnancům, kteří ve firmě již nepracují. Vytvoř samostatnou tabulku, která obsahuje jména zaměstnanců, kteří ve firmě již nepracují. Tabulku ulož do souboru CSV.
ex_employees = employees_payment_2[employees_payment_2['plat'].isnull()]
#print(ex_employees)
ex_employees.to_csv('byvali_zamestnanci.csv')

# Projekty
# Pokračuj ve své práci pro softwarovou firmu. Ze souboru vykazy.csv načti informace o výkazech na projekty pro jednoho vybraného zákazníka.


vykazy = requests.get("https://raw.githubusercontent.com/lutydlitatova/python-jaro-2022/main/ukoly/data/vykazy.csv")
open("vykazy.csv", "wb").write(vykazy.content)
# Načti data ze souboru a ulož je do tabulky.
vykazy = pandas.read_csv('vykazy.csv')
#print(vykazy)

# Proveď agregaci a zjisti celkový počet vykázaných hodin za jednotlivé projekty.
print(vykazy.groupby('project')['hours'].sum())

# Dobrovolný doplněk

# Propoj tabulku s výkazy s tabulkou se zaměstnanci, kterou jsi vytvořil(a) v předchozím cvičení.
vykazy.rename(columns={'emloyee_id':'cislo_zamestnance'}, inplace=True)
#print(vykazy)
employees_projects = pandas.merge(employees_payment, vykazy)
#print(employees_projects)

# Následně proveď statistiku vykázaných hodin za jednotlivé kanceláře, tj. spočítej celkový počet hodin vykázaný zaměstnanci jednotlivých kanceláří na projekty daného zákazníka.
print(employees_projects.groupby(['city','project'])['hours'].sum())
