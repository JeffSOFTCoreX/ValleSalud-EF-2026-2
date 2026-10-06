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
        self._codigo = codigo
        self._fecha = fecha
        self._hora = hora
        self._profesional = profesional
        self._paciente = paciente
        self._motivo = motivo
        self._observaciones = "Pendiente de atención"
        self._medicamentos = []

    @property
    def codigo(self):
        return self._codigo

    @property
    def fecha(self):
        return self._fecha

    @property
    def hora(self):
        return self._hora

    @property
    def profesional(self):
        return self._profesional

    @property
    def paciente(self):
        return self._paciente

    @property
    def motivo(self):
        return self._motivo

    @property
    def observaciones(self):
        return self._observaciones

    @property
    def medicamentos(self):
        return tuple(self._medicamentos)

    def registrar_atencion(self, observaciones):
        """Guarda información básica de la atención."""
        self._observaciones = observaciones

    def agregar_medicamento(self, medicamento):
        """Agrega un medicamento a la cita."""
        if medicamento not in self._medicamentos:
            self._medicamentos.append(medicamento)

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