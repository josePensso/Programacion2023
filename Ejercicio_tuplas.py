# Ejercicio hecho en clases, lunes 8 de mayo
ListaTuplas = [("galletas", 500, 25, "chocolinas"), ("fideos", 300, 10, "Terrabusi"), ("gaseosa", 450, 400, "Sprite"), ("arroz", 230, 30, "GalloOro")]
marca = "chocolinas"
precioMax= 600
listaProductos = []
for i in (ListaTuplas):
    if (i[3] == marca and i[1] <= precioMax):
        listaProductos.append(i)
print (listaProductos)

# Esta función llamada 'devolver_distintos' recibe 3 parámetros (int)
# Si la suma es mayor a 15, devolver el mayor
# Si menor a 10, devolver el menor
#Si entre 10 y 15, devolver el intermedio

def devolver_distintos(*args):

    listaNum = list(args) 
    lista.sort()
#    print(lista)
    
    if (sum(listaNum) > 15):
        return listaNum[-1]
    elif (sum(listaNum) < 10):
        return listaNum[0]
    else:
        return listaNum[1]

# Esta función requiere una cantidad indef de arg
# Devuelve True si la función encuentra 2 veces consecutivas el 0

def dosZero (*args):
    listaNum2 = list(args)
    valor = False

    for i in range (0, len(listaNum2)):

        if (i+1 == len(listaNum2)):
            return valor

        elif (listaNum2[i] == 0 and listaNum2[i+1] == 0):
            valor = True
            return valor
        else: pass
        
    print ("la lista no contienen dos ceros consecutivos")

# En guía de ejercicios sobre tuplas
msj = "ingrese una lista de numeros"
print (msj)
lista = list(input())
tupla = tuple(lista)
print (tupla)
inv = tuple(reversed (tupla))
print (inv)

# esta funcion me cuesta...
#def intercambiarTupla(Tuple):
 #   lista = list(Tuple)
  #  ult = len(lista)

# Ejercicio 2 (guía sobre tuplas)
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
    
# Ejercicio 1 (guía sobre tuplas)
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
