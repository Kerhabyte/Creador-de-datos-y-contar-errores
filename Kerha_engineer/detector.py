import csv #el programa abrira nuetro .csv para despues hacer lo que dice nuestro programa abajo

archivo = open("ventas_10000.csv", "r") #r porque ahora es leer c:
lector = csv.DictReader(archivo) #hacemos entender lo que leera

errores_clientes = 0
errores_cantidad = 0

for fila in lector: #ensena lo que esta leyendo 

    cliente = fila ["clientes"]
    cantidad = int(fila["cantidad"])

    if cantidad <=0:
       errores_cantidad = errores_cantidad + 1

    if cliente == "":
        errores_clientes = errores_clientes + 1

print("Errores en la base de datos:")
print("-Clientes faltantes:", errores_clientes)
print("-Cantidad erronea:", errores_cantidad)


archivo.close()