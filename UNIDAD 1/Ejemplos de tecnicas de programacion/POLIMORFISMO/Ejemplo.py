class Producto:
    def __init__(self, nombre, precio_base):
        self.nombre = nombre
        self.precio_base = precio_base

    # Método que debe ser sobrescrito por las subclases
    def calcular_precio(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las subclases.")

# Clase derivada (subclase) Producto Digital
class ProductoDigital(Producto):
    def __init__(self, nombre, precio_base, impuesto=0):
        super().__init__(nombre, precio_base)
        self.impuesto = impuesto

    # Sobrescribimos el método calcular_precio para productos digitales
    def calcular_precio(self):
        return self.precio_base * (1 + self.impuesto)

# Clase derivada (subclase) Producto Físico
class ProductoFisico(Producto):
    def __init__(self, nombre, precio_base, costo_envio):
        super().__init__(nombre, precio_base)
        self.costo_envio = costo_envio

    # Sobrescribimos el método calcular_precio para productos físicos
    def calcular_precio(self):
        return self.precio_base + self.costo_envio

# Ejemplo de uso
productos = [
    ProductoDigital("Curso Python", 100, 0.18),   # Producto Digital con 18% de impuesto
    ProductoFisico("Laptop", 1000, 50)             # Producto Físico con costo de envío
]

# Polimorfismo en acción
for producto in productos:
    print(f"El precio final del {producto.nombre} es: {producto.calcular_precio()} USD")
