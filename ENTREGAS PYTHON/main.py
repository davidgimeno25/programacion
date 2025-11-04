from crear_equipo import crear_equipo
from listar_equipos import listar_equipos
from buscar_por_id import buscar_por_id
from actualizar_datos import actualizar_datos

equipos = []

while True:
    print("Menú:")
    print("1. Crear equipo")
    print("2. Listar equipos")
    print("3. Buscar por ID")
    print("4. Actualizar datos")
    print("5. Eliminar equipo")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        crear_equipo(equipos)

    if opcion == "2":
        listar_equipos(equipos)

    if opcion == "3":
        buscar_por_id(equipos)

    if opcion == "4":
        actualizar_datos(equipos)

    if opcion == "5":
        eliminar_equipo(equipos)
