# Ejercicio 9: Turnos de un consultorio

class Turno:
    def __init__(self, paciente, hora):
        """Constructor del turno."""
        self.paciente = paciente
        self.hora = hora
        self.atendido = False  # Estado inicial

    def marcar_como_atendido(self):
        """Cambia el estado del turno a atendido."""
        self.atendido = True

    def __str__(self):
        estado = "Atendido" if self.atendido else "Pendiente"
        return f"[{self.hora}] Paciente: {self.paciente:<15} | Estado: {estado}"

class Agenda:
    def __init__(self, fecha):
        """Colección que gestiona los turnos del día."""
        self.fecha = fecha
        self.turnos = []

    def agendar_turno(self, turno):
        """Añade un nuevo turno a la agenda."""
        self.turnos.append(turno)

    def listar_pendientes(self):
        """Muestra en pantalla únicamente los turnos pendientes."""
        print(f"\n--- Turnos Pendientes para la fecha {self.fecha} ---")
        pendientes = [t for t in self.turnos if not t.atendido]
        if pendientes:
            for t in pendientes:
                print(t)
        else:
            print("No quedan turnos pendientes por hoy.")

if __name__ == "__main__":
    agenda_hoy = Agenda("18/09/2026")
    
    t1 = Turno("Juan Pérez", "08:00")
    t2 = Turno("Ana Gómez", "08:30")
    t3 = Turno("Carlos Sosa", "09:00")

    agenda_hoy.agendar_turno(t1)
    agenda_hoy.agendar_turno(t2)
    agenda_hoy.agendar_turno(t3)

    agenda_hoy.listar_pendientes()

    # Simulamos atender al primer paciente
    print("\n[>> Atendiendo al paciente de las 08:00... <<]")
    t1.marcar_como_atendido()

    agenda_hoy.listar_pendientes()