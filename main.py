#Funcion de potencia de numeros enteros


def a_powe_b(_a, _b):
    acu = 1
    
    if (_b != 0):
        for i in range(0, abs(_b)):
            acu = acu*_a
            
    if (_b < 0):
        acu = 1/acu
            
    return(acu)

a = int(input("Ingrese el numero a: "))
b = int(input("Ingrese el numero b: "))

print(a_powe_b(a, b))

