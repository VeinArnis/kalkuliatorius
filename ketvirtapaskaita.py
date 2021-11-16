def skaiciu_suma(sk1, sk2, sk3):
    return sk1 + sk2 + sk3


print(skaiciu_suma(45, 5, 6))


def saraso_suma(sarasas):
    suma = 0
    for skaicius in sarasas:
        suma += skaicius
    return suma


sarasas = [4, 5, 78, 8]
print(saraso_suma(sarasas))


def didziausias_skaicius(*args):
    return max(args)


print(didziausias_skaicius(5, 8, 789, 94, 78))


def stringas_atbulai(stringas):
    return stringas[::-1]


print(stringas_atbulai("Donatas Noreika"))


def info_apie_sakini(stringas):
    print(f"Šiame sakinyje yra {len(stringas.split())} žodžių")
    didziosios = 0
    mazosios = 0
    skaiciai = 0
    for simbolis in stringas:
        if simbolis.isupper():
            didziosios += 1
        if simbolis.islower():
            mazosios += 1
        if simbolis.isnumeric():
            skaiciai += 1
    print(f"Didžiosios: {didziosios}, mažosios: {mazosios}, skaičiai: {skaiciai}")


info_apie_sakini("Laba diena laba diena lab 522")


def unikalus_sarasas(sarasas):
    naujas_sarasas = []
    for skaicius in sarasas:
        if skaicius not in naujas_sarasas:
            naujas_sarasas.append(skaicius)
    return naujas_sarasas


print(unikalus_sarasas([4, 5, "Labas", 6, "Labas", True, 5, True, 10]))


def test_prime(i):
    ats = ''
    if i == 1:
        ats = 'Skaicius nera pirminis'
    elif i == 2:
        ats = 'Skaicius pirminis'
    else:
        for x in range(2, i):
            if i % x == 0:
                ats = 'Skaicius nera pirminis'
                break
            else:
                ats = 'skaicius pirminis'
    return ats


print(test_prime(5))


def isrikiuoti_nuo_galo(sakinys):
    zodziai = sakinys.split()[::-1]
    return " # ".join(zodziai)


print(isrikiuoti_nuo_galo("Vienas du trys keturi"))

import calendar


def ar_keliamieji(metai):
    return calendar.isleap(metai)


print(ar_keliamieji(2020))
print(ar_keliamieji(2100))
print(ar_keliamieji(2000))

import datetime


def patikrinti_data(sukaktis):
    ivesta_data = datetime.datetime.strptime(sukaktis, "%Y-%m-%d %X")
    now = datetime.datetime.now()
    skirtumas = now - ivesta_data

    print("Praėjo metų: ", skirtumas.days // 365)
    print("Praėjo mėnesių: ", skirtumas.days / 365 * 12)
    print("Praėjo savaičių: ", skirtumas.days // 7)
    print("Praėjo dienų: ", skirtumas.days)
    print("Praėjo valandų: ", skirtumas.total_seconds() / 3600)
    print("Praėjo minučių: ", skirtumas.total_seconds() / 60)
    print("Praėjo sekundžių: ", skirtumas.total_seconds())


patikrinti_data("2000-01-01 12:12:12")
patikrinti_data("1991-03-11 12:12:12")
