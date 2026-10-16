# Ejercicio 10: Carrito de compras de un e-commerce

from ej_2 import Producto  # Reutilizamos la clase Producto del ejercicio 02

class Item:
    def __init__(self, producto, cantidad):
        """Reúne un objeto Producto y la cantidad comprada."""
        self.producto = producto
        self.cantidad = cantidad

    def calcular_subtotal(self):
        """Suma el precio unitario del producto por la cantidad del ítem."""
        return self.producto.precio_unitario * self.cantidad

    def __str__(self):
        return f"{self.producto.nombre:<15} x{self.cantidad:<2} | Subtotal: {self.calcular_subtotal():,.0f} Gs."

class Carrito:
    def __init__(self, cliente):
        """Colección que almacena los ítems seleccionados."""
        self.cliente = cliente
        self.items = []

    def agregar_item(self, producto, cantidad):
        """Agrega un producto y su cantidad al carrito."""
        nuevo_item = Item(producto, cantidad)
        self.items.append(nuevo_item)

    def calcular_total(self):
        """Suma el costo de todos los subtotales del carrito."""
        total = 0
        for item in self.items:
            total += item.calcular_subtotal()
        return total

    def mostrar_detalle(self):
        """Imprime la factura detallada de la compra."""
        print(f"\n=== DETALLE DE COMPRA - Carrito de {self.cliente} ===")
        for item in self.items:
            print(f" - {item}")
        print("-" * 50)
        print(f" TOTAL A PAGAR: {self.calcular_total():,.0f} Gs.")
        print("=" * 50)

if __name__ == "__main__":
    prod1 = Producto("Teclado USB", 150000, 10)
    prod2 = Producto("Mouse Óptico", 80000, 15)

    mi_carrito = Carrito("Laura Benítez")
    mi_carrito.agregar_item(prod1, 2)
    mi_carrito.agregar_item(prod2, 1)

    mi_carrito.mostrar_detalle()