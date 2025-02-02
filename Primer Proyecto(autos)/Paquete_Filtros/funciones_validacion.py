from Paquete_generales.funciones_menu import *
from Paquete_datos.auto import *
from Paquete_datos.datos_autos import *

class ValidacionesFiltros:
    @staticmethod
    def validar_marca(marca: str, lista_autos: list) -> bool: 
        """Verifica que la marca ingresada sea valida.

        Args:
            marca (str): La marca ingresada por el usuario.
            lista_autos (list): La lista donde se encuentran los datos.

        Returns:
            resultado(bool): Indica si la marca ingresada es valida o no.
        """
        resultado = False
        for auto in lista_autos:
            if marca == auto.marca:
                resultado = True 
                break
            
        return resultado
    
    @staticmethod
    def validar_transmicion(transmicion: str) -> bool:
        """Verifica si la transmicion ingresada por el usuario es correcta.

        Args:
            transmicion (str): La adena ingresada por el usuario.

        Returns:
            bool: _description_
        """
        validacion = True
        transmicion = transmicion.lower()
        if transmicion == "automatica" or transmicion == "manual" or transmicion == "automática":
            validacion = False

        return validacion

