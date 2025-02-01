class Producto:
    """Clase para representar un producto en la tienda."""

    def __init__(self, nombre, precio, stock):
        """
        Inicializa un nuevo producto.
        :param nombre: Nombre del producto
        :param precio: Precio del producto
        :param stock: Cantidad disponible del producto
        """
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        """Devuelve una representación amigable del producto."""
        return f"Producto: {self.nombre}, Precio: ${self.precio:.2f}, Stock: {self.stock}"

    def reducir_stock(self, cantidad):
        """
        Reduce el stock del producto.
        :param cantidad: Cantidad a reducir
        """
        if cantidad > self.stock:
            raise ValueError("No hay suficiente stock disponible.")
        self.stock -= cantidad
