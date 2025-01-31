from Paquete_Filtros.filtros import *
from Paquete_generales import *
def crear_menu_principal(lista_autos: list) -> list:
    lista_opciones = ["Marca", "Año", "Presupuesto", "Kilometros",
                     "Transmicion", "Uso", "Consumo", "Carroceria",
                     "Ver resultados"]
    while True:
        eleccion = crear_menu(lista_opciones)
    
        match eleccion:
        
            case 1:
                lista_autos = filtrar_marcas(lista_autos)
            case 2:
                lista_autos = filtrar_año(lista_autos)
            case 3:
                lista_autos = filtrar_presupuesto(lista_autos)
            case 4:
                lista_autos = filtrar_kilometros(lista_autos)
            case 5:
                lista_autos = filtrar_transmicion(lista_autos)
            case 6:
                lista_autos = filtrar_uso(lista_autos)
            case 7:
                lista_autos = filtrar_consumo(lista_autos)
            case 8:
                lista_autos = filtrar_carroceria(lista_autos)
            case 9:
                mostrar_resultados(lista_autos)
            
         
