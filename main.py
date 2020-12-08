from random import randint
from Pitanja import broj_pitanja
from tacanodg import broj_todg
from netacanodg1 import broj_nodg1
from netacanodg2 import broj_nodg2
# importujem pitanja i odgovore

print("Pritisni Enter da baciš kockicu")

ptnj = ""
odg = ""
x = input()
i = 0
j = 0
z = 0
jedan = dva = tri = cetiri = False
van_kuce = [jedan, dva, tri, cetiri]
pozicija = [1, 11, 21, 31]
ime_igraca = ""


while True:

    kockica = randint(1, 6)
    # bacanje kockice

    if i % 4 == 0:
        ime_igraca = "Prvi"
    elif i % 4 == 1:
        ime_igraca = "Drugi"
    elif i % 4 == 2:
        ime_igraca = "Treći"
    else:
        ime_igraca = "Četvrti"
    print(ime_igraca + " igrač je dobio broj " + str(kockica))
    # Da kompjuter za koji igrač igra

    if van_kuce[i % 4]:
        print(broj_pitanja[i])
        print(broj_todg[i])
        print(broj_nodg1[i])
        print(broj_nodg2[i])

        print("Tačan odgovor je: ")
        odg = input()
        if odg == "A":
            pozicija[i % 4] = pozicija[i % 4] + kockica
            print(ime_igraca + " se pomera " + str(kockica) + " koraka")
            print(ime_igraca + " se pomera na poziciju " + str(pozicija[i % 4]))
            # Za one koji su izašli iz kućice
        else:
            print(ime_igraca + " nije odgovorio tačno na pitanje")
            print(ime_igraca + " ostaje na poziciji " + str(pozicija[i % 4]))

    if kockica == 6:
        van_kuce[i % 4] = True
    # Da komjuter zna ko je izašao iz kućice

    if not van_kuce[i % 4]:
        print(ime_igraca + " ostaje u kućici")
    # Da napiše da ko nije dobio 6 ostaje u kućici

    if kockica == 6:
        i = i - 1
    # Da onaj koji je dobio 6 igra opet
    if pozicija[0] > 40:
        print("Prvi je pobedio")
        break
    if pozicija[1] > 50:
        print("Drugi je pobedio")
        break
    if pozicija[2] > 60:
        print("Treci je pobedio")
        break
    if pozicija[3] > 70:
        print("Četvrti je pobedio")
        break
    i = i + 1

    x = input()
