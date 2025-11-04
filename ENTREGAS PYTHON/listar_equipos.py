from tabulate import tabulate

def listar_equipos(equipos):
    activo = []
    for equipo in equipos:
        if equipo("estado"):
            activo.append(equipo)
        if not activo:
            print("No hay equipos activos")

    else:
        from tabulate import tabulate
        print(tabulate (activo, headers="keys", tablefmt="grid"))
