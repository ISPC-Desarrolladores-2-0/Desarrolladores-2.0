import sqlite3
from tabulate import tabulate #Es importante tener instalado tabulate (poner en consola: pip install tabulate)
from datetime import datetime

print("\n  BIENVENIDO AL SISTEMA DE CONSULTAS DE LEYES\n")

##################### MARCO VIRINNI ###########################################
#CLASE USUARIO Y SUS 4 ATRIBUTOS (DEFINE UNA ESTRUCTURA BASICA PARA CREAR OBJETOS (USUARIO))DESARROLLADO POR MARCO VIRINNI
class Usuario:
    def __init__(self, apellido, nombre, dni, telefono):
        self.apellido = apellido
        self.nombre = nombre
        self.dni = dni
        self.telefono = telefono

#CLASE LEY Y SUS 5 ATRIBUTOS (DEFINE UNA ESTRUCTURA BASICA PARA CREAR OBJETOS (LEY))DESARROLLADO POR MARCO VIRINNI
class Ley:
    def __init__(self, nro_ley, fecha, jurisdiccion, descripcion, categoria):
        self.nro_ley = nro_ley
        self.fecha = fecha
        self.jurisdiccion = jurisdiccion
        self.descripcion = descripcion
        self.categoria = categoria

#CLASE CONSULTA Y SUS 4 ATRIBUTOS (DEFINE UNA ESTRUCTURA BASICA PARA CREAR OBJETOS (CONSULTA))DESARROLLADO POR MARCO VIRINNI
class Consulta:
    def __init__(self, usuario_id, tipo_busqueda, valor_ingresado):
        self.usuario_id = usuario_id
        self.tipo_busqueda = tipo_busqueda
        self.valor_ingresado = valor_ingresado
        self.fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

##################### RONI DUNCAN ###########################################
#conecta la base de leyes. Duncan Martinez 
def conectar_base_datos_leyes():
    conexion = sqlite3.connect('leyes.db')
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS leyes (
        nro_ley INTEGER PRIMARY KEY,
        fecha DATE,
        jurisdiccion TEXT,
        descripcion TEXT,
        categoria TEXT
        )
     """)
    return conexion

#conecta la base de usuarios. Duncan Martinez 
def conectar_base_datos_usuarios():
    conexion = sqlite3.connect('usuarios.db')
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        apellido TEXT,
        nombre TEXT,
        dni TEXT,
        telefono TEXT
        )
     """)
    return conexion

