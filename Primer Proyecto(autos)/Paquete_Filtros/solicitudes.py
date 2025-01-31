from Paquete_Inputs.input import *
from Paquete_generales.generales import *
from Paquete_Filtros.funciones_validacion import *

def solicitar_marca(lista_autos: list) -> list:
    """Le pide las marcas de preferencia al usario.

    Args:
        lista_autos (list): La lista donde se encuentran los datos.

    Returns:
        lista_marcas(list): Las marcas de preferencia del usuario.
    """
    lista_marcas = []
    quiere_continuar = True
    while quiere_continuar == True:
        marca = solicitar_cadena("Cual es su marca de preferencia?: ",
                                50, 1, "Marca invalida. Por favor vuelva a intentar: ")
        
        marca = marca.capitalize()
        validacion = validar_marca(marca, lista_autos)
        
        if validacion == False:
            print("Marca invalida, por favor vuelva a intentarlo.")

        else:
           lista_marcas.append(marca)
           quiere_continuar = continuar("Desea agregar otra marca? si/no: ")

    return lista_marcas

def solicitar_rangos(mensaje_min: str, mensaje_max: str, maximo: int, minimo: int,
                      mensaje_error: str, reintentos: int, mensaje_final: str) ->tuple:
    """Se utiliza para preguntarle el rango de presupuesto economico y
      el rango de kilometros de interes.

    Args:
        mensaje_max (str): El mensaje que se le muestra al usuario al pedir el valor maximo.
        mensaje_min (str): El mensaje que se le muestra al usuario al pedir el valor minimo.
        maximo (int): El valor maximo permitido.
        minimo (int): El valor minimo permitido.
        mensaje_error (str): El mensaje mostrado al usuario si el dato es incorrecto.
        reintentos(int): La cantidad de reintentos disponible.
        mensaje_final(str): El mensaje mostrado al usuario si se agotan los reintentos.
    Returns:
        minimo, maximo(tuple): El rango ingresado por el usuario.
    """
    

    valor_minimo = solicitar_numero(mensaje_min, maximo, minimo, mensaje_error, reintentos,
                              mensaje_final)
    
    valor_maximo = solicitar_numero(mensaje_max, maximo, valor_minimo, mensaje_error, reintentos,
                              mensaje_final)
    
    return valor_minimo, valor_maximo

def solicitar_transmicion() -> str:
    """Le solicita al usuario el ingreso del tipo de transmicion deseada.

    Returns:
        transmicion(str): El tipo de transmicion ingresado por el usuario.
    """
    validacion = True
    
    while validacion == True:
        transmicion = solicitar_cadena("Ingrese la transmicion de preferencia: ",
                                       10, 6, "Por favor, reingrese: ")
        
        validacion = validar_transmicion(transmicion)

    return transmicion


