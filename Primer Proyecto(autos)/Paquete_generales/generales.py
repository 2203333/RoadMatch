from Paquete_Inputs.input import *


def dar_bienvenida(mensaje: str, maximo: int, minimo: int, mensaje_error: str):
    """Le da la bienvenida al usuario.

    Args:
        mensaje (str): El mensaje que se le muestra al usuario al pedir el str.
        maximo (int): La cantidad maxima de caracteres permitido.
        minimo (int): La cantidad minima de caracteres permitido.
        mensaje_error (str): El mensaje mosrado al usuario en caso de que el dao sea incorrecto.
    """
    
    nombre = solicitar_cadena(mensaje, maximo, minimo, mensaje_error) 
    print(f"{nombre}, bienvenido a RoadMatch! \nA continuacion responderas una "
    "serie de preguntas para conocer tu vehiculo ideal")

dar_bienvenida("Ingrese su nombre: ", 30, 1, "Por favor, reingrese: ")

def crear_menu(lista_opciones: list) -> int:
    """Crea un menu de opciones.

    Args:
        lista_opciones (list): La lista de opciones.

    Returns:
        eleccion(int): La opcion seleccionada por el usuario.
    """

    for i, opcion in enumerate(lista_opciones, start= 1):
        print(f"{i}. {opcion}")
    
    while True:
        eleccion = solicitar_numero("Ingrese una opcion: ", (i),
                                1, "Por favor, reingrese: ", 10, 
                                "Asegurese de ingresar correctamente la opcion.")

        return eleccion
        
def encontrar_opcion(lista_opciones: list, opcion: int) -> str:
    """Encuentra la opcion que selecciono el usuario en la lista de opciones.

    Args:
        lista_opciones (list): La lista donde se encuentran las opciones.
        opcion (int): El numero de la opcion que selecciono el usuario.

    Returns:
        opcion_seleccionada(str): El valor del numero de opcion quue selecciono el usuario.
    """
    for i in range(len(lista_opciones)):
        if opcion == i + 1: 
            opcion_seleccionada = lista_opciones[i]
            break

    return opcion_seleccionada

def agregar_datos_lista(lista_autos: list, criterio: str, opcion_seleccionada: str) -> list:
    """Agrega los datos filtrados a la lista.

    Args:
        lista_autos (list): La lista donde se encuentran los datos. 
        criterio (str): La clave del diccionario para ralizar la busqda de los datos.
        opcion_seleccionada (str): La opcion seleccionada por el usuario.

    Returns:
        lista_filtro(list): La lista ya filtrada.
    """
    lista_filtro = []
    for auto in lista_autos:
        if auto[criterio] == opcion_seleccionada:
            lista_filtro.append(auto)
    
    return lista_filtro
        
def continuar(mensaje: str) -> bool:
    """Le pregunta al usuario si desea agregar otro valor a la hora de filtrar.

    Args:
        mensaje (str): El mensaje mostrado a la hora de realizar la consulta.

    Returns:
        respusta(bool): True en caso de quee quiera agrear un valor.
                        False en caso de que no.
    """
    while True:
        continua = solicitar_cadena(mensaje, 2, 2, "Eleccion invalida. Por favor reingrese: ")
        continua.lower
        if continua == "si":
            respuesta = True
            break
        else:
            if continua == "no":
                respuesta = False
                break
    
    return respuesta
      
def mostrar_resultados(lista_autos: list):
    if len(lista_autos) > 0:
        print("Los resltados de su busqueda son: ")
        for auto in lista_autos:
            print(f"Marca: {auto['marca']} Modelo{auto['modelo']}")
    else:
        print("No tuvimos resultados para tu busqueda.")
