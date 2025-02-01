class Cliente:
    """Clase para representar un cliente."""

    def __init__(self, nombre, direccion, telefono=None):
        """
        Inicializa un nuevo cliente.
        :param nombre: Nombre del cliente
        :param direccion: Dirección del cliente
        :param telefono: Número de teléfono del cliente (opcional)
        """
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono  # Número de teléfono (opcional)
        self.carrito = []

    def __str__(self):
        """Devuelve una representación amigable del cliente, incluyendo el teléfono."""
        telefono_str = f", Teléfono: {self.telefono}" if self.telefono else ""
        return f"Cliente: {self.nombre}, Dirección: {self.direccion}{telefono_str}"

    def agregar_producto(self, producto, cantidad):
        """
        Agrega un producto al carrito de compras.
        :param producto: Objeto de tipo Producto
        :param cantidad: Cantidad del producto a agregar
        """
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a cero.")
        producto.reducir_stock(cantidad)
        self.carrito.append((producto, cantidad))

    def mostrar_carrito(self):
        """Muestra los productos en el carrito."""
        if not self.carrito:
            return "El carrito está vacío."

        carrito_detalle = "Carrito de Compras:\n"
        total = 0
        for producto, cantidad in self.carrito:
            subtotal = producto.precio * cantidad
            carrito_detalle += f"- {producto.nombre}: {cantidad} x ${producto.precio:.2f} = ${subtotal:.2f}\n"
            total += subtotal

        carrito_detalle += f"Total: ${total:.2f}"
        return carrito_detalle