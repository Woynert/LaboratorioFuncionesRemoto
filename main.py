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
cont = 1
nCal = 0
nPar = 0
nImp = 0
nErr = 0
res = 0

#Bucle 
while (a != 0):
    print("\nPOTENCIA",cont,"___________________________")
    try:
        a = int(input("Ingrese el numero a: \n"))
        if a != 0:
            b = int(input("Ingrese el numero b: \n"))
            res = a_power_b(a, b)
            
            #Comprobar paridad 
            if (res % 2 == 0):
                nPar = nPar +1
            else:
                nImp = nImp +1
                
            print("-->", res)
            cont = cont +1
            nCal = nCal +1
    except:
        print("ERROR: Por Favor Vuelva A Intentar")
        a = 1
        nErr = nErr +1
print("\n___________________________________")
print("Resumen\nPotencias calculadas:",nCal,"\nPotencias pares:",
      nPar,"\nPotencias impares:",nImp,"\nErrores:",nErr)
