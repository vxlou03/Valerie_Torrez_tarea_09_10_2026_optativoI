# Ejercicio 4: Libro de una biblioteca

class Libro:
    def __init__(self, titulo, autor, disponible=True):
        """Constructor del libro."""
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible  # Atributo booleano (True/False)

    def __str__(self):
        """Muestra el libro indicando si se encuentra disponible o prestado."""
        estado = "Disponible" if self.disponible else "Prestado"
        return f"Título: '{self.titulo}' | Autor: {self.autor} | Estado: [{estado}]"

if __name__ == "__main__":
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", disponible=True)
    libro2 = Libro("Yo el Supremo", "Augusto Roa Bastos", disponible=False)

    print(libro1)
    print(libro2)