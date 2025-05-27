from funciones.validaciones import validar_dato_numerico
from funciones.validaciones import es_texto

def definir_matriz() -> list[list]:
    """
    Solicita al usuario la cantidad de filas y columnas, 
    y devuelve una matriz (lista de listas) inicializada con None.
    
    Returns:
        list[lists]: Matriz con las dimensiones especificadas, 
        inicializada con None.
    """
    filas = int(input("Ingrese la cantidad de pacientes que quiere ingresar: "))
    columnas = 5
    matriz = [None] * filas
    for i in range(len(matriz)):
        matriz[i] = [None] * columnas
    
    return matriz
    
def cargar_matriz(matriz : list[list]):
    """
    Carga los datos de una matriz previamente inicializada.

    Args:
        matriz (list[list]): Matriz a cargar. Se espera una lista de listas.

    Returns:
        None
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j == 0:
                matriz[i][j] = validar_dato_numerico(input("Ingrese nuemero" \
                " de historia clinica: "))
            elif j == 1:
                matriz[i][j] = es_texto(input("Ingrese nombre del paciente: "))
            elif j == 2:
                matriz[i][j] = validar_dato_numerico(input("Ingrese edad" \
                " del paciente: "))
            elif j == 3:
                matriz[i][j] = es_texto(input("Ingrese diagnostico del paciente: "))
            elif j == 4:
                matriz[i][j] = validar_dato_numerico(input("Ingrese cantidad" \
                " de dias de internacion: "))

                
def mostrar_pacientes(pacientes):
    for i in range(len(pacientes)):
        print("Paciente:")
        for j in range(len(pacientes[i])):
            if j == 0:
                print(f"Historia Clinica: {pacientes[i][j]}")
            elif j == 1:
                print(f"Nombre: {pacientes[i][j]}")
            elif j == 2:
                print(f"Edad: {pacientes[i][j]}")
            elif j == 3:
                print(f"Diagnostico {pacientes[i][j]}")
            elif j == 4:
                print(f"Dias de internacion: {pacientes[i][j]}" )
        print()

def buscar_paciente_por_historia_clinica(matriz : list[list], numero : int) -> list[list]:
    """
    Buscar un paciente por numero de historia clinica.

    Args:
        matriz (list[list]): Matriz donde se busca el paciente.
        nombre (str): numero de historia clinica.

    Returns:
        (str): Si lo encuentra retorna un mensaje con el dato encontrado 
        si no, reotrona un mensaje diciendo que no lo encontro.
    """
    for i in range(len(matriz)):
        if matriz[i][0] == numero:
            return [matriz[i]]
    
    return False


def ordenar_por_historia_clinica(matriz : list[list]):
    """
    ordena de manera ascendente por historia clinica la matriz.

    Args:
        matriz (list[list]): Matriz a ordenar.
    """
    for i in range(len(matriz) - 1):
        for j in range(len(matriz) - 1 - i):
            if matriz[j][0] > matriz[j + 1][0]:
                aux = matriz[j]
                matriz[j] = matriz[j + 1]
                matriz[j + 1] = aux

def mostrar_paciente_con_mas_dias_de_internacion(matriz: list[list]):
    """
    Muestra el paciente con más días de internación.

    Args:
        matriz (list[list]): Matriz donde se busca el paciente.
    """
    if not matriz:
        print("No hay pacientes cargados.")
        

    indice_mayor = 0

    for i in range(1, len(matriz)):
        if int(matriz[i][4]) > int(matriz[indice_mayor][4]):
            indice_mayor = i

    mostrar_pacientes([matriz[indice_mayor]])

def mostrar_paciente_con_menos_dias_de_internacion(matriz : list[list]):
    """
    Muestra el paciente con más días de internación.

    Args:
        matriz (list[list]): Matriz donde se busca el paciente.
    """
    if not matriz:
        print("No hay pacientes cargados.")
        

    indice_menor = 0

    for i in range(1, len(matriz)):
        if int(matriz[i][4]) < int(matriz[indice_menor][4]):
            indice_menor = i

    mostrar_pacientes([matriz[indice_menor]])


def mostrar_pacientes_con_mas_de_5_dias(matriz: list[list]):
    """
    Muestra la cantidad de pacientes con más de 5 días de internación.

    Args:
        matriz (list[list]): Matriz con los pacientes.
    """
    if not matriz:
        print("No hay pacientes cargados.")
        

    contador = 0

    for paciente in matriz:
        if int(paciente[4]) > 5:
            contador += 1

    print(f"Cantidad de pacientes con más de 5 días de internación: {contador}")

def mostrar_promedio_dias_internacion(matriz: list[list]):
    """
    Calcula y muestra el promedio de días de internación de todos los pacientes.

    Args:
        matriz (list[list]): Matriz con los pacientes.
    """
    if not matriz:
        print("No hay pacientes cargados.")
        

    total_dias = 0

    for paciente in matriz:
        total_dias += int(paciente[4])

    promedio = total_dias / len(matriz)
    print(f"Promedio de días de internación: {promedio:.2f}")
