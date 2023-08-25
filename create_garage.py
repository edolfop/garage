import sqlite3
import random
import DBG

# Ejemplo de uso
DBG.create_table()

# Lista de nombres de ejemplo
Brand_pool = ['Toyota', 'Seat', 'Mercedes', 'Fiat', 'Citroen']

Name_pool = ['Juan', 'Maria', 'Jose', 'Nieves', 'Roberto' , 'Claudia','Alberto','Jose']

Lastname_pool = ['Perez', 'Gonzalez', 'Pinal', 'Morgade', 'Losada' , 'Rodriguez','Garcia','Blanco']

ABC_pool = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','V','W','X','Y','Z']

# Agregar 40 coches de ejemplo
for i in range(40):
    Brand = random.choice(Brand_pool)
    Name = random.choice(Name_pool)
    Lastname = random.choice(Lastname_pool)
    Anno = random.randint(1990, 2023)
    Letters_plate = random.sample(ABC_pool, 3)
    Letter = ''.join(Letters_plate)
    Number_plate = random.randint(1000 , 9999)
    plate = Letter + '-' + str(Number_plate)
    phone_num = random.randint(600000000 , 699999999)
    DBG.add_vehicle(str(Brand), f'Model{i}', Anno, plate, str(Name), Lastname, f'Address{i}', phone_num)

print("Todos los vehículos:")
print(DBG.get_all_vehicles())
