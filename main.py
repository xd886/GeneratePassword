import random


caracteres = "!@#$%^&*()_+-=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


longitud = int(input("Introduce la longitud de la contraseña: "))

contraseña = ""


for _ in range(longitud):
    contraseña += random.choice(caracteres)


print("Tu contraseña generada es:", contraseña)
