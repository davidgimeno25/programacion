# Definir variables
articulos = []
usuarios = []

# Definir funciones
def leerTexto(mensaje):
    texto = input(mensaje)
    while texto == "":
        print("Error: no puede estar vacío.")
        texto = input(mensaje)
    return texto

def leerEntero(mensaje, minimo):
    while True:
        texto = input(mensaje)
        try:
            valorNumero = int(texto)
            if valorNumero >= minimo:
                return valorNumero
            else:
                print(f"Error: El número debe ser {minimo} o mayor.")
        except ValueError:
            print("Error: Ingrese un número entero válido.")

def leerFloat(mensaje, minimo):
    while True:
        texto = input(mensaje)
        try:
            valorNumero = float(texto)
            if valorNumero > minimo:
                return valorNumero
            else:
                print(f"Error: El número debe ser mayor que {minimo}.")
        except ValueError:
            print("Error: Ingrese un número decimal válido. Use un punto para los decimales.")

def leerEmail(mensaje):
    while True:
        email = input(mensaje)
        if email == "":
            print("Error, no puede estar vacío.")
        elif "@" in email and "." in email:
            return email
        else:
            print("Error: Introduce una dirección de email.")

def generar_id(articulos_lista):
    if len(articulos_lista) == 0:
        return 1
    id_mas_alto = 0
    for articulo in articulos_lista:
        if articulo["id"] > id_mas_alto:
            id_mas_alto = articulo["id"]
    return id_mas_alto + 1

def crearArticulo():
    nombre = leerTexto("Nombre: ")
    precio = leerFloat("Precio (>0): ", 0)
    stock = leerEntero("Stock (>=0): ", 0)
    nuevoID = generar_id(articulos)
    articulo = {
        "id": nuevoID,
        "nombre": nombre,
        "precio": precio,
        "stock": stock,
        "activo": True
    }
    articulos.append(articulo)
    print("Artículo creado correctamente.")

def crearUsuario():
    print("1. Crear usuario")
    nombre = leerTexto("Nombre: ")
    email = leerEmail("Email: ")
    nuevoID = generar_id(usuarios)
    usuario = {
        "id": nuevoID,
        "nombre": nombre,
        "email": email,
        "activo": True
    }
    usuarios.append(usuario)
    print("Usuario creado.")

def listarUsuarios():
    print("2. Listar usuarios")
    if len(usuarios) == 0:
        print("No hay usuarios registrados.")
        return
    print("1. Activos, 2. Inactivos, 3. Todos")
    opcion = leerEntero("Elige una opción (1-3): ", 1)
    while opcion > 3:
        print("Opción inválida.")
        opcion = leerEntero("Elige una opción (1-3): ", 1)
    print("Listado:")
    encontrados = 0
    for usuario in usuarios:
        mostrar = False
        if opcion == 1 and usuario["activo"]:
            mostrar = True
        elif opcion == 2 and not usuario["activo"]:
            mostrar = True
        elif opcion == 3:
            mostrar = True
        if mostrar:
            estado = "Activo" if usuario["activo"] else "Inactivo"
            print(f"ID: {usuario['id']}, Nombre: {usuario['nombre']}, Email: {usuario['email']}, Estado: {estado}")
            encontrados += 1
    if encontrados == 0:
        print("No se encontraron usuarios con ese filtro.")
    else:
        print()

def listarArticulos():
    print("2. Listar artículos")
    if len(articulos) == 0:
        print("No hay artículos registrados.")
        return
    print("1. Activos, 2. Inactivos, 3. Todos")
    opcion = leerEntero("Elige una opción (1-3): ", 1)
    while opcion > 3:
        print("Opción inválida.")
        opcion = leerEntero("Elige una opción (1-3): ", 1)
    print("Listado:")
    encontrados = 0
    for articulo in articulos:
        mostrar = False
        if opcion == 1 and articulo["activo"]:
            mostrar = True
        elif opcion == 2 and not articulo["activo"]:
            mostrar = True
        elif opcion == 3:
            mostrar = True
        if mostrar:
            estado = "Activo" if articulo["activo"] else "Inactivo"
            print(f"ID: {articulo['id']}, Nombre: {articulo['nombre']}, Precio: {articulo['precio']}, Stock: {articulo['stock']}, Estado: {estado}")
            encontrados += 1
    if encontrados == 0:
        print("No se encontraron artículos con ese filtro.")
    else:
        print()

