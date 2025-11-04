def actualizar_datos(equipos):
    pedirID = opcion(input("Escribe el ID del equipo: "))

    for equipo in equipos:
        if pedirID == equipos["id"]:
            nuevoNombre = input("Introduce el nuevo nombre del equipo: ")
            nuevaCiudad = input("Introduce la nueva ciudad del equipo: ")

            equipo["nombre"] = nuevoNombre
            equipo["ciudad"] = nuevaCiudad

            print("Los datos del equipo se han actualizado.")

        print(f"ID: {equipos["ID"]}")
        print(f"Nombre: {equipos["nombre"]}")
        print(f"Ciudad: {equipos["ciudad"]}")
        print(f"Estado: {"Activo" if equipos("estado") else "Inactivo"}")

    else:
        print("No hay ningún equipo con ese ID. Inténtalo de nuevo.")
