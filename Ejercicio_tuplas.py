ListaTuplas = [("galletas", 500, 25, "chocolinas"), ("fideos", 300, 10, "Terrabusi"), ("gaseosa", 450, 400, "Sprite"), ("arroz", 230, 30, "GalloOro")]
marca = "chocolinas"
precioMax= 600
listaProductos = []
for i in (ListaTuplas):
    if (i[3] == marca and i[1] <= precioMax):
        listaProductos.append(i)
print (listaProductos)

ListaTuplas = [("galletas", 500, 25, "chocolinas"), ("fideos", 300, 10, "Terrabusi"), ("gaseosa", 450, 400, "Sprite"), ("arroz", 230, 30, "GalloOro")]

marca = "chocolinas"
precioMax= 100
listaProductos = []
for i in (ListaTuplas):
    if (i[3] == marca and i[1] <= precioMax):
        listaProductos.append(i)
print (listaProductos)

msj = "ingrese una lista de numeros"
print (msj)
lista = list(input())
tupla = tuple(lista)
print (tupla)
inv = tuple(reversed (tupla))
print (inv)

def intercambiarTupla(Tuple):
    lista = list(Tuple)
    ult = len(lista)

# Ejercicio 2
tuplaV = (3,5,6,7,2,3,5,5,2)
print ("Ingrese un numero")
numVeces = 0
num = int(input())
for i in tuplaV:
    if num == tuplaV[i]:
        numVeces = numVeces + 1
    else:
        numVeces = numVeces
print ("El numero aparece " + str(numVeces) + " veces en la tupla")
    
# Ejercicio 1
mesesAño = ('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre')
fin = True
#print ("ingrese un número\nPara salir del programa ingrese 0 (cero)")
while (fin == True):
    print ("ingrese un número\nPara salir del programa ingrese 0 (cero)")  
    nro = int(input())
    if nro > len(mesesAño):
        print("Error")
    elif nro > 0 and nro < 12:
        mes = mesesAño[nro]
        print (mes)
    elif nro == 0:
        fin = False
        

