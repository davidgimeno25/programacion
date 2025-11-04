def buscar_por_id(equipos):
    IDusuario = input("Escribe un ID: ")
    if IDusuario == equipos["id"]:
        print(f"ID: {equipos["id"]}")
        print(f"Nombre: {equipos["nombre"]}")
        print(f"Ciudad: {equipos["ciudad"]}")
        print(f"Estado: {"Activo" if equipos("estado") else "Inactivo"}")
