class Cita:
    """Representa una cita médica asociada con un paciente."""

    def __init__(
        self,
        codigo,
        fecha,
        hora,
        profesional,
        paciente,
        motivo
    ):
        self.codigo = codigo
        self.fecha = fecha
        self.hora = hora
        self.profesional = profesional
        self.paciente = paciente
        self.motivo = motivo
        self.observaciones = "Pendiente de atención"
        self.medicamentos = []

    def registrar_atencion(self, observaciones):
        """Guarda información básica de la atención."""
        self.observaciones = observaciones

    def agregar_medicamento(self, medicamento):
        """Agrega un medicamento a la cita."""
        if medicamento not in self.medicamentos:
            self.medicamentos.append(medicamento)

    def resumen(self):
        """Devuelve un resumen completo de la cita."""
        lineas = [
            f"Cita {self.codigo}: {self.fecha} a las {self.hora}",
            f"Paciente: {self.paciente.nombre}",
            f"Profesional: {self.profesional}",
            f"Motivo: {self.motivo}",
            f"Observaciones: {self.observaciones}",
        ]

        if self.medicamentos:
            lineas.append("Medicamentos indicados:")

            for medicamento in self.medicamentos:
                lineas.append(f" - {medicamento}")
        else:
            lineas.append("Medicamentos indicados: ninguno")

        return "\n".join(lineas)

    def __str__(self):
        return (
            f"Cita {self.codigo} | "
            f"{self.fecha} {self.hora} | "
            f"Paciente: {self.paciente.nombre}"
        )