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

lista_productos = [('001','Televisor Smart 39',749),
                 ('002','Redmi 10C 3G+64GB',599),                
                 ('003','Televisor 70 LG UHD',2899),
                 ('004','Sansung A53 5G',1449),
                 ('005','Galaxy A23 128GB 4GB',799),
                 ('006','MOTO G31 4GB + 128GB',949),
                 ('007','Lavadora 16Kg Blanco',1299),
                 ('008','PS5 HW STANDARD',4299),
                 ('009','Lavadora Inverter',1699),
                 ('010','Control PS4 negro',329)
                 ]
 
consulta_registro = """INSERT INTO
                              Producto (codigo, nombre, precio)
                              VALUES (?,?,?)
                            """
cursor = conexion.cursor()
cursor.executemany(consulta_registro, lista_productos)
conexion.commit()
conexion.close()



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

if opcion == 4:
    consulta_lista = """SELECT *
                            FROM Producto
                            ORDER BY codigo
                              """
    cursor.execute(consulta_lista)
    lista = cursor.fetchall()
    for Producto in lista:
        print(Producto)




