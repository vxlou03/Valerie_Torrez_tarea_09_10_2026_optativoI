# Ejercicio 6: Caja registradora de una cuenta corriente

class CuentaCorriente:
    def __init__(self, cliente, saldo_inicial=0):
        """Constructor con saldo protegido."""
        self.cliente = cliente
        self.__saldo = max(0, saldo_inicial)  # Atributo privado

    def acreditar(self, monto):
        """Acredita dinero a la cuenta asegurando que sea un valor positivo."""
        if monto > 0:
            self.__saldo += monto
            print(f"[+] Depósito exitoso de {monto:,.0f} Gs.")
        else:
            print("[-] Error: El monto a acreditar debe ser mayor a 0.")

    def registrar_consumo(self, monto):
        """Registra una compra validando que el saldo sea suficiente."""
        if monto <= 0:
            print("[-] Error: El monto del consumo debe ser positivo.")
        elif monto <= self.__saldo:
            self.__saldo -= monto
            print(f"[✓] Consumo aprobado de {monto:,.0f} Gs.")
        else:
            print(f"[X] Rechazado: Saldo insuficiente para pagar {monto:,.0f} Gs.")

    def __str__(self):
        return f"Cuenta Corriente - Cliente: {self.cliente} | Saldo Actual: {self.__saldo:,.0f} Gs."

if __name__ == "__main__":
    cuenta = CuentaCorriente("Roberto Gómez", 100000)
    print(cuenta)
    print()

    # Secuencia de prueba
    cuenta.acreditar(50000)
    print(cuenta)
    print()

    cuenta.registrar_consumo(80000)
    print(cuenta)
    print()

    # Intento de compra rechazada por falta de fondos
    cuenta.registrar_consumo(100000)
    print(cuenta)