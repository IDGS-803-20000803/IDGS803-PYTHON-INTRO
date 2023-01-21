num1 =int (input("Dame primer numero"))
num2 =int(input("Dame segundo numero"))

#print("La suma de {} + {} = {}".format(num1,num2,(num1+num2)))

if(num1 > num2):
    print("{} es mayor que {}".format(num1,num2))
else:
    print("{1} es mayor que {0}".format(num1,num2))

print("-------Dato Nuevo---------")

edad = int(input("Dame tu edad"))

if(edad > 18):
    print("Eres mayor de Edad")
elif edad == 18:
    print("tienes 18")
else:
    print("Eres menor de Edad")