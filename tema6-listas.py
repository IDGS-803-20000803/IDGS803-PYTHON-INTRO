lista1 = [1,2,3,4,5]

lista2=[1,3,5,"Roberto",True]

print(lista1[-1])
print(lista1[:2])
print(lista1[1:3])
print(lista1[3:])

lista2.append("Laura")
print(lista2)
lista2.insert(3,"Juan")
print(lista2)
lista2.remove("Roberto")
print(lista2)
lista2.pop()
print(lista2)

del lista2[2]
print(lista2)




