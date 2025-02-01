class ClimaSemanal:
    def __init__(self):
        # Lista para almacenar las temperaturas diarias
        self.temperaturas = []

    # Método para ingresar temperaturas
    def ingresar_temperaturas(self):
        for i in range(7):
            temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
            self.temperaturas.append(temp)

    # Método para calcular el promedio
    def calcular_promedio(self):
        if not self.temperaturas:
            return 0  # Manejo de caso vacío
        return sum(self.temperaturas) / len(self.temperaturas)

# Función principal
def main():
    print("POO: Promedio semanal del clima")
    clima = ClimaSemanal()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()
