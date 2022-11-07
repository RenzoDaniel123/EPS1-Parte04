import sqlite3
conexion = sqlite3.connect("EscobarMejia_almacen.db")

#tabla_Producto="""CREATE TABLE Producto(
#                idproducto INTEGER PRIMARY KEY AUTOINCREMENT,
#                codigo TEXT UNIQUE,
#                nombre VARCHAR(20),
#                precio REAL    
#                )
#               """
#cursor = conexion.cursor()
#cursor.execute(tabla_Producto)
#conexion.close()


cursor = conexion.cursor()
print("\tBienvenido al programa")
print("    Menú")
print("1. Registrar")
print("2. Eliminar")
print("3. Editar")
print("4. Listar")
print("5. Salir")

opcion = int(input("Seleccione una opción: "))

if opcion == 1:
    print("\tREGISTRAR PRODUCTO")
    print("Ingrese código")
    codigo = input()
    print("Ingrese nombre:")
    nombre = input()
    print("Ingrese precio")
    precio = input()
    agregar_producto = [(codigo,nombre,precio)]
    consulta_registro = """INSERT INTO 
                              Producto (codigo, nombre, precio)
                              VALUES (?,?,?)
                            """
    cursor.executemany(consulta_registro,agregar_producto)
    conexion.commit()
    conexion.close()

if opcion == 2:
    print("\tELIMINAR PRODUCTO")
    print("Ingrese código")
    codigo = input()
    consulta_codigo = """ DELETE FROM 
                          Producto 
                          WHERE
                          CODIGO =?""" 
    cursor.execute(consulta_codigo,(codigo,))
    conexion.commit()
    conexion.close()
    
if opcion == 4:
    consulta_lista = """SELECT *
                            FROM Producto
                            ORDER BY codigo
                              """
   

    cursor.execute(consulta_lista)
    lista = cursor.fetchall()
    for Producto in lista:
        print(Producto)

if opcion==5:
    print("Finalizando el programa")
