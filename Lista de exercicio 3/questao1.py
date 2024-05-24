numeros=[]
for numero in range (1000,2001):
 if numero % 11 == 5:
  numeros.append(numero)
  print("numeros entre 1000 e 2000 que dividido por 11 produzem resto de 5: ")
  for numero in numeros: 
   print(numero)
    