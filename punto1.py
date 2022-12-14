cont = 0
numero=0
for i in range(10):
    numero = (int(input("ingrese un numero: ")))
    if numero  % 3 == 0 :
     cont = cont + 1
print(f"la cantidad de numeros multiplos de 3 es: {cont}")