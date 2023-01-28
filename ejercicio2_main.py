
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

def main():
    print("1-SUMA")
    print("2-RESTA")
    print("3-multiplicar")
    print("4-dividir")
    print("5-divisionExacta")
    print("6-potencia")
    print("7-salir")
    
    
if __name__=="__main__":
    main()
    
opcion = int(input("Selecciona una Opccion: "))
while  opcion != 7:
    if(opcion == 1):
        suma()
    elif (opcion == 2):
        resta()
    elif (opcion == 3):
        multiplicar()
    elif (opcion == 4):
        dividir()
    elif (opcion == 5):
        divisionExacta()
    elif (opcion == 6):
        potencia()
    else:
        print("Opcion no valida")
    main()
    opcion = int(input("Selecciona una Opccion: "))
   
