# Demanem un número per teclat
num = int(input("Introdueix un número sencer: "))

# Comprovem si és parell o senar
if num % 2 == 0:
    tipus = "parell"
else:
    tipus = "senar"

# Comprovem si és positiu, negatiu o zero
if num > 0:
    signe = "positiu"
elif num < 0:
    signe = "negatiu"
else:
    signe = "zero"

# Mostrem el resultat
print(f"El número {num} és {tipus} i {signe}")