def buscarArticulo():
    print("3. Buscar artículo por ID")
    id_buscar = leerEntero("Ingrese el ID: ", 1)
    encontrado = False
    for articulo in articulos:
        if articulo["id"] == id_buscar:
            encontrado = articulo
    if encontrado:
        estado = "Activo" if encontrado["activo"] else "Inactivo"
        print(f"ID: {encontrado['id']}, Nombre: {encontrado['nombre']}, Precio: {encontrado['precio']}, Stock: {encontrado['stock']}, Estado: {estado}")
    else:
        print("No se encontró ningún artículo con ese ID.")

def buscarUsuario():
    print("3. Buscar usuario por ID")
    id_buscar = leerEntero("Ingrese el ID: ", 1)
    encontrado = False
    for usuario in usuarios:
        if usuario["id"] == id_buscar:
            encontrado = usuario
    if encontrado:
        estado = "Activo" if encontrado["activo"] else "Inactivo"
        print(f"ID: {encontrado['id']}, Nombre: {encontrado['nombre']}, Email: {encontrado['email']}, Estado: {estado}")
    else:
        print("No se encontró ningun usuario con ese ID.")

def actualizarArticulo():
    print("4. Actualizar artículo")
    id_buscar = leerEntero("Ingrese el ID: ", 1)
    encontrado = False
    for articulo in articulos:
        if articulo["id"] == id_buscar:
            encontrado = articulo
    if encontrado:
        print("Actualizando", encontrado["nombre"])
        nuevo_nombre = leerTexto("Nuevo nombre: ")
        nuevo_precio = leerFloat("Nuevo precio (>0): ", 0)
        nuevo_stock = leerEntero("Nuevo stock (>=0): ", 0)
        encontrado["nombre"] = nuevo_nombre
        encontrado["precio"] = nuevo_precio
        encontrado["stock"] = nuevo_stock
        print("Artículo actualizado.")
    else:
        print("No se encontró ningún artículo con ese ID.")

def actualizarUsuario():
    print("4. Actualizar usuario")
    id_buscar = leerEntero("Ingrese el ID:", 1)
    encontrado = False
    for usuario in usuarios:
        if usuario["id"] == id_buscar:
            encontrado = usuario
    if encontrado:
        print("Actualizando", encontrado["nombre"])
        nuevo_nombre = leerTexto("Nuevo nombre: ")
        nuevo_email = leerEmail("Nuevo email: ")
        encontrado["nombre"] = nuevo_nombre
        encontrado["email"] = nuevo_email
        print("Usuario actualizado.")
    else:
        print("No se encontró ningun usuario con ese ID")

def eliminarArticulo():
    print("5. Eliminar artículo")
    idbuscar = leerEntero("Ingrese el ID: ", 1)
    indice = -1
    for i in range(len(articulos)):
        if articulos[i]["id"] == idbuscar:
            indice = i
    if indice != -1:
        confirmar = leerTexto("¿Seguro que desea eliminarlo? (si/no): ")
        if confirmar == "si":
            articulos.pop(indice)
            print("Artículo eliminado.")
        else:
            print("Operación cancelada.")
    else:
        print("No se encontró ningún artículo con ese ID.")

def eliminarUsuario():
    print("5. Eliminar usuario")
    idbuscar = leerEntero("Ingrese el ID: ", 1)
    indice = -1
    for i in range(len(usuarios)):
        if usuarios[i]["id"] == idbuscar:
            indice = i
    if indice != -1:
        confirmar = leerTexto("¿Seguro que desea eliminarlo? (si/no): ")
        if confirmar == "si":
            usuarios.pop(indice)
            print("Usuario eliminado.")
        else:
            print("Operación cancelada.")
    else:
        print("No se encontró ningún usuario con ese ID.")

