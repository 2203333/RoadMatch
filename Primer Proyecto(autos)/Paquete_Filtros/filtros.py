from abc import ABC, abstractmethod
from Paquete_datos.auto import *
from Paquete_datos.datos_autos import *
from Paquete_generales.funciones_menu import *
from Paquete_Filtros.solicitudes import *

class Filtro(ABC):
    @abstractmethod
    def aplicar(self, lista_autos: list ) -> list:
        """Aplica el filtro y retorna la lista filtrada.
        """
        pass

class FiltroMarca(Filtro):
    def __init__(self, lista_autos: list):
        self.lista_autos = lista_autos
    
    def aplicar(self, lista_autos: list) -> list:
        """Filtra los vehiculos segun la marca ingresada por el usuario.

        Args:
            lista_autos (list): La lista donde se encuentran los datos.

        Returns:
            autos_filtrados_marca(list): La lista de autos filtrada.
        """
        autos_filtrados_marca = []
        
        lista_marcas = SolicitudMarca.solicitar_marca(lista_autos)

        for marca in lista_marcas:
            for auto in lista_autos:

                if marca == auto.marca:
                    autos_filtrados_marca.append(auto)

        return autos_filtrados_marca

class FiltroAño:
    def __init__(self, lista_autos: list):
        self.lista_autos = lista_autos

    def aplicar(self, lista_autos: list) -> list:
        """Filtra los vehiculos segun el rango de años ingresado por el usuario.
        Args:
        lista_autos(list): La lista donde se encuentran los datos de los autos

        Returns:
            vehiculos_filtrados_año(list): La lista filtrada. 
        """
        vehiculos_filtrados_año = []
        minimo, maximo = SolicitudRangos.solicitar_rangos("Ingrese el minimo de año: ",
                                        "Ingrese el maximo de año: ",
                                        2025, 1960, "Por favor reingrese: ",
                                        5, "Por favor, asegurese de ingresar valores validos.")

        for auto in lista_autos:
            if maximo >= auto.año and minimo <= auto.año:
                vehiculos_filtrados_año.append(auto)

        return vehiculos_filtrados_año

class FiltroPresupuesto(Filtro):     
    def __init__(self, lista_autos: list):
            self.lista_autos = lista_autos

    def aplicar(self, lista_autos: list) -> list:
        """Filtra la lista de autos segun el presupuesto economico del usuario.

        Args:
        lista_autos(list): La lista donde se encuentran los datos de los autos.

        Returns:
        vehiculos_filtrados(list): Lista con los vehiculos que estan en el rango de precio.

        """
        vehiculos_filtrados_presupuesto = []

        minimo, maximo = SolicitudRangos.solicitar_rangos("Ingrese el valor minimo que desea pagar por su vehiculo: ",
                                      "Ingrese el valor maximo que desea pagar por su vehiculo: ",
                                      1000000, 14500, "Por favor, reingrese: ", 5,
                                       "Por favor, verifique quue los valores sean correctos." )

        for auto in lista_autos:
            if maximo >= auto.min_precio and minimo <= auto.min_precio:
                vehiculos_filtrados_presupuesto.append(auto)

        return vehiculos_filtrados_presupuesto

class FiltroKilometros(Filtro):     
    def __init__(self, lista_autos: list):
            self.lista_autos = lista_autos

    def aplicar(self, lista_autos:list) -> list:
        """Filtra la lista de autos segun la cantidad de kilometros ingresada por el usuario. 


        Args:
            lista_autos (list): La lista donde se encuentran los datos de los autos.

        Returns:
            vehiculos_filtrados_km(list): La lista de autos filtrada por la cantidad de
            kilometros.
        """
        vehiculos_filtrados_km = []

        minimo, maximo = SolicitudRangos.solicitar_rangos("Ingrese la cantidad minima de kilometros que tendra su auto: ",
                                      "Ingrese la cantidad maxima de kilometros que tendra su auto: ",
                                      1000000000, 0, "Por favor, reingrese: ", 5,
                                       "Por favor, verifique que los valores sean correctos." )

        for auto in lista_autos:
            if minimo <= auto.max_km and maximo >= auto.min_km:
                vehiculos_filtrados_km.append(auto)

        return vehiculos_filtrados_km

