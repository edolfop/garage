import sqlite3

def create_table():
    conn = sqlite3.connect('garage.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vehicles (
            id INTEGER PRIMARY KEY,
            brand TEXT,
            model TEXT,
            year INTEGER,
            plate_number TEXT,
            owner_first_name TEXT,
            owner_last_name TEXT,
            owner_address TEXT,
            owner_phone TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_vehicle(brand, model, year, plate_number, owner_first_name, owner_last_name, owner_address, owner_phone):
    conn = sqlite3.connect('garage.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO vehicles (brand, model, year, plate_number, owner_first_name, owner_last_name, owner_address, owner_phone)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (brand, model, year, plate_number, owner_first_name, owner_last_name, owner_address, owner_phone))
    conn.commit()
    conn.close()

def get_all_vehicles():
    conn = sqlite3.connect('garage.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM vehicles')
    vehicles = cursor.fetchall()
    conn.close()
    return vehicles

def get_vehicle_by_id(vehicle_id):
    conn = sqlite3.connect('garage.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM vehicles WHERE id = ?', (vehicle_id,))
    vehicle = cursor.fetchone()
    conn.close()
    return vehicle

def get_vehicle_by_brand(brand):
    conn = sqlite3.connect('garage.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM vehicles WHERE brand = ?', (brand,))
    vehicles = cursor.fetchall()
    conn.close()
    return vehicles

def get_vehicle_by_model(model):
    conn = sqlite3.connect('garage.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM vehicles WHERE model = ?', (model,))
    vehicles = cursor.fetchall()
    conn.close()
    return vehicles

def get_vehicle_by_year(year):
    conn = sqlite3.connect('garage.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM vehicles WHERE year = ?', (year,))
    vehicles = cursor.fetchall()
    conn.close()
    return vehicles

def get_vehicle_by_plate_number(plate_number):
    conn = sqlite3.connect('garage.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM vehicles WHERE plate_number = ?', (plate_number,))
    vehicles = cursor.fetchall()
    conn.close()
    return vehicles

def get_vehicle_by_owner_first_name(owner_first_name):
    conn = sqlite3.connect('garage.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM vehicles WHERE owner_first_name = ?', (owner_first_name,))
    vehicles = cursor.fetchall()
    conn.close()
    return vehicles

def get_vehicle_by_owner_last_name(owner_last_name):
    conn = sqlite3.connect('garage.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM vehicles WHERE owner_last_name = ?', (owner_last_name,))
    vehicles = cursor.fetchall()
    conn.close()
    return vehicles

def get_vehicle_by_owner_address(owner_address):
    conn = sqlite3.connect('garage.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM vehicles WHERE owner_address = ?', (owner_address,))
    vehicles = cursor.fetchall()
    conn.close()
    return vehicles

def get_vehicle_by_owner_phone(owner_phone):
    conn = sqlite3.connect('garage.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM vehicles WHERE owner_phone = ?', (owner_phone,))
    vehicles = cursor.fetchall()
    conn.close()
    return vehicles

