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

