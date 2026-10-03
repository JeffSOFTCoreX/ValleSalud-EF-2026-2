class Medicamento:
    """Representa un medicamento que puede registrarse en una cita."""

    def __init__(self, nombre, dosis, frecuencia):
        self.nombre = nombre
        self.dosis = dosis
        self.frecuencia = frecuencia

    def indicacion(self):
        """Devuelve la indicación del medicamento."""
        return f"{self.nombre} - {self.dosis}, {self.frecuencia}"

    def __str__(self):
        return self.indicacion()