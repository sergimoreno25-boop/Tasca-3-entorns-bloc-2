import random

# Generar les dades
height = random.randint(100, 210)
age = random.randint(10, 25)
wants_photos = random.choice([True, False])

# Veure les dades generades
print("Valors generats:")
print(f"Alçada: {height} cm")
print(f"Edat: {age} anys")
print(f"Vol fotos: {wants_photos}")

# Seguim les normes segons les el diagrama i les dades
if height > 120:
    print("Pot pujar a l'atracció")
    if age < 12:
        price = 5
    elif age <= 18:
        price = 7
    else:
        price = 12
    if wants_photos:
        price += 3
    print(f"La factura total és ${price}")
else:
    print("No pot pujar a l'atracció")