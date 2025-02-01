class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.__titular = titular   # Atributo privado
        self.__saldo = saldo_inicial  # Atributo privado

    # Getter para el titular
    def get_titular(self):
        return self.__titular

    # Setter para el titular
    def set_titular(self, titular):
        self.__titular = titular

    # Getter para el saldo
    def get_saldo(self):
        return self.__saldo

    # Método para depositar dinero
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Deposito exitoso. Nuevo saldo: {self.__saldo}")
        else:
            print("La cantidad a depositar debe ser mayor que 0.")

    # Método para retirar dinero
    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retiro exitoso. Nuevo saldo: {self.__saldo}")
        else:
            print("Saldo insuficiente o cantidad inválida.")

# Ejemplo de uso
cuenta = CuentaBancaria("Yaritza Arboleda", 500)

# Accediendo a los métodos getter y setter
print(f"Titular: {cuenta.get_titular()}")
print(f"Saldo inicial: {cuenta.get_saldo()}")

# Realizando operaciones
cuenta.depositar(200)    # Depositar dinero
cuenta.retirar(100)      # Retirar dinero

# Accediendo y modificando el saldo y titular
cuenta.set_titular("Juan Pérez")
print(f"Nuevo titular: {cuenta.get_titular()}")
