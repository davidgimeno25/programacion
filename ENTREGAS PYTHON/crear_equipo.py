from generar_id import generar_id

def crear_equipo(equipos):
    nombreEquipo = input("Escribe el nombre del equipo: ")
    ciudadEquipo = input("Escribe la ciudad del equipo: ")
    IDequipo = generar_id(equipos)

    equipo = {
        "nombre": nombreEquipo,
        "ciudad": ciudadEquipo,
        "ID": IDequipo,
        "estado": True
    }

    equipos.append(equipo)
    print("El equipo se ha creado.")
