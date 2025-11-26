import os

os.system('cls')
def fibonacci_serie():
    n = int(input("Ingrese cuántos números de Fibonacci desea imprimir: "))

    a, b = 0, 1
    print("Serie Fibonacci:")

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
print("/n")
print("/n")
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
       pass
    elif(opcion_seleccionada == '3'):
       pass
    elif(opcion_seleccionada == '4'):
       pass
    elif(opcion_seleccionada == '5'):
        break
 
    input('Presione una tecla para continuar.')
    os.system('cls')
 
 
print("Fue un placer")

