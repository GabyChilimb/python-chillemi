def Punto1():
    n1 = input("Ingrese un número.")
    n1 = int(n1)
    n2 = input("Ingrese otro número.")
    n2 = int(n2)

    resultado = n1 + n2

    print("El resultado es: ", resultado)

#Punto1()   

def Punto2():
    n1 = int(input("Ingrese un número."))
    n2 = int(input("Ingrese otro número."))
    n3 = int(input("Ingrese otro número."))
    n4 = int(input("Ingrese otro número."))

    resultado = n1 + n2 + n3 + n4

    print("El resultado es: "+ resultado)

#Punto2() 

def Punto3():
    ladoA = int(input("Cuánto mide el lado a?"))
    ladoB = int(input("Cuánto mide el lado b?"))

    superficie = ladoA * ladoB

    print("La superficie es: "+ superficie)
#Punto3()

def Punto4():
    ladoA = float(input("Inserte un número con decimales."))

    superficie = ladoA * ladoA

    print("La superficie es: "+ superficie)
#Punto4()

def TransformacionPunto5():
    hora = int(input("Ingrese la hora."))
    minutos = int(input("Ingrese los minutos."))
    segundos = int(input("Ingrese los segundos."))

    resultado1 = hora * 3600
    resultado2 = minutos *60

    EnSegundos = resultado1 + resultado2 + segundos

    print("El resultado expresado en segundos es: "+ EnSegundos)
#TransformacionPunto5()

def Punto6():
    ladoA = int(input("Cuánto mide el lado a?"))
    ladoB = int(input("Cuánto mide el lado b?"))


    suptriangulo = ladoA * ladoB /2
    print("La superficie del triángulo es: "+suptriangulo)
#Punto6()

def Punto7():
    n1 = input("Ingrese un número.")
    n1 = int(n1)
    n2 = input("Ingrese un segundo número.")
    n2 = int(n2)
    n3 = input("Ingrese un tercer número.")
    n3 = int(n3)
    n4 = input("Ingrese un cuarto número.")
    n4 = int(n4)
    n5 = input("Ingrese un quinto número.")
    n5 = int(n5)
    n6 = input("Ingrese el último número.")
    n6 = int(n6)

    total = n1+ n2 + n3 + n4 + n5 + n6

    promedio = total/6

    print("El promedio es: "+ promedio)
#Punto7()

def Punto8():
    n1 = int(input("Ingrese un número."))
    n2 = int(input("Ingrese otro número."))

    NUM1 = n1/100
    porcentaje = n2 / NUM1

    print("El promedio es:%", porcentaje)
#Punto8()

def Punto9():
    fecha = int(input("Ingrese la fecha en formato DDMMAAAA."))

    dia = fecha//1000000
    mes = (fecha//10000) % 100
    año = fecha % 10000

    print("Día: ", dia)
    print("Mes: ", mes)
    print("Año: ", año)
#Punto9()

def Punto10():
    a = int(input("Ingrese la calificación de exámen parcial."))
    b = int(input("Ingrese la calificación por TPs."))
    c = int(input("Ingrese la calificación del exámen integrador."))

    calificacionA = a * 0.3
    calificacionB = b * 0.2
    calificacionC = c * 0.5

    notafinal = calificacionA + calificacionB + calificacionC
    print("El promedio del estudiante es: "+ notafinal)
#Punto10

def Punto11():

    autos = []
    inputUser = ""
    while inputUser != "SALIR":
        inputUser = input("ingrese el valor del auto vendido o SALIR")
        if inputUser != "SALIR":
            inputUser = float(inputUser)
            autos.append(inputUser)

    AUx = sum(autos)
    comision = AUx * 0.05

#Punto11()