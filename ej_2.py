# Ejercicio 2: Producto de almacén (

class Producto:
    def __init__(self, nombre, precio_unitario, stock):
        """Constructor de producto con nombre, precio y cantidad en stock."""
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.stock = stock

    def calcular_valor_total_stock(self):
        """Calcula el valor monetario total del producto en inventario."""
        return self.precio_unitario * self.stock

    def __str__(self):
        """Muestra el producto con su precio unitario y unidades en stock."""
        return f"Producto: {self.nombre:<12} | Precio: {self.precio_unitario:,.0f} Gs. | Stock: {self.stock} un."

if __name__ == "__main__":
    # Instanciación de tres productos de despensa
    p1 = Producto("Yerba 500g", 12000, 25)
    p2 = Producto("Leche 1L", 7500, 40)
    p3 = Producto("Aceite 900ml", 14500, 10)

    for p in [p1, p2, p3]:
        print(p)
        print(f"  -> Valor total en stock: {p.calcular_valor_total_stock():,.0f} Gs.\n")