import sqlite3
conexion = sqlite3.connect("EscobarMejia_almacen.db")
tabla_Producto="""CREATE TABLE Producto(
                idproducto INTEGER PRIMARY KEY AUTOINCREMENT,
                codigo TEXT UNIQUE,
                nombre VARCHAR(20),
                precio REAL    
                )
               """
cursor = conexion.cursor()
cursor.execute(tabla_Producto)
conexion.close()


print("\tBienvenido al programa")
print("    Menú")
print("1. Listar alumno")
print("2. Agregar alumnos")
print("3. Eliminar alumnos")
print("4. Salir")

opcion = int(input("Seleccione una opción: "))

