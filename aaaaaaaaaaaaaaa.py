# Nr1
sarasas = ["Labas", "Lietuva", 5, 4, 7, 16, 29, "Vakaras"]
print(sarasas)
sarasas.append(69)
print(sarasas)
sarasas.pop(4)
print(sarasas)
sarasas[1] = "Italija"
print(sarasas)
sarasas2 = [1, 5, 9, 2, 16, 3, 4]
sarasas2.sort()
print(sarasas2)

# Nr2
listas = []

while True:
    digit = int(input("Iveskite kita skaiciu: "))
    if digit > 0:
        listas.append(digit)
    else:
        break
    print(sum(listas))

# Nr3

