import sqlite3 

Conexion = sqlite3.connect('consulta.db')

#creo un cursor para almacenar la información en memoria
Cursor = Conexion.cursor() 

#consulta
Cursor.execute("""
    CREATE TABLE IF NOT EXISTS consulta (
    nro_ley INTEGER PRIMARY KEY,
    palabra_clave TEXT )""")

#creando una lista de tuplas con la información que quiero mostrar en los campos creados anteriormente


#inserto los datos en la tabla
#Cursor.executemany("INSERT INTO leyes VALUES(?,?,?,?,?)", Data_Leyes)

Conexion.commit()

Conexion.close()