def alternarActivo():
    print("6. Alternar activo/inactivo")
    id_buscar = leerEntero("Ingrese el ID: ", 1)
    encontrado = False
    for articulo in articulos:
        if articulo["id"] == id_buscar:
            encontrado = articulo
    if encontrado:
        if encontrado["activo"]:
            encontrado["activo"] = False
            print("Ahora está inactivo.")
        else:
            encontrado["activo"] = True
            print("Ahora está activo.")
    else:
        print("No se encontró ningún artículo con ese ID.")

def alternarActivoUsuario():
    print("6. Alternar activo/inactivo")
    id_buscar = leerEntero("Ingrese el ID: ", 1)
    encontrado = False
    for usuario in usuarios:
        if usuario["id"] == id_buscar:
            encontrado = usuario
    if encontrado:
        if encontrado["activo"]:
            encontrado["activo"] = False
            print("Ahora está inactivo.")
        else:
            encontrado["activo"] = True
            print("Ahora está activo.")
    else:
        print("No se encontró ningún usuario con ese ID.")

# MENÚS
def mostrarMenu():
    print("MENÚ:")
    print("1. Crear artículo")
    print("2. Listar artículos")
    print("3. Buscar artículo por ID")
    print("4. Actualizar artículo")
    print("5. Eliminar artículo")
    print("6. Alternar activo/inactivo")
    print("7. Salir")

def articulo_mostrarMenu():
    print("Menú de artículos: ")
    print("1. Crear artículo")
    print("2. Listar artículos")
    print("3. Buscar artículo por ID")
    print("4. Actualizar artículo")
    print("5. Eliminar artículo")
    print("6. Alternar activo/inactivo")
    print("7. Volver al menú")

def menu_articulos():
    menu_articulos_activo = True
    while menu_articulos_activo:
        articulo_mostrarMenu()
        opcion = leerEntero("Elige una opción (1-7):", 1)
        while opcion < 1 or opcion > 7:
            print("Opción no válida.")
            opcion = leerEntero("Elige una opción (1-7): ", 1)
        if opcion == 1:
            crearArticulo()
        elif opcion == 2:
            listarArticulos()
        elif opcion == 3:
            buscarArticulo()
        elif opcion == 4:
            actualizarArticulo()
        elif opcion == 5:
            eliminarArticulo()
        elif opcion == 6:
            alternarActivo()
        elif opcion == 7:
            menu_articulos_activo = False

def usr_mostrarMenu():
    print("Menú de usuarios:")
    print("1. Crear usuario")
    print("2. Listar usuarios")
    print("3. Buscar usuario por ID")
    print("4. Actualizar usuario")
    print("5. Eliminar usuario")
    print("6. Alternar activo/inactivo")
    print("7. Volver al menú principal")

def menu_usr():
    menu_usr_activo = True
    while menu_usr_activo:
        usr_mostrarMenu()
        opcion = leerEntero("Elige una opción (1-7): ", 1)
        while opcion < 1 or opcion > 7:
            print("Opción no válida.")
            opcion = leerEntero("Elige una opción (1-7): ", 1)
        if opcion == 1:
            crearUsuario()
        elif opcion == 2:
            listarUsuarios()
        elif opcion == 3:
            buscarUsuario()
        elif opcion == 4:
            actualizarUsuario()
        elif opcion == 5:
            eliminarUsuario()
        elif opcion == 6:
            alternarActivoUsuario()
        elif opcion == 7:
            menu_usr_activo = False

def mostrar_menu_principal():
    print("Menú de la TIENDA ONLINE:")
    print("1. Gestionar Artículos")
    print("2. Gestionar Usuarios")
    print("3. Salir")

menuActivo = True
while menuActivo:
    mostrar_menu_principal()
    opcion = leerEntero("Elige una opción (1-3): ", 1)
    while opcion < 1 or opcion > 3:
        print("Opción inválida.")
        opcion = leerEntero("Elige una opción (1-3): ", 1)
    if opcion == 1:
        menu_articulos()
    elif opcion == 2:
        menu_usr()
    elif opcion == 3:
        menuActivo = False
        print("Saliendo del programa... ¡Hasta luego!")
