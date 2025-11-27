import os

os.system('cls')
def fibonacci_serie():
    n = int(input("Ingrese cuántos números de Fibonacci desea imprimir: "))

    a, b = 0, 1
    print("Serie Fibonacci:")

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b



def calcular_factorial():
    n = int(input("Ingrese un número: "))
    
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    print(f"El factorial de {n} es {factorial}")

def imprimir_primos():
    n = int(input("Ingrese cuántos números primos desea imprimir: "))
    contador = 0
    numero = 2  # empezamos a buscar primos desde 2

    while contador < n:
        es_primo = True
        
        for i in range(2, numero):
            if numero % i == 0:
                es_primo = False
                break
        
        if es_primo:
            print(numero)
            contador += 1
        
        numero += 1    

def mostrar_perfectos():
    n = int(input("¿Cuántos números perfectos deseas ver? "))
    
    encontrados = 0
    num = 1

    while encontrados < n:
        suma = 0
        for i in range(1, num):
            if num % i == 0:
                suma += i
        
        if suma == num:
            print(num)
            encontrados += 1

        num += 1

def rellenar_espacios(texto, tamanio):
    cantidad_espacios = tamanio - len(texto)
    return texto + ' ' * cantidad_espacios
 
print("╔" + "═" * 64 + "╗")
print("║" + "Bienvenido al mundo de ...".center(64) + "║")
print("╚" + "═" * 64 + "╝\n")
 
while True:
    print("╔" + "═" * 64 + "╗")
    print("║" + 'Seleccione una de las siguientes opciones'.center(64) + "║")
    print("╠" + "═" * 64 + "╣")
    print("║" + rellenar_espacios(' 1. Fibonacci', 64) + "║")
    
    
    print("║" + rellenar_espacios(' 2. Factorial', 64) + "║")
    print("║" + rellenar_espacios(' 3. Primos', 64) + "║")
    print("║" + rellenar_espacios(' 4. N números perfectos', 64) + "║")
    print("║" + rellenar_espacios(' 5. salir', 64) + "║")
    print("╚" + "═" * 64 + "╝\n")
 
    opcion_seleccionada = input('Digite la opcion a elegir: ')
    if (opcion_seleccionada == '1'):
       fibonacci_serie()
       pass
    elif(opcion_seleccionada == '2'):
       calcular_factorial()
       pass
    elif(opcion_seleccionada == '3'):
       imprimir_primos()
       pass
    elif(opcion_seleccionada == '4'):
       mostrar_perfectos()
       pass
    elif(opcion_seleccionada == '5'):
        break
 
    input('Presione una tecla para continuar.')
    os.system('cls')
 
 
print("Fue un placer")

