class Cafeteria:
    def __init__(self, nombre, ubicacion, menu):
        """
        Constructor de la clase Cafeteria.
        Inicializa los atributos de la cafetería, como el nombre, la ubicación
        y el menú disponible en la cafetería.
        """
        self.nombre = nombre  # Nombre de la cafetería
        self.ubicacion = ubicacion  # Ubicación de la cafetería
        self.menu = menu  # Lista de productos del menú
        print(f"Bienvenidos a mi cafetería {self.nombre} en {self.ubicacion}.")

    def agregar_plato(self, plato):
        """
        Método para agregar un plato al menú de la cafetería.
        """
        self.menu.append(plato)
        print(f"Plato '{plato}' agregado al menú de la cafetería {self.nombre}.")

    def listar_menu(self):
        """
        Método para mostrar los platos disponibles en el menú de la cafetería.
        """
        print(f"Menú de la cafetería {self.nombre}:")
        for plato in self.menu:
            print(f"- {plato}")

    def __del__(self):
        """
        Destructor de la clase Cafeteria.
        Este método se llama cuando el objeto Cafeteria es destruido o cuando
        el programa termina.
        Realiza tareas de limpieza, como cerrar conexiones o liberar recursos.
        """
        print(f"La cafetería {self.nombre} en {self.ubicacion} ha sido cerrada.")


class Restaurante(Cafeteria):
    def __init__(self, nombre, ubicacion, menu, tipo_cocina):
        """
        Constructor de la clase Restaurante.
        Inicializa los atributos del restaurante, incluidos los atributos de la clase Cafeteria.
        """
        super().__init__(nombre, ubicacion, menu)  # Llamamos al constructor de la clase base Cafeteria
        self.tipo_cocina = tipo_cocina  # Tipo de cocina del restaurante
        print(f"El restaurante {self.nombre} ofrece {self.tipo_cocina}.")

    def agregar_plato_restaurante(self, plato):
        """
        Método para agregar un plato solo al menú del restaurante.
        """
        # Agregamos solo al menú del restaurante, no al menú de la cafetería
        self.menu.append(plato)
        print(f"Plato '{plato}' agregado al menú del restaurante {self.nombre}.")

    def listar_menu_restaurante(self):
        """
        Método para listar los platos disponibles en el menú del restaurante.
        """
        print(f"Menú del restaurante {self.nombre}:")
        self.listar_menu()  # Reutilizamos el método de la clase Cafeteria

    def __del__(self):
        """
        Destructor de la clase Restaurante.
        Llamamos al destructor de la clase base Cafeteria para realizar limpieza.
        """
        print(f"El restaurante {self.nombre} especializado en {self.tipo_cocina} ha sido cerrado.")
        super().__del__()  # Llamamos al destructor de la clase base Cafeteria


# Ejemplo de uso de las clases Cafeteria y Restaurante
if __name__ == "__main__":
    # Crear la cafetería
    cafeteria1 = Cafeteria("DELIYARI", "AV. LIBERTAD y PARADA 9", ["Café", "Pasteles", "Sándwich"])
    cafeteria1.agregar_plato("Torta de zanahoria")
    cafeteria1.listar_menu()

    # Crear el restaurante
    restaurante1 = Restaurante("LA PARILLA", "Avenida del Sol", ["Asado", "Pasta", "Pizza"], "Comida Italiana")
    restaurante1.agregar_plato_restaurante("Empanadas")
    restaurante1.listar_menu_restaurante()

    # Destruir los objetos (llama automáticamente a los destructores)
    del cafeteria1
    del restaurante1
