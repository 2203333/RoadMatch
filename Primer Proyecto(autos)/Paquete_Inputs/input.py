from .validate import *

class Solicitador:
    """Clase que contiene metodos para solicitar datos al usuario y validarlos.
    """
    def solicitar_numero(mensaje: str, maximo: int, minimo: int,
                mensaje_error: str, reintentos: int, mensaje_final: str) -> int:
        
        """Pide un numero y llama a la funcion validar_numero para validarlo. 

        Args:
            mensaje (str): El mensaje que se le muestra al usuario al ingresar el dato.
            maximo (int): El valor maximo permitido.
            minimo (int): El valor minimo permitido.
            mensaje_error (str): El mensaje que se le muestra al usuario en caso de que
            el dato sea incorreco.
            reintentos (int): La cantidad de intentos que tiene el usuario para ingresar
            el dato.
            mensaje_final (str): El mensaje que se le muestra al usuario en caso de que
            se quede sin intentos.

        Returns:
            resultado(int): El numero validado.
        """
        numero = input(mensaje)
        numero_validado = Validador.validar_numero(numero, maximo, minimo,
                                                    mensaje_error, reintentos)
        
        if numero_validado == None:
            resultado = mensaje_final
        else: 
            resultado = numero_validado
        
        return resultado


    def solicitar_cadena(mensaje: str, maximo: int, minimo: int, 
                         mensaje_error: str) -> str:
        
        """Pide un dato de tipo str y llama a validar_cadena para validarlo.

        Args:
            mensaje (str): El mensaje que se le muestra al usuario al pedir el str.
            maximo (int): La cantidad maxima de caracteres permitido.
            minimo (int): La cantidad minima de caracteres permitido.
            mensaje_error (str): El mensaje mostrado al usuario en caso de que
            el dato sea incorrecto.

        Returns:
            cadena_validada(str): La cadena ingresada por el usuario ya validada.
        """
        cadena = input(mensaje)
        cadena_validada = Validador.validar_cadena(cadena, maximo, minimo, mensaje_error)

        return cadena_validada

