import sqlite3
conexion = sqlite3.connect('basedatos.db')
conexion.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        dni INTEGER PRIMARY KEY,
        nombre TEXT,
        apellido TEXT,
        telefono TEXT
    )
''')
dni = input("Ingrese el DNI: ")
nombre = input("Ingrese el nombre: ")
apellido=input("Ingrese el apellido: ")
telefono= input("Ingrese el teléfono: ")
conexion.execute('INSERT INTO usuarios (dni, nombre, apellido, telefono) VALUES (?, ?, ?, ?)', (dni, nombre, apellido, telefono))
conexion.commit()
conexion.close()