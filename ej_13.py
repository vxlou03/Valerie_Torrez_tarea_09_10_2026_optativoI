# Ejercicio 13: Habitación de un hotel

class Habitacion:
    def __init__(self, numero, tipo, tarifa_por_noche):
        """Constructor de habitación."""
        self.numero = numero
        self.tipo = tipo
        self.tarifa_por_noche = tarifa_por_noche
        self.ocupada = False  # Estado inicial: libre

    def ocupar(self):
        """Cambia el estado a ocupada si no lo estaba previamente."""
        if not self.ocupada:
            self.ocupada = True
            print(f"[✓] Habitación {self.numero} ha sido ocupada con éxito.")
        else:
            print(f"[X] Error: La habitación {self.numero} ya se encuentra ocupada.")

    def liberar(self):
        """Desocupa la habitación."""
        if self.ocupada:
            self.ocupada = False
            print(f"[✓] Habitación {self.numero} liberada.")
        else:
            print(f"[-] La habitación {self.numero} ya estaba libre.")

    def calcular_costo_estadia(self, noches):
        """Multiplica la tarifa por el total de noches de estadía."""
        if noches > 0:
            return self.tarifa_por_noche * noches
        return 0

    def __str__(self):
        estado = "Ocupada" if self.ocupada else "Libre"
        return f"Habitación {self.numero} ({self.tipo}) | Tarifa: {self.tarifa_por_noche:,.0f} Gs./noche | Estado: [{estado}]"

if __name__ == "__main__":
    h = Habitacion(302, "Matrimonial Deluxe", 350000)
    print(h)
    print()

    # Ocupación
    h.ocupar()
    print(h)
    print()

    # Intento de re-ocupación no permitido
    h.ocupar()
    print()

    # Cálculo de estadía de 3 noches
    noches = 3
    costo = h.calcular_costo_estadia(noches)
    print(f"Costo por {noches} noches de estadía: {costo:,.0f} Gs.")
    print()

    # Liberación
    h.liberar()
    print(h)