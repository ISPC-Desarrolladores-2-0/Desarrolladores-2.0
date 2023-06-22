#Inicial
import sqlite3
print("BIENVENIDO")

class Usuario:
    def __init__(self, apellido, nombre, dni, telefono):
        self.apellido = apellido
        self.nombre = nombre
        self.dni = dni
        self.telefono = telefono


def conectar_base_datos():
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, apellido TEXT, nombre TEXT, dni TEXT, telefono TEXT)")
    return conexion


def cerrar_base_datos(conexion):
    conexion.close()


def cargar_usuario():
    apellido = input("Ingrese su apellido: ")
    nombre = input("Ingrese su nombre: ")
    dni = input("Ingrese su DNI: ")
    telefono = input("Ingrese su teléfono: ")
    return Usuario(apellido, nombre, dni, telefono)


def mostrar_usuarios(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()


    if len(usuarios) == 0:
        print("No hay usuarios para mostrar.")
    else:
        print("\n=== Usuarios ===")
        for usuario in usuarios:
            print(f"ID: {usuario[0]}")
            print(f"Apellido: {usuario[1]}")
            print(f"Nombre: {usuario[2]}")
            print(f"DNI: {usuario[3]}")
            print(f"Teléfono: {usuario[4]}")
            print("================")


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


def submenu_usuarios(conexion):
    while True:
        print("\n=== Menú de Usuarios ===")
        print("1. Cargar un usuario")
        print("2. Mostrar usuarios")
        print("3. Eliminar un usuario")
        print("4. Volver al menú principal")
        opcion = input("Ingrese una opción: ")


        if opcion == "1":
            usuario = cargar_usuario()
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO usuarios (apellido, nombre, dni, telefono) VALUES (?, ?, ?, ?)", (usuario.apellido, usuario.nombre, usuario.dni, usuario.telefono))
            conexion.commit()
            print("Usuario cargado exitosamente.")


        elif opcion == "2":
            mostrar_usuarios(conexion)


        elif opcion == "3":
            mostrar_usuarios(conexion)
            id_usuario = int(input("Ingrese el ID del usuario a eliminar: "))
            eliminar_usuario(conexion, id_usuario)


        elif opcion == "4":
            break


        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


def main():
    conexion = conectar_base_datos()


    while True:
        print("\n=== Menú Principal ===")
        print("1. Registra tus datos")
        print("2. Consultar por N° de Ley")
        print("3. Consulta por Palabra Clave")
        print("4. Editar lista de consultas")
        print("5. Salir del programa")
        opcion = input("Ingrese una opción: ")


        if opcion == "1": # Manipulacion de registros de usuarios
            submenu_usuarios(conexion)


        elif opcion == "2":
            # Código para la opción 2 - Consultar por N° de Ley
            pass


        elif opcion == "3":
            # Código para la opción 3 - Consulta por Palabra Clave
            pass


        elif opcion == "4":
            # Código para la opción 4 - Editar lista de consultas
            pass


        elif opcion == "5":
            cerrar_base_datos(conexion)
            print("Ha salido del programa ¡Hasta luego!")
            break


        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


if __name__ == '__main__':
    main()
