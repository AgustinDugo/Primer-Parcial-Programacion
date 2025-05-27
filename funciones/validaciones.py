def validar_dato_numerico(dato: str) -> int:
    """
    Valida que el dato ingresado sea numérico. Si no lo es, solicita
    al usuario que ingrese un nuevo valor hasta que sea válido.

    Args:
        dato (str): Dato a validar.

    Returns:
        int: El dato validado y convertido a entero.
    """
    while dato.isdigit() == False:
        print("Error: el dato debe ser numérico.")
        dato = input("Ingrese el dato correcto: ")

    return int(dato)

def es_texto(dato):

    while dato.isdigit() == True:
        print("Error: el dato no puede ser numerico.")
        dato = input("Ingrese el dato correcto: ")
    return dato 

def es_matriz_vacia(matriz : list[list]) -> bool:
    """
    Valida que la matriz contenga elementos.

    Args:
        matriz (list[list]): Matriz a validar.

    Returns:
        bool: Si la matriz contiene elementos, retorna true,
             Si la matriz es igual a cero, retorna false.
    """
    if len(matriz) == 0:
        return True
    return False