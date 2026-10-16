# Ejercicio 12: Cuenta de servicio con planes

class LineaTelefono:
    def __init__(self, numero, gb_incluidos):
        """Constructor de línea telefónica."""
        self.numero = numero
        self.gb_incluidos = gb_incluidos
        self.__gb_consumidos = 0.0  # Atributo privado

    def registrar_consumo(self, gb):
        """Suma gigabytes consumidos y emite alertas si el saldo se agota."""
        if gb <= 0:
            print("[-] El consumo debe ser mayor a 0 GB.")
            return

        if self.__gb_consumidos >= self.gb_incluidos:
            print(f" Operación rechazada: Paquete agotado para la línea {self.numero}.")
            return

        self.__gb_consumidos += gb
        print(f"[✓] Consumo de {gb:.2f} GB registrado.")

        if self.__gb_consumidos >= self.gb_incluidos:
            print(f"   ¡ALERTA! Has consumido la totalidad de tus datos incluidos ({self.gb_incluidos} GB).")

    def gb_disponibles(self):
        """Informa la cantidad restante de GB."""
        restante = self.gb_incluidos - self.__gb_consumidos
        return max(0.0, restante)

    def __str__(self):
        return (
            f"Línea: {self.numero} | Plan: {self.gb_incluidos} GB | "
            f"Consumido: {self.__gb_consumidos:.2f} GB | Disponible: {self.gb_disponibles():.2f} GB"
        )

if __name__ == "__main__":
    linea = LineaTelefono("0981-999888", gb_incluidos=10.0)
    print(linea)
    print()

    linea.registrar_consumo(6.5)
    print(linea)
    print()

    linea.registrar_consumo(4.0)  # Supera el plan -> salta la alerta
    print(linea)
    print()

    linea.registrar_consumo(2.0)  # Rechazado por paquete agotado