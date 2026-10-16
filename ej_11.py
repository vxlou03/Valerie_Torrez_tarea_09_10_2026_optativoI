# Ejercicio 11: Estudiante y sus materias

class Estudiante:
    def __init__(self, nombre, carrera):
        """Constructor del estudiante."""
        self.nombre = nombre
        self.carrera = carrera
        self.notas = {}  # Diccionario: {"Materia": nota}

    def registrar_nota(self, materia, nota):
        """Guarda la nota obtenida en una materia."""
        if 1 <= nota <= 5:
            self.notas[materia] = nota
        else:
            print("[-] Error: La nota debe estar entre 1 y 5.")

    def calcular_promedio(self):
        """Calcula el promedio general sin usar funciones complejas."""
        if not self.notas:
            return 0.0
        suma = 0
        for n in self.notas.values():
            suma += n
        return suma / len(self.notas)

    def esta_aprobado(self, nota_minima=2.0):
        """Verifica si el promedio alcanza el valor mínimo exigido."""
        return self.calcular_promedio() >= nota_minima

    def __str__(self):
        lineas = [f"--- BOLETÍN ACADÉMICO ---", f"Estudiante: {self.nombre}", f"Carrera   : {self.carrera}", "Notas:"]
        for mat, nota in self.notas.items():
            lineas.append(f"  * {mat:<20}: {nota}")
        
        prom = self.calcular_promedio()
        condicion = "APROBADO" if self.esta_aprobado() else "REPROBADO"
        lineas.append("-" * 30)
        lineas.append(f"Promedio General: {prom:.2f}")
        lineas.append(f"Condición Final : [{condicion}]")
        return "\n".join(lineas)

if __name__ == "__main__":
    e = Estudiante("Matías Fernández", "Ingeniería en Informática")
    e.registrar_nota("Python I", 5)
    e.registrar_nota("Algoritmos", 4)
    e.registrar_nota("Matemática Discreta", 3)

    print(e)