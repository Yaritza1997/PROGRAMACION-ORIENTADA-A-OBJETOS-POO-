from producto import Producto
from cliente import Cliente

def main():
    print("BIENVENIDOS A MI TIENDA ONLINE LILISTORE .")

    # Crear productos
    laptop = Producto("Laptop", 1000, 10)
    mouse = Producto("Mouse", 20, 50)
    teclado = Producto("Teclado", 30, 25)
    impresora = Producto("Impresora", 350, 25)

    # Mostrar productos
    print("\nProductos disponibles:")
    print(laptop)
    print(mouse)
    print(teclado)
    print(impresora)

    # Crear cliente con teléfono
    cliente1 = Cliente("Yaritza Arboleda", "Esmeraldas", "0981898227")
    print("\n" + str(cliente1))

    # Cliente agrega productos al carrito
    print("\nAgregando productos al carrito...")
    cliente1.agregar_producto(laptop, 2)  # Compra 2 Laptop
    cliente1.agregar_producto(mouse, 2)  # Compra 2 Mouses
    cliente1.agregar_producto(teclado, 1)  # Compra 1 Teclado
    cliente1.agregar_producto(impresora, 1)  # Compra 1 Impresora

    # Mostrar carrito
    print("\n" + cliente1.mostrar_carrito())

if __name__ == "__main__":
    main()