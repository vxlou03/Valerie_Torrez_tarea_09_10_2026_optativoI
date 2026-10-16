# Ejercicio 1: Ficha de cliente

class Cliente:
    def __init__(self, nombre, cedula, telefono):
        """Constructor: inicializa los datos personales del cliente."""
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono

    def __str__(self):
        """Devuelve la ficha del cliente ordenada y legible."""
        return (
            f"--- FICHA DE CLIENTE ---\n"
            f"Nombre   : {self.nombre}\n"
            f"Cédula   : {self.cedula}\n"
            f"Teléfono : {self.telefono}\n"
            f"------------------------"
        )

if __name__ == "__main__":
    # Creación de dos objetos distintos
    cliente1 = Cliente("María González", "4.567.890", "0981-123456")
    cliente2 = Cliente("Carlos Benítez", "3.210.987", "0971-654321")

    print(cliente1)
    print()
    print(cliente2)