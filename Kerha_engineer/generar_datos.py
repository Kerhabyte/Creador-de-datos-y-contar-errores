import random #permite crear datos aleatoriamente
import csv 


cliente = ("Ana", "Carla", "Jose", "Emmanuel", "Luis", "Carlos", "Luu", "Kat", "Rick", "Angel Ikari")
ciudad = ("Sinaloa", "CDMX", "Monterrey", "Guadalajara", "Puebla", "Toluca", "San Miguel de Allende", "Tamaulipas","Taxco", "Veracruz")
producto =("Mouse", "Teclado", "Monitor", "Camara", "Audifonos", "USB", "Laptop", "Adaptador", "SSD", "Impresora")

archivo = open("ventas_10000.csv","w", newline="") # archivo creara un archivo xd tipo csv para hacer un estilo tabla para mis datos
escritor = csv.writer(archivo)

escritor.writerow([ #esto saldra en csv como encabezado

    "id",
    "clientes",
    "ciudades",
    "productos",
    "cantidad",
    "precio"
])

#Crear datos
for i in range(10000): 

    #para que python elija random d:
    clientes = random.choice(cliente)
    posibilidad_faltante = random.randint(1,100) #cree para que falten nombres d:
    if posibilidad_faltante==1:
        clientes = ""


    ciudades = random.choice(ciudad)
    productos = random.choice(producto)

    cantidad = random.randint(1, 100)            
    posibilidad_error = random.randint(1, 1000)  #cree errores beatch
    if posibilidad_error == 1:
        cantidad = random.choice([-15, -100, -56, -49, -75, -13, 0])


    precio = random.randint(100, 35000)



    escritor.writerow([

    i + 1,
    clientes,
    ciudades,
    productos,
    cantidad,
    precio
])

archivo.close()



print ("Datos generados con exitoo!!")

