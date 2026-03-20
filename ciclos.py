#1.USO BÁSICO DE WHILE

""" contador = 1

while contador <5:
    print(contador)
    contador +=1 """

#2.USO BÁSICO DE FOR

""" Lista = ["manzana", "plátano", "naranja"]
    
for fruta in Lista:
    print(fruta)
 """
#3.CONDICIÓN EN UN CICLO 

""" for numero in range(1,11):

    if numero % 2 == 0:
        print(str(numero) + ": Par")

    else:
        print(str(numero) + ": Impar") """


#4.CICLO INFINITO CONTROLADO CON BREAK

while True:

 numero = int(input("Ingrese un número, de lo contrario digite 0 para salir: "))

 if numero == 0:
  print("Exit")
  break

#5.CICLO ANIDADO

for i in range(1,14):
    for j in range(1,11):
   