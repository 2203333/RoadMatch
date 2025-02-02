class Auto:
    def __init__(self, marca, año, modelo, min_km, max_km, min_precio, transmicion, uso, consumo, tamaño):
        """Representa los automoviles con sus atributos asociados.

        Atributos:
            marca (str): La marca del vehiculo.
            año (int): El año de fabricacion.
            modelo (str): El modelo del vehiculo.
            min_km (_type_): La cantidad minima de kilometros.
            max_km (_type_): La cantidad maxima de kilometros.
            min_precio (_type_): El valor minimo de mercado por el vehiculo.
            transmicion (str): automatica o manual.
            uso (str): El uso idel del vehiculo.
            consumo (str): El rango de consumo entre nafta, seguro y patente.
            tamaño (str): El tipo de carroceria del vehiculo.
        """
        self.marca = marca
        self.año = año
        self.modelo = modelo
        self.min_km = min_km
        self.max_km = max_km
        self.min_precio = min_precio
        self.transmicion = transmicion
        self.uso = uso
        self.consumo = consumo
        self.tamaño = tamaño