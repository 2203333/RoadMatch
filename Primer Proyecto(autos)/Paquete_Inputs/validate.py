class Validador: 
    """Clase que contiene metodos para validar datos de tipo int y str.

    """
    @staticmethod
    def validar_numero(numero: int, maximo: int, minimo: int, mensaje_error: str,
                        reintentos: int) -> int:
        
        """Realiza la validacion del dato pasado por parametro.

        Args:
            numero (int): El numero a verificar.
            maximo (int): El maximo permitido.
            minimo (int): El minimo permitido.
            mensaje_error (str): Mensaje de error que le indique al usuario que
            el dato es incorrecto.
            reintentos (int): La cantidad de reintentos disponible.

        Returns:
            validacion(int): En caso de que el dato sea correcto lo retorna,
            caso contrario retorna None.
        """

        for _ in range(reintentos):
            try:
                numero = int(numero)
                if minimo <= numero <= maximo:
                    return numero
                else:
                    print(f"El número debe estar entre {minimo} y {maximo}.")
            except ValueError:
                print(f"Debe ingresar unicamente caracteres numericos.")

            numero = input(mensaje_error)

        return None

    @staticmethod
    def validar_cadena(cadena: str, maximo: int, minimo: int,
                     mensaje_error: str) -> str:
        
        """Valida la cadena de caracteres ingresada por el usuario.

        Args:
            cadena (str): La cadena ingrsada por el usuario.
            maximo (int): La cantidad maxima de caracteres.
            minimo (int): La cantidad minima de caracteres.
            mensaje_error (str): El mensaje mostrado al usuario en caso de que 
            el dato sea incorrecto.

        Raises:
            ValueError: Excepcion lanzada en caso de que el usuario ingrese caracteres
                        no aceptados.
            ValueError: Excepcion lanzada en caso de que el usuario ingrese una cadena 
                        fuera de rango.

        Returns:
            cadena(str): La cadena ingresada por el usuario.
        """

        while True:
            try:
                
                if not cadena.isalpha():
                    raise ValueError("Asegurse de ingrsar solo caracteres alfabeticos.")
                if not (minimo <= len(cadena) <= maximo):
                    raise ValueError(f"Debe ingresar entre {minimo} y {maximo} caracteres.")
                return cadena

            except ValueError as error:
                print(error)

            cadena = input(mensaje_error)

        return cadena

    










    










