##maquina de bebidas
##n = True
##while n:

from calendar import c


print ("Que producto deseas elegir A,B,C?")
print("A = $270")
print("B = $340")
print("C = $390")
print("SOLO ACEPTAMOS MONEDAS DE 10,50,100")
opcion = input()

if opcion =="A":
    print("Ingresa moneda1")
    moneda1=int (input())
    print("Ingresa moneda2")
    moneda2=int (input())
    print("Ingresa moneda3")
    moneda3=int (input())
    print("Ingresa moneda4")
    moneda4=int (input())
    suma = moneda1 + moneda2 + moneda3 + moneda4 
    print("Lacantidad ingresada es :",suma)
    if suma >=270:
        cambio = suma - 270
        print("tu cambio es ....",cambio )
    else:
        print("ingresa mas monedas")



if opcion =="B":
    print("Ingresa moneda1")
    moneda1=int (input())
    print("Ingresa moneda2")
    moneda2=int (input())
    print("Ingresa moneda3")
    moneda3=int (input())
    print("Ingresa moneda4")
    moneda4=int (input())
    suma = moneda1 + moneda2 + moneda3 + moneda4 
    print("Lacantidad ingresada es :",suma)
    if suma >=340:
        cambio = suma - 340
        print("tu cambio es ....",cambio )
    else:
        print("ingresa mas monedas")

if opcion =="C":
    print("Ingresa moneda1")
    moneda1=int (input())
    print("Ingresa moneda2")
    moneda2=int (input())
    print("Ingresa moneda3")
    moneda3=int (input())
    print("Ingresa moneda4")
    moneda4=int (input())
    suma = moneda1 + moneda2 + moneda3 + moneda4 
    print("Lacantidad ingresada es :",suma)
    if suma >=390:
        cambio = suma - 390
        print("tu cambio es ....",cambio )
    else:
        print("ingresa mas monedas")


    







