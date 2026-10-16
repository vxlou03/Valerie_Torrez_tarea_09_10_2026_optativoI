# Ejercicio 3: Empleado y su sueldo

class Empleado:
    def __init__(self, nombre, cargo, salario_mensual):
        """Constructor de empleado."""
        self.nombre = nombre
        self.cargo = cargo
        self.salario_mensual = salario_mensual

    def calcular_salario_anual(self, incluir_aguinaldo=True):
        """Calcula el ingreso anual (12 meses + 1 mes opcional de aguinaldo)."""
        meses = 13 if incluir_aguinaldo else 12
        return self.salario_mensual * meses

    def __str__(self):
        """Devuelve los datos del empleado formateados."""
        return f"Empleado: {self.nombre} | Cargo: {self.cargo} | Salario mensual: {self.salario_mensual:,.0f} Gs."

if __name__ == "__main__":
    e1 = Empleado("Ana Torres", "Analista de Sistemas", 6500000)
    e2 = Empleado("Juan López", "Asistente Administrativo", 3200000)

    for emp in [e1, e2]:
        print(emp)
        print(f"  -> Cobro anual (con aguinaldo): {emp.calcular_salario_anual():,.0f} Gs.\n")