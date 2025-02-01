from abc import ABC, abstractmethod

# Clase abstracta Animal
class Animal(ABC):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @abstractmethod
    def hacer_sonido(self):
        pass

    @abstractmethod
    def moverse(self):
        pass

# Clase Perro que hereda de Animal
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Guau!")

    def moverse(self):
        print(f"{self.nombre} corre rápidamente por el parque.")

# Clase Gato que hereda de Animal
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color

    def hacer_sonido(self):
        print(f"{self.nombre} dice: ¡Miau!")

    def moverse(self):
        print(f"{self.nombre} camina de forma sigilosa por la casa.")

# Ejemplo de uso
perro = Perro("Rex", 3, "Labrador")
gato = Gato("Miau", 2, "Negro")

# Mostrar información y acciones de los animales
perro.hacer_sonido()   # Output: Rex dice: ¡Guau!
perro.moverse()         # Output: Rex corre rápidamente por el parque.

gato.hacer_sonido()    # Output: Miau dice: ¡Miau!
gato.moverse()          # Output: Miau camina de forma sigilosa por la casa.
