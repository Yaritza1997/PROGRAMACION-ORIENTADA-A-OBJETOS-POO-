class Empleado:
    def __init__(self, nombre, puesto, salario):
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario

    def mostrar_info(self):
        print(f"Empleado: {self.nombre}")
        print(f"Puesto: {self.puesto}")
        print(f"Salario: {self.salario}")

    def trabajar(self):
        print(f"{self.nombre} está trabajando.")

# Clase derivada (subclase)
class Gerente(Empleado):
    def __init__(self, nombre, puesto, salario, departamento):
        # Llamando al constructor de la clase base
        super().__init__(nombre, puesto, salario)
        self.departamento = departamento

    # Método adicional específico para Gerente
    def gestionar_equipo(self):
        print(f"{self.nombre} está gestionando el departamento de {self.departamento}.")

    # Sobrescribir el método trabajar para personalizar el comportamiento
    def trabajar(self):
        print(f"{self.nombre} está supervisando el trabajo del equipo en {self.departamento}.")

# Ejemplo de uso
empleado = Empleado("Yaritza Arboleda", "Desarrolladora", 3000)
gerente = Gerente("Carlos Pérez", "Gerente de TI", 5000, "Tecnologías de la Información")

# Mostrando la información de cada empleado
empleado.mostrar_info()
empleado.trabajar()

print("\n---\n")

gerente.mostrar_info()
gerente.trabajar()
gerente.gestionar_equipo()