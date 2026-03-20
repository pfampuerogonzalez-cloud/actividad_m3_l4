#1.USO BÁSICO DE WHILE

contador = 1

while contador <5: #SE EJECUTA MIENTRAS LA VARIABLE CONTADOR SEA MENOR O IGUAL A 5
    print(contador)
    contador +=1



#2.USO BÁSICO DE FOR

Lista = ["manzana", "plátano", "naranja"]
    
for fruta in Lista: #RECORRE LA LISTA UNO POR UNO
    print(fruta)



#3.CONDICIÓN EN UN CICLO 

for numero in range(1,11): #SE ESTABLECE UN RANGO DE 1 A 10

    if numero % 2 == 0:  #OPERACIÓN QUE DA EL RESULTADO DE LA DIVISIÓN
        print(str(numero) + ": Par") #DEFINE SI ES PAR

    else:
        print(str(numero) + ": Impar") #DEFINE SI ES IMPAR



#4.CICLO INFINITO CONTROLADO CON BREAK

while True:

 numero = int(input("Ingrese un número, de lo contrario digite 0 para salir: ")) #ESTABLECE UNA ENTRADA AL USUARIO

 if numero == 0: #CONCIÓN DE SALIDA
  print("Exit")
  break #ROMPRE EL CICLO
 
 

#5.CICLO ANIDADO

for i in range(1,4): #CICLO EXTERNO DE MULTIPLICADOR PRINCIPAL
    
    for j in range(1,11): #CICLO INTERNO DE MULTIPLICACIONES
       
       print(i, "*", j, "=", i * j ) #EJECUCIÓN DE MULTIPLICACIÓN MOSTRANDO EL RESULTADO
       
       print("--------") #SEPARADOR VISUAL ENTRE TABLAS
       
      

#6.USO DE CONTINUE

lista_nombres = ["Esteban", "Juan", "Pablo", "Joel", "Francisco"]

for nombre_persona in lista_nombres: #CICLO QUE ITERA LOS NOMBRES UNO POR UNO

    if nombre_persona == "Juan": #PONEMOS LA CONDICIONAL DE QUE SI EL NOMBRE ES JUAN
        continue                 #DA UN SALTO A LA SIGUIENTE ITERACION

    print(nombre_persona) #NO SE EJECUTA SI EL NOMBRE ES JUAN

   



        