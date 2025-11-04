def eliminar_equipo(equipo):
    pedirID = input("Introduce el ID del equipo: ")

    for equipo in equipos:
        if pedirID == equipos["id"]:
            equipos["estado"] = False
