class operBas():
    def suma(self):
        num1 =int (input("Dame primer numero"))
        num2 =int(input("Dame segundo numero"))
        print("Suma: ",(num1 + num2))
    def resta(self):
        num1 =int (input("Dame primer numero"))
        num2 =int(input("Dame segundo numero"))
        print("Resta: ",(num1 - num2))
    def multiplicar(self):
        num1 =int (input("Dame primer numero"))
        num2 =int(input("Dame segundo numero"))
        print("Multiplicar: ",(num1*num2))
    def dividir(self):
        num1 =int (input("Dame primer numero"))
        num2 =int(input("Dame segundo numero"))
        print("Dividir: ",(num1/num2))

def main():
    print("1-SUMA")
    print("2-RESTA")
    print("3-multiplicar")
    print("4-dividir")
    print("5-salir")
    opcion = int(input("Selecciona una Opccion: "))
    obj=operBas()
    while  opcion != 5:
        
        if(opcion == 1):
            obj.suma()
        elif (opcion == 2):
            obj.resta()
        elif (opcion == 3):
            obj.multiplicar()
        elif (opcion == 4):
            obj.dividir()
        else:
            print("Opcion no valida")
            
        opcion = int(input("Selecciona una Opccion: "))
        
        

if __name__=="__main__":
    main()