class FiltroTransmicion(Filtro):     
    def __init__(self, lista_autos: list):
            self.lista_autos = lista_autos
    
    def aplicar(self, lista_autos: list) -> list:
        """Filtra los autos segun el tipo de transmicion que inreso el usuario.

        Args:
            lista_autos (list): La lista donde se encuentran los autos.

        Returns:
            lista_filtrar_transmicion(list): La lista de autos filtrada.
        """
        lista_opciones = ["automática", "manual"]
        opcion = FuncionesMenu.crear_menu(lista_opciones)
        opcion_seleccionada = FuncionesMenu.encontrar_opcion(lista_opciones, opcion)

        vehiculos_filtrados_transmicion = FuncionesMenu.agregar_datos_lista(lista_autos, "transmicion",
                                                                    opcion_seleccionada)

        return vehiculos_filtrados_transmicion

class FiltroUso(Filtro):     
    def __init__(self, lista_autos: list):
            self.lista_autos = lista_autos
    
    def aplicar(self, lista_autos: list) -> list:
        """Filtra los autos segun el so indicado por el usuario.

        Args:
            lista_autos (list): La lista donde se encuentran los datos de los autos.

        Returns:
            vehiculos_filtrados_uso(list): La lista de autos filtrada segun el uso.
        """
        lista_opciones = ["familiar", "urbano", "viajes de larga distancia", "todo terreno", "cargamento pesado", "deportivo"]

        opcion = FuncionesMenu.crear_menu(lista_opciones)
        opcion_seleccionada = FuncionesMenu.encontrar_opcion(lista_opciones, opcion)

        vehiculos_filtrados_uso = FuncionesMenu.agregar_datos_lista(lista_autos, "uso", 
                                                      opcion_seleccionada)

        return vehiculos_filtrados_uso

class FiltroCarroceria(Filtro):     
    def __init__(self, lista_autos: list):
            self.lista_autos = lista_autos

    def aplicar(self, lista_autos: list) -> list:
        """Filtra los autos segun el tipo de carroceria ingresada por el usuario.

        Args:
            lista_autos (list): La lista donde se encuentran los datos.

        Returns:
            vehiculos_filtrados_carroceria(list): La lista filtrada. 
        """
        lista_opciones = ["Sedán", "Hatchback", "SUV", "Coupé", "Pick-up", "Minivan"]

        opcion = FuncionesMenu.crear_menu(lista_opciones)
        opcion_seleccionada = FuncionesMenu.encontrar_opcion(lista_opciones, opcion)

        vehiculos_filtrados_carroceria = FuncionesMenu.agregar_datos_lista(lista_autos, "tamaño",
                                                             opcion_seleccionada)

        return vehiculos_filtrados_carroceria

class FiltroConsumo(Filtro):     
    def __init__(self, lista_autos: list):
            self.lista_autos = lista_autos
    
    def aplicar(self, lista_autos: list) -> list:
        """Filtra los autos segun el costo de consumo ingresado por el usuario.

        Args:
            lista_autos (list): La lista donde se encuentran los datos.

        Returns:
            vehiculos_filtrados_autos(list): La lista filtrada.
        """
        lista_opciones = ["muy alto", "alto", "medio", "bajo", "muy bajo"]

        opcion = FuncionesMenu.crear_menu(lista_opciones)
        opcion_seleccionada = FuncionesMenu.encontrar_opcion(lista_opciones, opcion)

        vehiculos_filtrados_consumo = FuncionesMenu.agregar_datos_lista(lista_autos, "consumo",
                                                          opcion_seleccionada)

        return vehiculos_filtrados_consumo

