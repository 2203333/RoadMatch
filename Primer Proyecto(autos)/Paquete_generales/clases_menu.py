from Paquete_Filtros.filtros import *
from Paquete_generales import *
from .funciones_menu import *

def crear_menu_principal(lista_autos: list) -> list:
    lista_opciones = ["Marca", "Año", "Presupuesto", "Kilometros",
                     "Transmicion", "Uso", "Consumo", "Carroceria",
                     "Ver resultados"]
    while True:
        eleccion = FuncionesMenu.crear_menu(lista_opciones)
    
        match eleccion:
        
            case 1:
                filtro = FiltroMarca(lista_autos)
                lista_autos = filtro.aplicar(lista_autos)
            case 2:
                filtro = FiltroAño(lista_autos)
                lista_autos = filtro.aplicar(lista_autos)
            case 3:
                filtro = FiltroPresupuesto(lista_autos)
                lista_autos = filtro.aplicar(lista_autos)
            case 4:
                filtro = FiltroKilometros(lista_autos)
                lista_autos = filtro.aplicar(lista_autos)
            case 5:
                filtro = FiltroTransmicion(lista_autos)
                lista_autos = filtro.aplicar(lista_autos)
            case 6:
                filtro = FiltroUso(lista_autos)
                lista_autos = filtro.aplicar(lista_autos)
            case 7:
                filtro = FiltroConsumo(lista_autos)
                lista_autos = filtro.aplicar(lista_autos)
            case 8:
                filtro = FiltroCarroceria(lista_autos)
                lista_autos = filtro.aplicar(lista_autos)
            case 9:
                InterfazUsuario.mostrar_resultados(lista_autos)
            
         
