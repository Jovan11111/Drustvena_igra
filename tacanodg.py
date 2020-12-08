import mysql.connector
broj_todg = []

mata_veza = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Dirigent02!",
    database="pitanja"
)
ist_veza = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Dirigent02!",
    database="pitanja"
)
muz_veza = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Dirigent02!",
    database="pitanja"
)
sport_veza = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Dirigent02!",
    database="pitanja"
)
opsta_veza = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Dirigent02!",
    database="pitanja"
)

mata_baza = mata_veza.cursor()
mata = "SELECT todg FROM pitanja_iz_matematike"
mata_baza.execute(mata)

ist_baza = ist_veza.cursor()
ist = "SELECT todg FROM pitanja_iz_istorije"
ist_baza.execute(ist)

muz_baza = muz_veza.cursor()
muz = "SELECT todg FROM pitanja_iz_muzike"
muz_baza.execute(muz)

sport_baza = sport_veza.cursor()
sport = "SELECT todg FROM pitanja_iz_sporta"
sport_baza.execute(sport)

opsta_baza = opsta_veza.cursor()
opsta = "SELECT todg FROM pitanja_iz_opste"
opsta_baza.execute(opsta)

while True:
    mata_pitanje = mata_baza.fetchone()
    ist_pitanje = ist_baza.fetchone()
    muz_pitanje = muz_baza.fetchone()
    sport_pitanje = sport_baza.fetchone()
    opsta_pitanje = opsta_baza.fetchone()
    if mata_pitanje is None:
        break
    broj_todg.append(mata_pitanje)
    broj_todg.append(ist_pitanje)
    broj_todg.append(muz_pitanje)
    broj_todg.append(sport_pitanje)
    broj_todg.append(opsta_pitanje)

