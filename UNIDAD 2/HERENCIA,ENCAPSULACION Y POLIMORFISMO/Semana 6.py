#Clase base: Dispositivo
class Dispositivo:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    # Método para mostrar la información básica del dispositivo
    def mostrar_informacion(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Precio: ${self.precio}"

    # Método para encender el dispositivo
    def encender(self):
        return f"El dispositivo {self.modelo} está encendido."


# Clase derivada: Televisor (herencia de Dispositivo)
class Televisor(Dispositivo):
    def __init__(self, marca, modelo, precio, tamaño_pantalla, resolucion):
        super().__init__(marca, modelo, precio)  # Llamada al constructor de la clase base
        self.__tamaño_pantalla = tamaño_pantalla  # Atributo encapsulado
        self.resolucion = resolucion

    # Método para acceder al atributo encapsulado
    def obtener_tamaño_pantalla(self):
        return self.__tamaño_pantalla

    # Sobrescribir el método encender (polimorfismo)
    def encender(self):
        return f"El televisor {self.modelo} de {self.__tamaño_pantalla} pulgadas está encendido y mostrando una imagen a {self.resolucion}."

    # Método adicional para calcular el descuento basado en un porcentaje
    def calcular_descuento(self, porcentaje_descuento):
        return self.precio * (1 - porcentaje_descuento / 100)


# Ejemplo de uso
if __name__ == "__main__":
    # Crear una instancia de la clase base Dispositivo
    dispositivo = Dispositivo("LG", "Model X", 300)
    print(dispositivo.mostrar_informacion())
    print(dispositivo.encender())

    # Crear una instancia de la clase derivada Televisor
    televisor = Televisor("Samsung", "QLED 55", 1200, 55, "4K")
    print(televisor.mostrar_informacion())
    print(televisor.encender())  # Polimorfismo: el televisor tiene un comportamiento específico al encenderse
    print(f"Tamaño de pantalla: {televisor.obtener_tamaño_pantalla()} pulgadas")
    print(f"Precio con descuento (15%): ${televisor.calcular_descuento(15):.2f}")