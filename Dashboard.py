import os

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r', encoding='utf-8', errors='ignore') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'Unidad 1/COMPARACION PROGRAMACION TRADICIONAL Y POO/Programacion orientada a objetos.py',
        '2': 'Unidad 1/COMPARACION PROGRAMACION TRADICIONAL Y POO/Programacion tradicional.py',
        '3': 'Unidad 1/Ejemplos de tecnicas de programacion/ABSTRACCION/Ejemplo tecnica abstraccion.py',
        '4': 'Unidad 1/Ejemplos de tecnicas de programacion/ENCAPSULACION/Ejemplo.py',
        '5': 'Unidad 1/Ejemplos de tecnicas de programacion/HERENCIA/Ejemplo.py',
        '6': 'Unidad 1/Ejemplos de tecnicas de programacion/POLIMORFISMO/Ejemplo.py',
        '7': 'Unidad 1/EJEMPLOS DEL MUNDO REAL POO/Tienda/Cliente.py',
        '8': 'Unidad 1/EJEMPLOS DEL MUNDO REAL POO/Tienda/Main.py',
        '9': 'Unidad 1/EJEMPLOS DEL MUNDO REAL POO/Tienda/Producto.py' ,
        '10':'Unidad 2/Constructores o destructores/Semana 7.py' ,
        '11':'Unidad 2/HERENCIA,ENCAPSULACION Y POLIMORFISMO/Semana 6.py',
        '12':'Unidad 2/IDENTIFICADORES TIPOS Y FUNCIONES/Semana 5.py',
    }

    while True:
        print("\n********Menu Principal - Dashboard*************")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()