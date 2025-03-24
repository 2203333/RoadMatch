import mysql.connector
from .auto import *

conexion = mysql.connector.connect(
    host='127.0.0.1',         
    user="root",        
    password="Mysqlemma", 
    database="roadmatch" 
)
cursor = conexion.cursor()
sql = """
INSERT INTO autos (marca, año, modelo, min_km, max_km, minimo_precio, transmicion, uso, consumo, tamaño)
VALUES (%(marca)s, %(año)s, %(modelo)s, %(min_km)s, %(max_km)s, %(minimo_precio)s, %(transmicion)s, %(uso)s, %(consumo)s, %(tamaño)s)
"""
lista_autos = [
    {"marca": "Toyota", "año": 2018, "modelo": "Corolla", "min_km": 50000, "max_km": 100000, "minimo_precio": 25000, "transmicion": "automatica", "uso": "urbano", "consumo": "medio", "tamaño": "sedan"},
    {"marca": "Toyota", "año": 2018, "modelo": "Corolla", "min_km": 50000, "max_km": 100000, "minimo_precio": 25000, "transmicion": "automática", "uso": "urbano", "consumo": "medio", "tamaño": "Sedán"},
    {"marca": "Ford", "año": 2020, "modelo": "Fiesta", "min_km": 30000, "max_km": 80000, "minimo_precio": 18000, "transmicion": "manual", "uso": "urbano", "consumo": "bajo", "tamaño": "Hatchback"},
    {"marca": "Honda", "año": 2019, "modelo": "Civic", "min_km": 20000, "max_km": 70000, "minimo_precio": 22000, "transmicion": "automática", "uso": "familiar", "consumo": "medio", "tamaño": "Sedán"},
    {"marca": "Chevrolet", "año": 2021, "modelo": "Cruze", "min_km": 15000, "max_km": 60000, "minimo_precio": 23000, "transmicion": "automática", "uso": "urbano", "consumo": "medio", "tamaño": "Sedán"},
    {"marca": "Volkswagen", "año": 2017, "modelo": "Golf", "min_km": 40000, "max_km": 120000, "minimo_precio": 19500, "transmicion": "manual", "uso": "urbano", "consumo": "bajo", "tamaño": "Hatchback"},
    {"marca": "Nissan", "año": 2016, "modelo": "Sentra", "min_km": 80000, "max_km": 150000, "minimo_precio": 17000, "transmicion": "automática", "uso": "familiar", "consumo": "alto", "tamaño": "Sedán"},
    {"marca": "Hyundai", "año": 2022, "modelo": "Tucson", "min_km": 10000, "max_km": 50000, "minimo_precio": 32000, "transmicion": "automática", "uso": "todo terreno", "consumo": "alto", "tamaño": "SUV"},
    {"marca": "Kia", "año": 2020, "modelo": "Sportage", "min_km": 25000, "max_km": 90000, "minimo_precio": 28000, "transmicion": "automática", "uso": "familiar", "consumo": "medio", "tamaño": "SUV"},
    {"marca": "Bmw", "año": 2019, "modelo": "Serie 3", "min_km": 35000, "max_km": 110000, "minimo_precio": 41000, "transmicion": "automática", "uso": "deportivo", "consumo": "muy alto", "tamaño": "Sedán"},
    {"marca": "Mercedes-Benz", "año": 2021, "modelo": "Clase C", "min_km": 12000, "max_km": 40000, "minimo_precio": 48000, "transmicion": "automática", "uso": "viajes de larga distancia", "consumo": "alto", "tamaño": "Sedán"},
    {"marca": "Toyota", "año": 2017, "modelo": "RAV4", "min_km": 60000, "max_km": 130000, "minimo_precio": 27000, "transmicion": "automática", "uso": "familiar", "consumo": "medio", "tamaño": "SUV"},
    {"marca": "Ford", "año": 2018, "modelo": "Ranger", "min_km": 45000, "max_km": 140000, "minimo_precio": 35000, "transmicion": "manual", "uso": "cargamento pesado", "consumo": "muy alto", "tamaño": "Pick-up"},
    {"marca": "Honda", "año": 2020, "modelo": "CR-V", "min_km": 22000, "max_km": 75000, "minimo_precio": 31000, "transmicion": "automática", "uso": "todo terreno", "consumo": "medio", "tamaño": "SUV"},
    {"marca": "Chevrolet", "año": 2015, "modelo": "Camaro", "min_km": 70000, "max_km": 160000, "minimo_precio": 42000, "transmicion": "manual", "uso": "deportivo", "consumo": "muy alto", "tamaño": "Coupé"},
    {"marca": "Volkswagen", "año": 2022, "modelo": "Tiguan", "min_km": 5000, "max_km": 30000, "minimo_precio": 38000, "transmicion": "automática", "uso": "familiar", "consumo": "alto", "tamaño": "SUV"},
    {"marca": "Nissan", "año": 2019, "modelo": "Qashqai", "min_km": 30000, "max_km": 85000, "minimo_precio": 26000, "transmicion": "automática", "uso": "urbano", "consumo": "medio", "tamaño": "SUV"},
    {"marca": "Hyundai", "año": 2018, "modelo": "Santa Fe", "min_km": 35000, "max_km": 95000, "minimo_precio": 29000, "transmicion": "automática", "uso": "familiar", "consumo": "alto", "tamaño": "SUV"},
    {"marca": "Kia", "año": 2021, "modelo": "Sorento", "min_km": 18000, "max_km": 65000, "minimo_precio": 34000, "transmicion": "automática", "uso": "viajes de larga distancia", "consumo": "medio", "tamaño": "SUV"},
    {"marca": "Bmw", "año": 2020, "modelo": "X5", "min_km": 25000, "max_km": 80000, "minimo_precio": 67000, "transmicion": "automática", "uso": "todo terreno", "consumo": "muy alto", "tamaño": "SUV"},
    {"marca": "Mercedes-Benz", "año": 2016, "modelo": "GLC", "min_km": 55000, "max_km": 135000, "minimo_precio": 44000, "transmicion": "automática", "uso": "familiar", "consumo": "alto", "tamaño": "SUV"},
    {"marca": "Toyota", "año": 2021, "modelo": "Hilux", "min_km": 40000, "max_km": 145000, "minimo_precio": 39000, "transmicion": "manual", "uso": "cargamento pesado", "consumo": "muy alto", "tamaño": "Pick-up"},
    {"marca": "Ford", "año": 2019, "modelo": "Explorer", "min_km": 28000, "max_km": 92000, "minimo_precio": 36000, "transmicion": "automática", "uso": "familiar", "consumo": "alto", "tamaño": "SUV"},
    {"marca": "Honda", "año": 2017, "modelo": "Pilot", "min_km": 65000, "max_km": 150000, "minimo_precio": 33000, "transmicion": "automática", "uso": "viajes de larga distancia", "consumo": "alto", "tamaño": "SUV"},
    {"marca": "Chevrolet", "año": 2022, "modelo": "Equinox", "min_km": 15000, "max_km": 60000, "minimo_precio": 27000, "transmicion": "automática", "uso": "urbano", "consumo": "medio", "tamaño": "SUV"},
    {"marca": "Volkswagen", "año": 2018, "modelo": "Jetta", "min_km": 38000, "max_km": 110000, "minimo_precio": 21000, "transmicion": "automática", "uso": "urbano", "consumo": "bajo", "tamaño": "Sedán"},
    {"marca": "Nissan", "año": 2020, "modelo": "Altima", "min_km": 22000, "max_km": 78000, "minimo_precio": 24000, "transmicion": "automática", "uso": "familiar", "consumo": "medio", "tamaño": "Sedán"},
    {"marca": "Hyundai", "año": 2016, "modelo": "Elantra", "min_km": 70000, "max_km": 160000, "minimo_precio": 16500, "transmicion": "manual", "uso": "urbano", "consumo": "bajo", "tamaño": "Sedán"},
    {"marca": "Kia", "año": 2022, "modelo": "Rio", "min_km": 8000, "max_km": 40000, "minimo_precio": 18500, "transmicion": "manual", "uso": "urbano", "consumo": "muy bajo", "tamaño": "Hatchback"},
    {"marca": "BMW", "año": 2021, "modelo": "X3", "min_km": 12000, "max_km": 45000, "minimo_precio": 55000, "transmicion": "automática", "uso": "todo terreno", "consumo": "alto", "tamaño": "SUV"},
    {"marca": "Mercedes-Benz", "año": 2017, "modelo": "Sprinter", "min_km": 90000, "max_km": 180000, "minimo_precio": 52000, "transmicion": "manual", "uso": "cargamento pesado", "consumo": "muy alto", "tamaño": "Minivan"},
    {"marca": "Toyota", "año": 2019, "modelo": "Camry", "min_km": 30000, "max_km": 90000, "minimo_precio": 28000, "transmicion": "automática", "uso": "familiar", "consumo": "medio", "tamaño": "Sedán"},
    {"marca": "Ford", "año": 2016, "modelo": "Focus", "min_km": 85000, "max_km": 170000, "minimo_precio": 14500, "transmicion": "manual", "uso": "urbano", "consumo": "bajo", "tamaño": "Hatchback"},
    {"marca": "Honda", "año": 2021, "modelo": "HR-V", "min_km": 10000, "max_km": 50000, "minimo_precio": 25500, "transmicion": "automática", "uso": "urbano", "consumo": "medio", "tamaño": "SUV"},
    {"marca": "Chevrolet", "año": 2018, "modelo": "Malibu", "min_km": 42000, "max_km": 125000, "minimo_precio": 22500, "transmicion": "automática", "uso": "familiar", "consumo": "medio", "tamaño": "Sedán"},
    {"marca": "Volkswagen", "año": 2020, "modelo": "Polo", "min_km": 20000, "max_km": 70000, "minimo_precio": 17500, "transmicion": "manual", "uso": "urbano", "consumo": "muy bajo", "tamaño": "Hatchback"},
    {"marca": "Nissan", "año": 2015, "modelo": "X-Trail", "min_km": 95000, "max_km": 190000, "minimo_precio": 20000, "transmicion": "automática", "uso": "todo terreno", "consumo": "alto", "tamaño": "SUV"},
    {"marca": "Hyundai", "año": 2022, "modelo": "Kona", "min_km": 5000, "max_km": 35000, "minimo_precio": 23000, "transmicion": "automática", "uso": "urbano", "consumo": "bajo", "tamaño": "SUV"},
    {"marca": "Kia", "año": 2019, "modelo": "Picanto", "min_km": 35000, "max_km": 100000, "minimo_precio": 12500, "transmicion": "manual", "uso": "urbano", "consumo": "muy bajo", "tamaño": "Hatchback"},
    {"marca": "Bmw", "año": 2018, "modelo": "Serie 5", "min_km": 60000, "max_km": 140000, "minimo_precio": 48000, "transmicion": "automática", "uso": "deportivo", "consumo": "muy alto", "tamaño": "Sedán"},
    {"marca": "Mercedes-Benz", "año": 2020, "modelo": "Clase A", "min_km": 25000, "max_km": 75000, "minimo_precio": 37000, "transmicion": "automática", "uso": "urbano", "consumo": "alto", "tamaño": "Hatchback"},
    {"marca": "Toyota", "año": 2022, "modelo": "Prius", "min_km": 7000, "max_km": 30000, "minimo_precio": 32000, "transmicion": "automática", "uso": "urbano", "consumo": "muy bajo", "tamaño": "Sedán"},
    {"marca": "Ford", "año": 2017, "modelo": "Mustang", "min_km": 50000, "max_km": 130000, "minimo_precio": 45000, "transmicion": "manual", "uso": "deportivo", "consumo": "muy alto", "tamaño": "Coupé"},
    {"marca": "Honda", "año": 2016, "modelo": "Accord", "min_km": 75000, "max_km": 155000, "minimo_precio": 19500, "transmicion": "automática", "uso": "familiar", "consumo": "medio", "tamaño": "Sedán"},
    {"marca": "Chevrolet", "año": 2020, "modelo": "Silverado", "min_km": 30000, "max_km": 100000, "minimo_precio": 41000, "transmicion": "automática", "uso": "cargamento pesado", "consumo": "muy alto", "tamaño": "Pick-up"},
    {"marca": "Volkswagen", "año": 2019, "modelo": "Amarok", "min_km": 40000, "max_km": 120000, "minimo_precio": 43000, "transmicion": "manual", "uso": "todo terreno", "consumo": "muy alto", "tamaño": "Pick-up"},
    {"marca": "Nissan", "año": 2021, "modelo": "Frontier", "min_km": 22000, "max_km": 85000, "minimo_precio": 38000, "transmicion": "automática", "uso": "cargamento pesado", "consumo": "alto", "tamaño": "Pick-up"},
    {"marca": "Hyundai", "año": 2017, "modelo": "Creta", "min_km": 55000, "max_km": 135000, "minimo_precio": 21000, "transmicion": "automática", "uso": "urbano", "consumo": "medio", "tamaño": "SUV"},
    {"marca": "Kia", "año": 2018, "modelo": "Stonic", "min_km": 32000, "max_km": 95000, "minimo_precio": 19500, "transmicion": "automática", "uso": "urbano", "consumo": "bajo", "tamaño": "SUV"},
    {"marca": "Bmw", "año": 2022, "modelo": "Serie 1", "min_km": 15000, "max_km": 50000, "minimo_precio": 36000, "transmicion": "manual", "uso": "deportivo", "consumo": "alto", "tamaño": "Hatchback"},
    {"marca": "Mercedes-Benz", "año": 2019, "modelo": "GLE", "min_km": 28000, "max_km": 88000, "minimo_precio": 62000, "transmicion": "automática", "uso": "todo terreno", "consumo": "muy alto", "tamaño": "SUV"},
    {"marca": "Toyota", "año": 2020, "modelo": "RAV4", "min_km": 18000, "max_km": 65000, "minimo_precio": 34000, "transmicion": "automática", "uso": "familiar", "consumo": "medio", "tamaño": "SUV"},
    {"marca": "Ford", "año": 2021, "modelo": "Explorer", "min_km": 12000, "max_km": 45000, "minimo_precio": 39000, "transmicion": "automática", "uso": "viajes de larga distancia", "consumo": "alto", "tamaño": "SUV"}
]
cursor.executemany(sql, lista_autos)
conexion.commit()
cursor.close()
conexion.close()


