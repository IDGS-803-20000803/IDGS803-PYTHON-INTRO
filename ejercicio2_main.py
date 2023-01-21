
def suma():
    num1 =int (input("Dame primer numero"))
    num2 =int(input("Dame segundo numero"))
    print("Suma: ",(num1 + num2))
def resta():
    num1 =int (input("Dame primer numero"))
    num2 =int(input("Dame segundo numero"))
    print("Resta: ",(num1 - num2))
def multiplicar():
    num1 =int (input("Dame primer numero"))
    num2 =int(input("Dame segundo numero"))
    print("Multiplicar: ",(num1*num2))
def dividir():
    num1 =int (input("Dame primer numero"))
    num2 =int(input("Dame segundo numero"))
    print("Dividir: ",(num1/num2))
def divisionExacta():
    num1 =int (input("Dame primer numero"))
    num2 =int(input("Dame segundo numero"))
    print("Division Exacta", (num1 // num2))
def potencia():
    num1 =int (input("Dame primer numero"))
    num2 =int(input("Dame segundo numero"))
    print("Potencia: ",(num1**num2))

print("1-SUMA")
print("2-RESTA")
print("3-multiplicar")
print("4-dividir")
print("5-divisionExacta")
print("6-potencia")
print("7-salir")
opcion = int(input("Selecciona un Opccion: "))
while  opcion != 7:
    if(opcion == 1):
        suma()
    if (opcion == 2):
        resta()
    if (opcion == 3):
        multiplicar()
    if (opcion == 4):
        dividir()
    if (opcion == 5):
        divisionExacta()
    if (opcion == 6):
        potencia()
    print("1-SUMA")
    print("2-RESTA")
    print("3-multiplicar")
    print("4-dividir")
    print("5-divisionExacta")
    print("6-potencia")
    print("7-salir")
    opcion = int(input("Selecciona un Opccion: "))
