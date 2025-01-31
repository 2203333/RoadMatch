
from Paquete_generales.generales import *
from Paquete_Filtros.solicitudes import *

def filtrar_marcas(lista_autos: list) -> list:
    """Filtra los autos segun la marca ingresada por el usuario.

    Args:
        lista_autos (list): La lista donde se encuentran los datos.

    Returns:
        autos_filtrados_marca(list): La lista de autos filtrada.
    """
    autos_filtrados_marca = []
    lista_marcas = solicitar_marca(lista_autos)
    
    for marca in lista_marcas:
        for auto in lista_autos:
            
            if marca == auto["marca"]:
                autos_filtrados_marca.append(auto)

    return autos_filtrados_marca


def filtrar_año(lista_autos: list) -> list:
    """Filtra los vehiculos segun el rango de años ingresado por el usuario.
    Args:
    lista_autos(list): La lista donde se encuentran los datos de los autos
    
    Returns:
        vehiculos_filtrados_año(list): La lista filtrada. 
    """
    vehiculos_filtrados_año = []
    minimo, maximo = solicitar_rangos("Ingrese el minimo de año: ",
                                    "Ingrese el maximo de año: ",
                                    2025, 1960, "Por favor reingrese: ",
                                    5, "Por favor, asegurese de ingresar valores validos.")
    
    for auto in lista_autos:
        if maximo >= auto["año"] and minimo <= auto["año"]:
            vehiculos_filtrados_año.append(auto)

    return vehiculos_filtrados_año
        
    
def filtrar_presupuesto(lista_autos: list) -> list:
    """Filtra la lista de autos segun el presupuesto economico del usuario.

    Args:
    lista_autos(list): La lista donde se encuentran los datos de los autos.

    Returns:
    vehiculos_filtrados(list): Lista con los vehiculos que estan en el rango de precio.

    """
    vehiculos_filtrados_presupuesto = []

    minimo, maximo = solicitar_rangos("Ingrese el valor minimo que desea pagar por su vehiculo: ",
                                  "Ingrese el valor maximo que desea pagar por su vehiculo: ",
                                  1000000000, 20000, "Por favor, reingrese: ", 5,
                                   "Por favor, verifique quue los valores sean correctos." )

    for auto in lista_autos:
        if maximo >= auto["min_precio"] and minimo <= auto["min_precio"]:
            vehiculos_filtrados_presupuesto.append(auto)

    return vehiculos_filtrados_presupuesto

def filtrar_kilometros(lista_autos:list) -> list:
    """Filtra la lista de autos segun la cantidad de kilometros ingresada por el usuario. 


    Args:
        lista_autos (list): La lista donde se encuentran los datos de los autos.

    Returns:
        vehiculos_filtrados_km(list): La lista de autos filtrada por la cantidad de
        kilometros.
    """
    vehiculos_filtrados_km = []
    
    minimo, maximo = solicitar_rangos("Ingrese la cantidad minima de kilometros que tendra su auto: ",
                                  "Ingrese la cantidad maxima de kilometros que tendra su auto: ",
                                  1000000000, 0, "Por favor, reingrese: ", 5,
                                   "Por favor, verifique que los valores sean correctos." )
    
    for auto in lista_autos:
        if minimo <= auto["max_km"] and maximo >= auto["min_km"]:
            vehiculos_filtrados_km.append(auto)
    
    return vehiculos_filtrados_km

def filtrar_transmicion(lista_autos: list) -> list:
    """Filtra los autos segun el tipo de transmicion que inreso el usuario.

    Args:
        lista_autos (list): La lista donde se encuentran los autos.

    Returns:
        lista_filtrar_transmicion(list): La lista de autos filtrada.
    """
    transmicion = solicitar_transmicion()

    vehiculos_filtrados_transmicion = agregar_datos_lista(lista_autos, "transmicion",
                                                          transmicion)

    return vehiculos_filtrados_transmicion


def filtrar_uso(lista_autos: list) -> list:
    """Filtra los autos segun el so indicado por el usuario.

    Args:
        lista_autos (list): La lista donde se encuentran los datos de los autos.

    Returns:
        vehiculos_filtrados_uso(list): La lista de autos filtrada segun el uso.
    """
    lista_opciones = ["familiar", "urbano", "viajes de larga distancia", "todo terreno", "cargamento pesado", "deportivo"]
    
    opcion = crear_menu(lista_opciones)
    opcion_seleccionada = encontrar_opcion(lista_opciones, opcion)
    
    vehiculos_filtrados_uso = agregar_datos_lista(lista_autos, "uso", 
                                                  opcion_seleccionada)
    
    return vehiculos_filtrados_uso

def filtrar_carroceria(lista_autos: list) -> list:
    """Filtra los autos segun el tipo de carroceria ingresada por el usuario.

    Args:
        lista_autos (list): La lista donde se encuentran los datos.

    Returns:
        vehiculos_filtrados_carroceria(list): La lista filtrada. 
    """
    lista_opciones = ["Sedán", "Hatchback", "SUV", "Coupé", "Pick-up", "Minivan"]

    opcion = crear_menu(lista_opciones)
    opcion_seleccionada = encontrar_opcion(lista_opciones, opcion)
    
    vehiculos_filtrados_carroceria = agregar_datos_lista(lista_autos, "tamaño",
                                                         opcion_seleccionada)

    return vehiculos_filtrados_carroceria

def filtrar_consumo(lista_autos: list) -> list:
    """Filtra los autos segun el costo de consumo ingresado por el usuario.

    Args:
        lista_autos (list): La lista donde se encuentran los datos.

    Returns:
        vehiculos_filtrados_autos(list): La lista filtrada.
    """
    lista_opciones = ["muy alto", "alto", "medio", "bajo", "muy bajo"]

    opcion = crear_menu(lista_opciones)
    opcion_seleccionada = encontrar_opcion(lista_opciones, opcion)
    
    vehiculos_filtrados_consumo = agregar_datos_lista(lista_autos, "consumo",
                                                      opcion_seleccionada)
    
    return vehiculos_filtrados_consumo

