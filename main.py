#Bucle de funcion de potencia de numeros enteros

def a_power_b(_a, _b):
    acu = 1
    
    if (_b != 0):
        for i in range(0, abs(_b)):
            acu = acu*_a
            
    if (_b < 0):
        acu = 1/acu
            
    return(acu)

a = 1
b = 1
cont = 1;

while (a != 0):
    print("\nPOTENCIA",cont,"-------------------------")
    a = int(input("Ingrese el numero a: \n"))
    if a != 0:
        b = int(input("Ingrese el numero b: \n"))
        print("-->", a_power_b(a, b))
        cont = cont+1

