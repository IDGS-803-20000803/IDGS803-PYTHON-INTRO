numero = int(input("Numero para tabla de multiplicar: "))

def funcion(x):
    for i in range(1,11):
        print("{} x {} = {}".format(x, i, x*i))

funcion(numero)