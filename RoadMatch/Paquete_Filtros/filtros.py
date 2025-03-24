from abc import ABC, abstractmethod
from Paquete_datos.auto import *
from Paquete_datos.datos_autos import *


class Filtro(ABC):
    @abstractmethod
    def aplicar(self, lista_autos: list ) -> list:
        """Aplica el filtro y retorna la lista filtrada.
        """
        pass

class FiltroMarca(Filtro):
    def __init__(self, lista_autos: list):
        self.lista_autos = lista_autos
    
    def aplicar(self, lista_autos: list, marca: str) -> list:
        """Filtra los vehiculos segun la marca ingresada por el usuario.

        Args:
            lista_autos (list): La lista donde se encuentran los datos.

        Returns:
            autos_filtrados_marca(list): La lista de autos filtrada.
        """
        autos_filtrados_marca = []

        for auto in lista_autos:
            if auto["marca"] == marca.capitalize():
                autos_filtrados_marca.append(auto)

        return autos_filtrados_marca

class FiltroAño:
    def __init__(self, lista_autos: list):
        self.lista_autos = lista_autos

    def aplicar(self, lista_autos: list, minimo: int, maximo: int) -> list:
        """Filtra los vehiculos segun el rango de años ingresado por el usuario.
        Args:
        lista_autos(list): La lista donde se encuentran los datos de los autos

        Returns:
            vehiculos_filtrados_año(list): La lista filtrada. 
        """
        vehiculos_filtrados_año = []

        for auto in lista_autos:
            if maximo >= auto["año"] and minimo <= auto["año"]:
                vehiculos_filtrados_año.append(auto)

        return vehiculos_filtrados_año

class FiltroPresupuesto(Filtro):     
    def __init__(self, lista_autos: list):
            self.lista_autos = lista_autos

    def aplicar(self, lista_autos: list, minimo: float, maximo: float) -> list:
        """Filtra la lista de autos segun el presupuesto economico del usuario.

        Args:
        lista_autos(list): La lista donde se encuentran los datos de los autos.

        Returns:
        vehiculos_filtrados(list): Lista con los vehiculos que estan en el rango de precio.

        """
        vehiculos_filtrados_presupuesto = []

        for auto in lista_autos:
            if maximo >= auto["minimo_precio"] and minimo <= auto["minimo_precio"]:
                vehiculos_filtrados_presupuesto.append(auto)

        return vehiculos_filtrados_presupuesto

class FiltroKilometros(Filtro):     
    def __init__(self, lista_autos: list):
            self.lista_autos = lista_autos

    def aplicar(self, lista_autos:list, minimo: int, maximo: int) -> list:
        """Filtra la lista de autos segun la cantidad de kilometros ingresada por el usuario. 


        Args:
            lista_autos (list): La lista donde se encuentran los datos de los autos.

        Returns:
            vehiculos_filtrados_km(list): La lista de autos filtrada por la cantidad de
            kilometros.
        """
        vehiculos_filtrados_km = []

        for auto in lista_autos:
            if minimo <= auto["max_km"] and maximo >= auto["min_km"]:
                vehiculos_filtrados_km.append(auto)

        return vehiculos_filtrados_km

class FiltroTransmicion(Filtro):     
    def __init__(self, lista_autos: list):
            self.lista_autos = lista_autos
    
    def aplicar(self, lista_autos: list, transmicion) -> list:
        """Filtra los autos segun el tipo de transmicion que inreso el usuario.

        Args:
            lista_autos (list): La lista donde se encuentran los autos.

        Returns:
            lista_filtrar_transmicion(list): La lista de autos filtrada.
        """
        vehiculos_filtrados_transmicion = []
        for auto in lista_autos:
            if auto["transmicion"].lower() == transmicion.lower():
                vehiculos_filtrados_transmicion.append(auto)
        return vehiculos_filtrados_transmicion

class FiltroUso(Filtro):     
    def __init__(self, lista_autos: list):
            self.lista_autos = lista_autos
    
    def aplicar(self, lista_autos: list, uso) -> list:
        """Filtra los autos segun el so indicado por el usuario.

        Args:
            lista_autos (list): La lista donde se encuentran los datos de los autos.

        Returns:
            vehiculos_filtrados_uso(list): La lista de autos filtrada segun el uso.
        """
        vehiculos_filtrados_uso = []
        for auto in lista_autos:
            if auto["uso"].lower() == uso.lower():
                vehiculos_filtrados_uso.append(auto)
        return vehiculos_filtrados_uso

class FiltroCarroceria(Filtro):     
    def __init__(self, lista_autos: list):
            self.lista_autos = lista_autos

    def aplicar(self, lista_autos: list, carroceria) -> list:
        """Filtra los autos segun el tipo de carroceria ingresada por el usuario.

        Args:
            lista_autos (list): La lista donde se encuentran los datos.

        Returns:
            vehiculos_filtrados_carroceria(list): La lista filtrada. 
        """
        vehiculos_filtrados_carroceria = []
        for auto in lista_autos:
            if auto["tamaño"].lower() == carroceria.lower():
                vehiculos_filtrados_carroceria.append(auto)
        return vehiculos_filtrados_carroceria

class FiltroConsumo(Filtro):     
    def __init__(self, lista_autos: list):
            self.lista_autos = lista_autos
    
    def aplicar(self, lista_autos: list, consumo) -> list:
        """Filtra los autos segun el costo de consumo ingresado por el usuario.

        Args:
            lista_autos (list): La lista donde se encuentran los datos.

        Returns:
            vehiculos_filtrados_autos(list): La lista filtrada.
        """
        vehiculos_filtrados_consumo = []
        for auto in lista_autos:
            if auto["consumo"].lower() == consumo.lower():
                vehiculos_filtrados_consumo.append(auto)
        return vehiculos_filtrados_consumo
