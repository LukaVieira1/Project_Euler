lista = []

for numero in range(1, 1000):  # Loop for numbers from 1 to 1000
    if ((numero % 3) == 0) or ((numero % 5) == 0):  # Take the number and check if it is multiple of 3 or 5
        lista.append(numero)  # Put that number on the list


print(f"A soma é {sum(lista)}")  # Prints the sum of these numbers




