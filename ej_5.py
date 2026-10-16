# Ejercicio 5: Vehículo de una agencia

class Vehiculo:
    def __init__(self, marca, modelo, anio, precio):
        """Constructor de vehículo."""
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.precio = precio

    def descripcion_comercial(self):
        """Devuelve la descripción comercial formateada para publicación."""
        return f"{self.marca} {self.modelo} {self.anio} - {self.precio:,.0f} Gs."

    def __str__(self):
        return self.descripcion_comercial()

if __name__ == "__main__":
    v1 = Vehiculo("Toyota", "Corolla", 2020, 95000000)
    v2 = Vehiculo("Hyundai", "HB20", 2022, 82000000)

    print("--- Catálogo de la Agencia ---")
    print(v1)
    print(v2)