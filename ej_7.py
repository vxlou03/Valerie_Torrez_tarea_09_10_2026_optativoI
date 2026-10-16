# Ejercicio 7: Control de stock con alertas

class ProductoStock:
    def __init__(self, nombre, precio, stock_inicial, stock_minimo=5):
        """Constructor de producto con manejo de stock y límite mínimo."""
        self.nombre = nombre
        self.precio = precio
        self.__stock = stock_inicial
        self.stock_minimo = stock_minimo

    def reponer(self, cantidad):
        """Suma unidades al inventario."""
        if cantidad > 0:
            self.__stock += cantidad
            print(f"[+] Reposición de {cantidad} un. de '{self.nombre}' realizada.")
            self._verificar_alerta()

    def vender(self, cantidad):
        """Resta unidades si hay disponible suficiente."""
        if cantidad <= 0:
            print("[-] Error: La cantidad a vender debe ser mayor a 0.")
        elif cantidad <= self.__stock:
            self.__stock -= cantidad
            print(f"[✓] Venta aprobada de {cantidad} un. de '{self.nombre}'.")
            self._verificar_alerta()
        else:
            print(f"[X] Venta no realizada: Stock insuficiente de '{self.nombre}' (Quedan {self.__stock} un.).")

    def _verificar_alerta(self):
        """Método privado para emitir alerta si se supera el umbral mínimo."""
        if self.__stock < self.stock_minimo:
            print(f"   ¡ALERTA DE REPOSICIÓN! Stock bajo en '{self.nombre}' ({self.__stock} un. restantes, mínimo: {self.stock_minimo}).")

    def __str__(self):
        return f"Producto: {self.nombre} | Precio: {self.precio:,.0f} Gs. | Stock: {self.__stock} un."

if __name__ == "__main__":
    prod = ProductoStock("Café 250g", 22000, stock_inicial=10, stock_minimo=4)
    print(prod)
    print()

    prod.vender(7)  # Quedan 3 -> Debe saltar la alerta
    print(prod)
    print()

    prod.vender(5)  # No alcanza -> Se rechaza
    print()

    prod.reponer(10)  # Se recupera el stock
    print(prod)