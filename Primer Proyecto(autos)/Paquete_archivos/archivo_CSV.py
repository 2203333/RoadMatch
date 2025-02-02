from Paquete_datos.datos_autos import *
def generar_csv(path: str, lista_autos: list):
    """Genera un archivo CSV con los datos de los autos

    Args:
        path (str): Nombre del archivo.
        lista_autos (list): Los datos de los autos.
    """
    with open(path, "w", encoding = "utf8") as archivo:
        archivo.write("marca, modelo, min_km, max_km, min_precio, max_precio, "
                      "transmicion, uso, consumo, tamaño\n")
        for auto in lista_autos:
            cadena = (
                f"{auto['marca']},"
                f"{auto['modelo']},"
                f"{auto['min_km']},"
                f"{auto['max_km']},"
                f"{auto['min_precio']},"
                f"{auto['transmicion']},"
                f"{auto['uso']},"
                f"{auto['consumo']},"
                f"{auto['tamaño']}\n"
            )
            archivo.write(cadena)


