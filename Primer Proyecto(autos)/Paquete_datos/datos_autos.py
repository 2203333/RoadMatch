from Paquete_datos.auto import *

lista_autos = [
    Auto("Toyota", 2018, "Corolla", 50000, 100000, 25000, "automatica", "urbano", "medio", "sedan"),
    Auto("Toyota", 2018, "Corolla", 50000, 100000, 25000, "automática", "urbano", "medio", "Sedán"),
    Auto("Ford", 2020, "Fiesta", 30000, 80000, 18000, "manual", "urbano", "bajo", "Hatchback"),
    Auto("Honda", 2019, "Civic", 20000, 70000, 22000, "automática", "familiar", "medio", "Sedán"),
    Auto("Chevrolet", 2021, "Cruze", 15000, 60000, 23000, "automática", "urbano", "medio", "Sedán"),
    Auto("Volkswagen", 2017, "Golf", 40000, 120000, 19500, "manual", "urbano", "bajo", "Hatchback"),
    Auto("Nissan", 2016, "Sentra", 80000, 150000, 17000, "automática", "familiar", "alto", "Sedán"),
    Auto("Hyundai", 2022, "Tucson", 10000, 50000, 32000, "automática", "todo terreno", "alto", "SUV"),
    Auto("Kia", 2020, "Sportage", 25000, 90000, 28000, "automática", "familiar", "medio", "SUV"),
    Auto("Bmw", 2019, "Serie 3", 35000, 110000, 41000, "automática", "deportivo", "muy alto", "Sedán"),
    Auto("Mercedes-Benz", 2021, "Clase C", 12000, 40000, 48000, "automática", "viajes de larga distancia", "alto", "Sedán"),
    Auto("Toyota", 2017, "RAV4", 60000, 130000, 27000, "automática", "familiar", "medio", "SUV"),
    Auto("Ford", 2018, "Ranger", 45000, 140000, 35000, "manual", "cargamento pesado", "muy alto", "Pick-up"),
    Auto("Honda", 2020, "CR-V", 22000, 75000, 31000, "automática", "todo terreno", "medio", "SUV"),
    Auto("Chevrolet", 2015, "Camaro", 70000, 160000, 42000, "manual", "deportivo", "muy alto", "Coupé"),
    Auto("Volkswagen", 2022, "Tiguan", 5000, 30000, 38000, "automática", "familiar", "alto", "SUV"),
    Auto("Nissan", 2019, "Qashqai", 30000, 85000, 26000, "automática", "urbano", "medio", "SUV"),
    Auto("Hyundai", 2018, "Santa Fe", 35000, 95000, 29000, "automática", "familiar", "alto", "SUV"),
    Auto("Kia", 2021, "Sorento", 18000, 65000, 34000, "automática", "viajes de larga distancia", "medio", "SUV"),
    Auto("Bmw", 2020, "X5", 25000, 80000, 67000, "automática", "todo terreno", "muy alto", "SUV"),
    Auto("Mercedes-Benz", 2016, "GLC", 55000, 135000, 44000, "automática", "familiar", "alto", "SUV"),
    Auto("Toyota", 2021, "Hilux", 40000, 145000, 39000, "manual", "cargamento pesado", "muy alto", "Pick-up"),
    Auto("Ford", 2019, "Explorer", 28000, 92000, 36000, "automática", "familiar", "alto", "SUV"),
    Auto("Honda", 2017, "Pilot", 65000, 150000, 33000, "automática", "viajes de larga distancia", "alto", "SUV"),
    Auto("Chevrolet", 2022, "Equinox", 15000, 60000, 27000, "automática", "urbano", "medio", "SUV"),
    Auto("Volkswagen", 2018, "Jetta", 38000, 110000, 21000, "automática", "urbano", "bajo", "Sedán"),
    Auto("Nissan", 2020, "Altima", 22000, 78000, 24000, "automática", "familiar", "medio", "Sedán"),
    Auto("Hyundai", 2016, "Elantra", 70000, 160000, 16500, "manual", "urbano", "bajo", "Sedán"),
    Auto("Kia", 2022, "Rio", 8000, 40000, 18500, "manual", "urbano", "muy bajo", "Hatchback"),
    Auto("BMW", 2021, "X3", 12000, 45000, 55000, "automática", "todo terreno", "alto", "SUV"),
    Auto("Mercedes-Benz", 2017, "Sprinter", 90000, 180000, 52000, "manual", "cargamento pesado", "muy alto", "Minivan"),
    Auto("Toyota", 2019, "Camry", 30000, 90000, 28000, "automática", "familiar", "medio", "Sedán"),
    Auto("Ford", 2016, "Focus", 85000, 170000, 14500, "manual", "urbano", "bajo", "Hatchback"),
    Auto("Honda", 2021, "HR-V", 10000, 50000, 25500, "automática", "urbano", "medio", "SUV"),
    Auto("Chevrolet", 2018, "Malibu", 42000, 125000, 22500, "automática", "familiar", "medio", "Sedán"),
    Auto("Volkswagen", 2020, "Polo", 20000, 70000, 17500, "manual", "urbano", "muy bajo", "Hatchback"),
    Auto("Nissan", 2015, "X-Trail", 95000, 190000, 20000, "automática", "todo terreno", "alto", "SUV"),
    Auto("Hyundai", 2022, "Kona", 5000, 35000, 23000, "automática", "urbano", "bajo", "SUV"),
    Auto("Kia", 2019, "Picanto", 35000, 100000, 12500, "manual", "urbano", "muy bajo", "Hatchback"),
    Auto("Bmw", 2018, "Serie 5", 60000, 140000, 48000, "automática", "deportivo", "muy alto", "Sedán"),
    Auto("Mercedes-Benz", 2020, "Clase A", 25000, 75000, 37000, "automática", "urbano", "alto", "Hatchback"),
    Auto("Toyota", 2022, "Prius", 7000, 30000, 32000, "automática", "urbano", "muy bajo", "Sedán"),
    Auto("Ford", 2017, "Mustang", 50000, 130000, 45000, "manual", "deportivo", "muy alto", "Coupé"),
    Auto("Honda", 2016, "Accord", 75000, 155000, 19500, "automática", "familiar", "medio", "Sedán"),
    Auto("Chevrolet", 2020, "Silverado", 30000, 100000, 41000, "automática", "cargamento pesado", "muy alto", "Pick-up"),
    Auto("Volkswagen", 2019, "Amarok", 40000, 120000, 43000, "manual", "todo terreno", "muy alto", "Pick-up"),
    Auto("Nissan", 2021, "Frontier", 22000, 85000, 38000, "automática", "cargamento pesado", "alto", "Pick-up"),
    Auto("Hyundai", 2017, "Creta", 55000, 135000, 21000, "automática", "urbano", "medio", "SUV"),
    Auto("Kia", 2018, "Stonic", 32000, 95000, 19500, "automática", "urbano", "bajo", "SUV"),
    Auto("Bmw", 2022, "Serie 1", 15000, 50000, 36000, "manual", "deportivo", "alto", "Hatchback"),
    Auto("Mercedes-Benz", 2019, "GLE", 28000, 88000, 62000, "automática", "todo terreno", "muy alto", "SUV"),
    Auto("Toyota", 2020, "RAV4", 18000, 65000, 34000, "automática", "familiar", "medio", "SUV"),
    Auto("Ford", 2021, "Explorer", 12000, 45000, 39000, "automática", "viajes de larga distancia", "alto", "SUV")
]