import random#importamos la libreria random para el ejercicio #6

#Ejercicio #1

print("La lista de numeros es:")
for numeros in range(1,11):#este range es que empieze en uno y termine en 10,(empieze en 1, termine en 11
    print(f" {numeros}")

#Ejercicio #2
lista=[]#la lista donde se guardan los numeros

sum_total=0#variable donde se guarda la suma

while True:

#lower() nos permite convertir el texto en mayusculas y minusculas
    desicion=input("Desea agregar un numero: SI/NO").lower()

    if desicion == "si":#Si el usuario dice que si
        #Se le pediran los numeros y se agregaran a la lista
        numero = int(input("Ingrese un número: "))
        if numero >= 0:
             lista.append(numero)
        else:
            print("Lo siento pero es un numero negativo")

    elif desicion == "no":#Si el usuario dice no
        #Se le imprimira un mensaje
        print("No se ingresaran mas numeros")
        break#Salimos
    else:
        print("Por favor escriba 'Si' o 'No'.")

#Este for cuanta los numeros que has en la lista
for numero in lista:
    sum_total += numero#aqui suma todos los numeros de l lista

print(f"La suma total es: {sum_total}")#Imprime el resultado de la suma total

#Ejercicio #3
lista2=[]#se crea la lista para almacenar la palabra

palabra=input("Ingrese una palabra")#se le pide al usuario la palabra

lista2=list(palabra)#se llena la lista

predeterminada="a"#variable que se le asigna la letra predeterminada

letra_total=0#variable para contar la cantidad de letras encontradas

encontro=False#si encuentra la letra se convierte en true

#isalpha() es un metodo para verificar que no tenga caracteres especiales ni numeros una palabra
if palabra.isalpha():
    #recorre en busca de la letra
    for letra in lista2:
        if letra == predeterminada:#si la encuentra
            encontro=True#se pasa en true
            letra_total += 1#y suma las letras que tiene la palabra

    if encontro:#si encontro la letra le tira un mensaje con el total de letras
        print(f"La letra se encontro y la cantidad de suma de esa letra son: {letra_total} ")
    else:# si no encontro la letra tira un mensaje de que no se encontro
        print("No se encontro esa letra")
else:
    print("Lo siento, esa palabra debe tener un numero o un caracter especial")


#Ejercicio #3
n=int(input("Ingrese un numero entero"))#El usuario ingresa el numero entero

es_primo=True#si el numero es primo se mantiene como verdadero

#este if nos ayuda a verificar que no hayan ingresado numeros negativos
if n >=0:
    if n<2:#verifica que n sea menor a 2
        es_primo=False #si es menor la variable pasa a false
    else:
        for i in range(2,n):#duscamos los divisores de n
            if n%i==0:#el divisor para verificar que no sea primo
                es_primo=False
                break
    if es_primo:#este if imprime los mensajes
        print(f"El numero primo es: {n}")
    else:
        print(f"No es numero primo {n}")
else:
   print("El numero debe ser positivo")


#Ejercicio #5
lista3=[]#se crea la lista para guardar los numeros
cantidad=int(input("Ingrese la cantidad de numeros"))
resultado=1

#se varifica que cantidad sea numeros negativos
if cantidad >=0:
    for i in range(cantidad):#este for permite iterar por la cantidad de numeros ingrsados por el usuario
        n = int(input("Ingrese el numero"))
        lista3.append(n)#se agrega n a la listaa

        # este if si el usuario pone 0 de un solo nos da resultado 0
        if n == 0:
            resultado = 0
            print("El resultado de la multiplicacion es cero")
            break
        else:#Si no nos tira el resultado
            resultado *= n
            print(f"El resultado de la multiplicacion es: {resultado}")
else:
     print("Lo siento la cantidad debe ser un numero positivo")


#Ejercicio #6

secreto=random.randint(1,100)# aqui se genera un rango de 1 a 100

while True:

    adivina=int(input("Cual es el numero: "))#se el pide al usuario que ingrese el numero a adivinar

#Este if verifica que no haya numeros negativos
    if adivina >=0:
        #este if da las pistas y cuando adivinas te da el numero secreto
        if adivina<secreto:
            print("El numero secreto es mayor")
        elif adivina > secreto:
            print("El numero secreto es menor")
        else:
            print(f"Adivinaste el numero que era el {secreto}")
            break#para el bucle
    else:
        print("Solo se aceptan numeros positivos")#tira el mensaje cuando se introduce un numero negativo
        break