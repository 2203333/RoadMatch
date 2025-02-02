from Paquete_Inputs.input import *

class FuncionesMenu:
    """Clase que contiene metodos utilizados a la hora de trabajar con el
    menu de opciones.
    """

    @staticmethod
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
            eleccion = Solicitador.solicitar_numero("Ingrese una opcion: ", (i),
                                    1, "Por favor, reingrese: ", 10, 
                                    "Asegurese de ingresar correctamente la opcion.")

            return eleccion


    @staticmethod
    def encontrar_opcion(lista_opciones: list, opcion: int) -> str:
        """Encuentra la opcion que selecciono el usuario en la lista de opciones.

        Args:
            lista_opciones (list): La lista donde se encuentran las opciones.
            opcion (int): El valor numerico de la opcion que selecciono el usuario.

        Returns:
            opcion_seleccionada(str): La opcion que selecciono el usuario.
        """
        for i in range(len(lista_opciones)):
            if opcion == i + 1: 
                opcion_seleccionada = lista_opciones[i]
                break

        return opcion_seleccionada


    @staticmethod
    def agregar_datos_lista(lista_autos: list, criterio: str, opcion_seleccionada: str) -> list:
        """Agrega los datos filtrados a la lista.

        Args:
            lista_autos (list): La lista donde se encuentran los datos. 
            criterio (str): El atributo por el que se realiza el filtro.
            opcion_seleccionada (str): La opcion seleccionada por el usuario.

        Returns:
            lista_filtro(list): La lista ya filtrada.
        """
        lista_filtro = []
        for auto in lista_autos:
            if getattr(auto, criterio) == opcion_seleccionada:
                lista_filtro.append(auto)

        return lista_filtro
