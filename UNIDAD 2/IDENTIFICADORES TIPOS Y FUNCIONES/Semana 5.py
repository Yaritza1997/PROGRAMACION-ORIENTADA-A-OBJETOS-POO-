# Programa para calcular el Índice de Masa Corporal (IMC).
# Permite al usuario ingresar su peso y altura, y calcula su IMC.

def calcular_imc(peso, altura):
    """Calcula el Índice de Masa Corporal (IMC)."""
    return peso / (altura ** 2)


def main():
    print("BIENVENIDO AL PROGRAMA DE CALCULO: INDICE DE MASA CORPORAL.")

    try:
        # Solicitar peso y altura al usuario
        peso = float(input("Ingrese su peso en kilogramos: "))
        altura = float(input("Ingrese su altura en metros: "))

        # Validar que los valores sean positivos
        if peso <= 0 or altura <= 0:
            print("El peso y la altura deben ser valores positivos.")
            return

        # Calcular y mostrar el IMC
        imc = calcular_imc(peso, altura)
        print(f"Su Índice de Masa Corporal (IMC) es: {imc:.2f}")

        # Interpretación del IMC
        if imc < 18.5:
            print("Clasificación: Tienes un bajo peso")
        elif 18.5 <= imc < 24.9:
            print("Clasificación: Tienes un peso normal")
        elif 25 <= imc < 29.9:
            print("Clasificación: Tienes sobrepeso")
        else:
            print("Clasificación: Tienes obesidad")

    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")


if __name__ == "__main__":
    main()