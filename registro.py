contador = 0

def registro_form():
    nombre = input("Ingrese el nombre de la marca: ")
    descripcion = input("Ingrese el descripcion de la marca: ")
    producto = input("Ingrese el producto/los productos de la marca: ")
    numero = input("Ingrese el numero de la marca: ")
    foto = input("Ingrese el foto del productos/s: ")
    logo = input("Ingrese el logo de la marca: ")
    video =input("Ingrese el video promocional: ")
    print("Marca registrada")
    print("Nombre de la marca: ", nombre)
    print("Descripcion: ", descripcion)
    print("Producto/s: ", producto)
    print("Numero de contacto de marca: ", numero)
    print("Foto de productos: ", foto)
    print("Logo: ", logo)
    print("Video promocional: ", video)

while True:

    opcion = input("Desea registrar una nueva marca? (S/N): ")
    if opcion == "S":
        registro_form()
        contador += 1

    elif opcion == "N":
        print("Cantidad de marcas registradas: ", contador)
        break

    else:
        print("Opcion invalida")


