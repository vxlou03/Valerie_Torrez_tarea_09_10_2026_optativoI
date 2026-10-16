# Ejercicio 8: Reproductor de lista de canciones

class Cancion:
    def __init__(self, titulo, artista, duracion_segundos):
        """Constructor de la canción."""
        self.titulo = titulo
        self.artista = artista
        self.duracion_segundos = duracion_segundos

    def __str__(self):
        minutos = self.duracion_segundos // 60
        segundos = self.duracion_segundos % 60
        return f"'{self.titulo}' - {self.artista} ({minutos}:{segundos:02d})"

class ListaReproduccion:
    def __init__(self, nombre):
        """Lista que almacena colecciones de objetos Cancion."""
        self.nombre = nombre
        self.__canciones = []

    def agregar_cancion(self, cancion):
        """Agrega un objeto de tipo Cancion a la lista."""
        self.__canciones.append(cancion)

    def calcular_duracion_total(self):
        """Recorre las canciones y suma la duración total en segundos."""
        total_seg = 0
        for c in self.__canciones:
            total_seg += c.duracion_segundos
        return total_seg

    def __str__(self):
        lineas = [f"=== Lista de Reproducción: {self.nombre} ==="]
        for i, c in enumerate(self.__canciones, 1):
            lineas.append(f"{i}. {c}")
        
        tot_seg = self.calcular_duracion_total()
        minutos = tot_seg // 60
        segundos = tot_seg % 60
        lineas.append("-" * 40)
        lineas.append(f"Duración Total: {minutos} min {segundos} seg")
        return "\n".join(lineas)

if __name__ == "__main__":
    mi_playlist = ListaReproduccion("Éxitos de Rock")
    mi_playlist.agregar_cancion(Cancion("Bohemian Rhapsody", "Queen", 354))
    mi_playlist.agregar_cancion(Cancion("Hotel California", "Eagles", 391))
    mi_playlist.agregar_cancion(Cancion("De Música Ligera", "Soda Stereo", 212))

    print(mi_playlist)