# Demanar un número enter
numero = int(input("Introdueix un número enter: "))

# Comprovar si és múltiple de 5 i 7
if numero % 5 == 0 and numero % 7 == 0:
    print(f"El número {numero} és múltiple de 5 i de 7.")
else:
    print(f"El número {numero} NO és múltiple de 5 i de 7.")