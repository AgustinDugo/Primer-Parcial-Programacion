def menu():

    opciones = 0

    while opciones != 9:
        print("\n--- Sistema de Gestion de Clinica --- " \
              "\n1. Cargar pacientes/s"
              "\n2. Mostrar todos los pacientes"
              "\n3. Buscar pacientes por numero de Historia Clinica"
              "\n4. Ordenar pacientes por numero de Historia Clinica ."
              "\n5. Mostrar pacientes con mas dias de internacion" 
              "\n6. Mostrar pacientes con menos dias de internacion" \
              "\n7. Cantidad de pacientes con mas de 5 dias de internacion"
              "\n8. Promedio de dias de internacion de todos los pacientes"
              "\n9. Salir\n") 

        opcion_input = input("\nIngrese una opción: ")

        if opcion_input.isdigit(): 
            opciones = int(opcion_input)
            if 1 <= opciones <= 9:
                return opciones  
            else:
                print("Por favor ingrese un número entre 1 y 9.")
        else:
            print("Entrada inválida. Ingrese un número.")