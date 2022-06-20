n = True
while n:
    print("elige alguna de las  opciones")
    print("Opcion C. SUMA A 1000")
    print("Opcion D. SALIR")
    op = input()  ##variable por teclado
    
        
    if op == "C" or op == "c":
        w = True
        while w:
            print("Dame un numero")
            num = int(input())
            suma = suma + num
            print("la suma es", suma)
            if suma >= 1000:
                w = False
            print("Se detuvo el programa ")
    if op == "D" or op == "d":
        print("BYE , VUELVE PRONTO")
        n = False
        