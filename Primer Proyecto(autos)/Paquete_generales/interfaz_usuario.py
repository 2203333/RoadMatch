from Paquete_Inputs.input import *

class InterfazUsuario: 
    """Clase que contiene metodos relacionados con la interfaz de usuario.

    """

    @staticmethod
    def dar_bienvenida(mensaje: str, maximo: int, minimo: int, mensaje_error: str):
        """Le da la bienvenida al usuario.

        Args:
            mensaje (str): El mensaje que se le muestra al usuario al pedir su nombre.
            maximo (int): La cantidad maxima de caracteres permitido.
            minimo (int): La cantidad minima de caracteres permitido.
            mensaje_error (str): El mensaje mostrado al usuario en caso de que ingrese
            caracteres no permitidos.
        """

        nombre = Solicitador.solicitar_cadena(mensaje, maximo, minimo, mensaje_error) 
        print(f"{nombre}, Bienvenido a RoadMatch. \nPreparate para conocer tu "
        "vehiculo ideal!")

    @staticmethod
    def continuar(mensaje: str) -> bool:
        """Le pregunta al usuario si desea agregar otro valor a la hora de filtrar.

        Args:
            mensaje (str): El mensaje mostrado a la hora de realizar la consulta.

        Returns:
            respusta(bool): True en caso de que quiera agrear un valor.
                            False en caso de que no.
        """
        while True:
            continua = Solicitador.solicitar_cadena(mensaje, 2, 2, "Eleccion invalida. Por favor reingrese: ")
            continua = continua.lower()
            if continua == "si":
                respuesta = True
                break
            else:
                if continua == "no":
                    respuesta = False
                    break
                
        return respuesta

    @staticmethod
    def mostrar_resultados(lista_autos: list):
        if len(lista_autos) > 0:
            print("Los resultados de su busqueda son: ")
            for auto in lista_autos:
                print(f"Marca: {auto.marca} Modelo: {auto.modelo}")
        else:
            print("No tuvimos resultados para tu busqueda.")