#Numero perfecto

def perfect_number(_n):
    global text
    cont = 0
    acu = 0
    
    #buscar divisores
    for i in range(1, _n-1):
        if (_n%i == 0):
            n.insert(cont, i)
            cont = cont +1
            
    #sumar divisores
    for i in range(len(n)):
        acu = acu +n[i]
        if (i == 0):
            text = str(n[i])
        else:
            text = text + " + " + str(n[i])
            
    if (acu == _n) and (_n != 0):
        return(1)
    else:
        return(0)

text = "0"
n = []
num = int(input("Ingrese el numero a comprobar su PERFECCION: "))
print("")
if (perfect_number(num)):
    print(text, "=", str(num))
    print("Enhorabuena! El numero digitado es Perfecto.")
else:
    if (num == 0):
        print("∞ !=", str(num))
    else:
        print(text, "!=", str(num))
    print("Vaya! El numero digitado es imperfecto.")
    