#conecta la base de Consulta. Duncan Martinez 
def conectar_base_datos_consultas():
    conexion = sqlite3.connect('consultas.db')
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS consultas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER,
        tipo_busqueda TEXT,
        valor_ingresado TEXT,
        fecha TEXT,
        FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
        )
     """)
    return conexion

##################### HERNAN ZAZARINI ###########################################

def cerrar_base_datos_leyes(conexion):
    conexion.close() #cierra base de datos leyes. Hernan Zazzarini

def cerrar_base_datos_usuarios(conexion):
    conexion.close() #cierra base de datos usuarios. Hernan Zazzarini

##################### EMI ROBLES #####################

#Permite cerrar la conexion con la BDD de Consultas. 【★】Desarrollado por Emilce Robles【★】
def cerrar_base_datos_consultas(conexion):
    conexion.close()

#Permite registrar un nuevo usuario permitiendole ingresar sus datos personales de manera manual, que incluyen Apellido, Nombre, DNI y Telefono.
#Con dichos datos se armara el objeto Usuarios que retornara.【★】 Desarrollado por Emilce Robles【★】
def cargar_usuario():
    apellido = input("\n⮞ Ingrese su apellido: ")
    nombre = input("⮞ Ingrese su nombre: ")
    dni = input("⮞ Ingrese su DNI: ")
    telefono = input("⮞ Ingrese su teléfono: ")
    return Usuario(apellido, nombre, dni, telefono)

##################### HERNAN ZAZARINI ###########################################
#Función que recupera y muestra todas las filas de una tabla llamada usuarios en una base de datos.
#La función toma un objeto conexion como argumento, que representa la conexión a la base de datos
#este código verifica si hay algún usuario para mostrar. Si no hay usuarios, imprime un mensaje indicando que no hay usuarios para mostrar. Si hay usuarios, 
#imprime una lista de los usuarios con sus detalles, incluyendo su ID, apellido, nombre, DNI y teléfono. Hernan Zazzarini   
def mostrar_usuarios(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()


    if len(usuarios) == 0:
        print("No hay usuarios para mostrar.")
    else:
        print("\n°•. °•. °•. USUARIOS .•° .•° .•°")
        for usuario in usuarios:
            print(f"ID: {usuario[0]}")
            print(f"Apellido: {usuario[1]}")
            print(f"Nombre: {usuario[2]}")
            print(f"DNI: {usuario[3]}")
            print(f"Teléfono: {usuario[4]}")
            print("================")

# La función crea un objeto cursor a partir de la conexión y ejecuta una consulta SQL 
# para seleccionar el usuario con el ID especificado en la tabla usuarios. 
# Luego, utiliza el método fetchone para recuperar el primer resultado de la consulta. Hernan Zazzarini
def eliminar_usuario(conexion, id_usuario):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id_usuario,))
    usuario = cursor.fetchone()


    if usuario is None:
        print("ID de usuario inválido.")
    else:
        cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))
        conexion.commit()
        print(f"Usuario eliminado: {usuario[2]} {usuario[1]}")

##################### EMI ROBLES #####################

#Submenu que sirve para manipular la información de los usuarios que ingresan a hacer las consulta.
#Permite cargar nuevos registros y subirlos a la BDD Usuarios, mostrarlos en forma de lista uno debajo de otro,
#eliminar usuarios segun su nro de ID y retornar al menu principal. 【★】Desarrollado por Emilce Robles【★】
def submenu_usuarios(conexion):
    while True:
        print("\n°•. °•. °•. MENU DE USUARIOS .•° .•° .•°\n")
        print("1. Cargar un usuario")
        print("2. Mostrar usuarios")
        print("3. Eliminar un usuario")
        print("4. Volver al menú principal")
        opcion = input("\n⮞ Ingrese una opción: ")


        if opcion == "1":
            usuario = cargar_usuario()
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO usuarios (apellido, nombre, dni, telefono) VALUES (?, ?, ?, ?)",
                           (usuario.apellido, usuario.nombre, usuario.dni, usuario.telefono))
            conexion.commit()
            print("\n░▒▓█ Usuario cargado exitosamente █▓▒░")


        elif opcion == "2":
            mostrar_usuarios(conexion)


        elif opcion == "3":
            mostrar_usuarios(conexion)
            id_usuario = int(input("\n⮞Ingrese el ID del usuario a eliminar: "))
            eliminar_usuario(conexion, id_usuario)


        elif opcion == "4":
            break


        else:
            print("\n░▒▓█ Opción inválida. Por favor, ingrese una opción válida █▓▒░")

##################### PAULA VELEZ ###########################################

#Creo la siguiente funcion que sirve para cargar una ley en el programa, para eso le solicito al usuario que ingrese 
#5 valores: n° ley, fecha de promulgacion, jurisdiccion, descripcion y categoria. 
#Despues usando esa informacion ingresada le devuelvo un nuevo objeto "Ley". 
#Ademas "Ley" tiene un constructor que toma los mismos parámetros que la función e inicializa los atributos de la clase con ellos.
def cargar_ley_nueva():
    nro_ley = input("Ingrese el N° de Ley: ")
    fecha = input("Ingrese la fecha en que se promulgó: ")
    jurisdiccion = input("Ingrese la jurisdiccion: ")
    descripcion = input("Ingrese la descripcion: ")
    categoria = input("Ingrese la categoria: ")
    return Ley(nro_ley, fecha, jurisdiccion, descripcion, categoria)

#Por medio de esta funcion estaria mostrando una lista de leyes guardadas en la base de datos, esa base se llama 'leyes',
#si la logitud de la lista es 0 le indico que imprima un mensaje para darle un feedback al usuario, de que no hay leyes para mostrar,
#en caso contrario le indico que imprima un encabezado y la lista de leyes usando la función tabular.
def mostrar_leyes(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM leyes")
    leyes = cursor.fetchall()


    if len(leyes) == 0:
        print("\n░▒▓█No hay leyes para mostrar█▓▒░")
    else:
        print("\n°•. °•. °•. LISTA DE LEYES .•° .•° .•°\n")
        
        headers = ["Nro. Ley", "Fecha", "Jurisdicción", "Descripción", "Categoría"]
        ley_data = [(ley[0], ley[1], ley[2], ley[3], ley[4]) for ley in leyes]
        print(tabulate(ley_data, headers=headers, tablefmt="fancy_grid"))
        
#Para esta funcion lo que estoy haciendo es poder eliminar una ley de la base de datos, esta funcion recibe dos parametros,
#[conexion] que se refiere a la conexion con la base de datos y [id_ley] que seria el número de ID de la ley que se desee borrar.
#para manejar las eventualidades le indico que imprima dos mensajes, uno de exito al eliminar la ley y otro de que el nro_ley que se ingreso no es valido
def eliminar_ley(conexion, id_ley):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM leyes WHERE nro_ley = ?", (id_ley,))
    ley = cursor.fetchone()


    if ley is None:
        print("\n░▒▓█Nro de ley inválido█▓▒░")
    else:
        cursor.execute("DELETE FROM leyes WHERE nro_ley = ?", (id_ley,))
        conexion.commit()
        print(f"\n●●--●●--●● Ley eliminada: N° {ley[0]} ●●--●●--●●")

##################### JORGE PEGORARO ###########################################
#MENU LEYES
# Desarrollado por Jorge Pegoraro (Menú de leyes: te permite seleccionar entre cargar una ley, mostrar una ley, eliminar una ley o volver al menu principal)
def submenu_leyes(conexion):
    while True:
        print("\n\n°•. °•. °•. MENU DE LEYES .•° .•° .•°\n")
        print("1. Cargar una Ley")
        print("2. Mostrar Leyes")
        print("3. Eliminar una Ley")
        print("4. Volver al menú principal")
        opcion = input("\n⮞ Ingrese una opción: ")


        if opcion == "1":
            ley = cargar_ley_nueva()
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO leyes (nro_ley, fecha, jurisdiccion, descripcion, categoria) VALUES (?, ?, ?, ?, ?)",
                           (ley.nro_ley, ley.fecha, ley.jurisdiccion, ley.descripcion, ley.categoria))
            conexion.commit()
            print("-·=»★«=·-Ley cargada exitosamente-·=»★«=·-")


        elif opcion == "2":
            mostrar_leyes(conexion)


        elif opcion == "3":
            mostrar_leyes(conexion)
            id_ley = int(input("\n⮞ Ingrese el N° de Ley a borrar: "))
            eliminar_ley(conexion, id_ley)


        elif opcion == "4":
            break


        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

#=======================
#Desarrollado por Jorge Pegoraro. Buscar leyes permite realizar 2 tipos de busqueda, por nro de ley o por palabra clave.
def buscar_leyes(conexion):
    cursor = conexion.cursor()
    opcion_busqueda = input("¿Desea buscar por número de ley (N) o por palabra clave (P)? ")


    if opcion_busqueda.lower() == "n":
        nro_ley = input("\n⮞ Ingrese el número de ley: ")
        cursor.execute("SELECT * FROM leyes WHERE nro_ley = ?", (nro_ley,))
    elif opcion_busqueda.lower() == "p":
        palabra_clave = input("\n⮞ Ingrese la palabra clave: ")
        cursor.execute("SELECT * FROM leyes WHERE descripcion LIKE ?", ('%' + palabra_clave + '%',))
    else:
        print("Opción inválida.")
        return


    leyes = cursor.fetchall()


    if len(leyes) == 0:
        print("No se encontraron leyes.")
    else:
        headers = ["Nro. Ley", "Fecha", "Jurisdicción", "Descripción", "Categoría"]
        ley_data = [(ley[0], ley[1], ley[2], ley[3], ley[4]) for ley in leyes]
        print("\n=== Leyes Encontradas ===")
        print(tabulate(ley_data, headers=headers))
        print("==========================")

#Desarrollado por Jorge  Pegoraro. Permite cargar leyes predeterminadas
def cargar_leyes(conexion):
    leyes = [
        ('27555', '14/08/2020', 'NACIONAL', 'ESTABLECER LOS PRESUPUESTOS LEGALES \nMINIMOS PARA LA REGULACION DE LA \nMODALIDAD DE TELETRABAJO EN AQUELLAS \nACTIVIDADES, QUE POR SU NATURALEZA\n Y PARTICULARES CARACTERISTICAS \nLO PERMITAN', 'LABORAL'),
        ('20744', '11/09/1974', 'NACIONAL', 'REGULA LAS RELACIONES LABORALES DE LOS \nTRABAJADORES QUE SE ENCUENTRAN BAJO\n RELACION DE DEPENDENCIA, INDICA\n CUALES SON LAS CARACTERISTICAS QUE\n DEBE REUNIR UN CONTRATO LABORAL', 'LABORAL'),
        ('7642', '25/11/1987', 'PROVINCIAL', 'DETERMINA LAS CONDICIONES PARA EL \nEJERCICIO PROFESIONAL DE CIENCIAS \nINFORMÁTICAS, CONSTITUYE EL CONSEJO\n PROFESIONAL DE CIENCIAS INFORMÁTICAS\n DE LA PROVINCIA DE CÓRDOBA,\n DETERMINA UN CÓDIGO DE ÉTICA\n (DEBERES PARA PROFESIONALES \nY PARA CLIENTES)', 'DERECHO INFORMATICO')
    ]


    cursor = conexion.cursor()
    for ley in leyes:
        nro_ley = ley[0]
        cursor.execute("SELECT * FROM leyes WHERE nro_ley = ?", (nro_ley,))
        existing_ley = cursor.fetchone()
        if existing_ley is None:
            cursor.execute("INSERT INTO leyes VALUES(?,?,?,?,?)", ley)
             
        
    conexion.commit()

##################### PAMELA PONCE ###########################################
#Consultar información usando el número de la ley. Si el número de ley se encuentra en la base, nos muestra el detalle. En el caso de una ley que no esta en la base, muestra el mensaje que no se encuentra la ley. 
def consultar_por_numero_ley(conexion, conexion_consultas, conexion_usuarios):
    nro_ley = input("Ingrese el número de ley a consultar: ")


    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM leyes WHERE nro_ley = ?", (nro_ley,))
    ley = cursor.fetchone()


    if ley is None:
        print("No se ha encontrado la ley ingresada.")
    else:
        headers = ["N° Ley", "Fecha", "Jurisdicción", "Descripción", "Categoría"]
        ley_data = [ley]
        ley_table = tabulate(ley_data, headers=headers, tablefmt="fancy_grid")
        print(ley_table)


        usuario_id = obtener_ultimo_usuario_id(conexion_usuarios)
        consulta = Consulta(usuario_id, "Búsqueda por N° de Ley", nro_ley)
        guardar_consulta(conexion_consultas, consulta)

# Consultar información usando una palabra clave de la ley. Se ingresa la palabra clave y muestra la información de la ley. En caso de una palabra que no es clave, muestra el mensaje de que no se encuentran leyes con esa clave.
def consultar_por_palabra_clave(conexion, conexion_consultas, conexion_usuarios):
    palabra_clave = input("Ingrese la palabra clave a buscar: ")


    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM leyes WHERE descripcion LIKE ?", ('%' + palabra_clave + '%',))
    leyes = cursor.fetchall()


    if len(leyes) == 0:
        print("No se ha encontrado ninguna ley con la palabra clave ingresada.")
    else:
        headers = ["N° Ley", "Fecha", "Jurisdicción", "Descripción", "Categoría"]
        leyes_table = tabulate(leyes, headers=headers, tablefmt="fancy_grid")
        print(leyes_table)


        usuario_id = obtener_ultimo_usuario_id(conexion_usuarios)
        consulta = Consulta(usuario_id, "Búsqueda por Palabra Clave", palabra_clave)
        guardar_consulta(conexion_consultas, consulta)

##################### MARCO VIRINNI ###########################################
#FUNCION QUE REALIZA UNA CONSULTA SQL A TRAVES DEL METODO EXECUTE SE ENCARGA DE OBTENER EL ID MAS ALTO ALMACENADO EN LA TABLA USUARIOS.DB PARA DESARROLLADO POR MARCO VIRINNI
def obtener_ultimo_usuario_id(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT MAX(id) FROM usuarios")
    ultimo_id = cursor.fetchone()[0]
    return ultimo_id

##################### RONI DUNCAN ###########################################
# Guarda cada vez que se hace una consulta teniendo encuenta el tipo de consulta. Duncan Martinez 
def guardar_consulta(conexion, consulta):
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO consultas (usuario_id, tipo_busqueda, valor_ingresado, fecha) VALUES (?, ?, ?, ?)",
                   (consulta.usuario_id, consulta.tipo_busqueda, consulta.valor_ingresado, consulta.fecha))
    conexion.commit()

##################### EMI ROBLES ###########################################
#Permite consultar a la BDD "Consultas" trayendo todas las busquedas que se hicieron en formato tabla.
#Se muestran teniendo en cuenta los campos de ID de la consulta, el ID propio del usuario, Tipo de Busqueda,
# y el valor ingresado por teclado que utilizó para realizar la busqueda.Ademas de la fecha que se generó cuando
# efectuó la consulta. 【★】Desarrollado por Emilce Robles【★】
def mostrar_consultas(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM consultas")
    consultas = cursor.fetchall()


    if len(consultas) == 0:
        print("No hay consultas para mostrar.")
    else:
        headers = ["ID", "Usuario ID", "Tipo de Búsqueda", "Valor Ingresado", "Fecha"]
        consultas_table = tabulate(consultas, headers=headers, tablefmt="fancy_grid")
        print(consultas_table)

##################### PAULA VELEZ ###########################################
#La idea es que por medio de esta funcion genere un submenu con varias opciones y espera a que el usuario seleccione alguna,
#le indique que tome tres parámetros: "conexion_leyes", "conexion_usuarios" y "conexion_consultas",
#que representan conexiones a las 3 bases de datos diferentes que tenemos.
#Ademas estoy usando un bucle while para seguir mostrando el menú hasta que el usuario elija salir del programa.
def submenu_principal(conexion_leyes, conexion_usuarios, conexion_consultas):
    menu = True
    while menu == True:
        print("\n•·.·•·.·•·.·•·.·•Menú Principal•·.·•·.·•·.·•·.·•\n")
        print("1. Registra tus datos")
        print("2. Consulta por N° de Ley")
        print("3. Consulta por Palabra Clave")
        print("4. Editar Leyes")
        print("5. Mostrar lista de consultas")
        print("6. Salir del programa")
        opcion = input("\n⮞ Ingrese una opción: ")


        if opcion == "1":
            submenu_usuarios(conexion_usuarios)


        elif opcion == "2":
            consultar_por_numero_ley(conexion_leyes, conexion_consultas, conexion_usuarios)


        elif opcion == "3":
            consultar_por_palabra_clave(conexion_leyes, conexion_consultas, conexion_usuarios)
        
        elif opcion == "4":
            submenu_leyes(conexion_leyes)

            
        elif opcion == "5":
            mostrar_consultas(conexion_consultas)


        elif opcion == "6":
            cerrar_base_datos_leyes(conexion_leyes)
            cerrar_base_datos_usuarios(conexion_usuarios)
            cerrar_base_datos_consultas(conexion_consultas)
            print("Ha salido del programa. ¡Hasta luego!")
            menu = False                 
            
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

##################### PAMELA PONCE ###########################################
#Por medio de esta función se invoca a las conecciones a las bases de datos. Se hace la precarga de leyes y se ejecuta el menú principal.
def main():
    conexion_leyes = conectar_base_datos_leyes()
    conexion_usuarios = conectar_base_datos_usuarios()
    conexion_consultas = conectar_base_datos_consultas()
    cargar_leyes(conexion_leyes)

    submenu_principal(conexion_leyes, conexion_usuarios, conexion_consultas)


if __name__ == '__main__':
    main()