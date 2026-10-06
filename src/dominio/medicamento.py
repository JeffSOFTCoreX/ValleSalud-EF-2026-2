class Medicamento:
    """Representa un medicamento que puede registrarse en una cita."""

    def __init__(self, nombre, dosis, frecuencia):
        self._nombre = nombre
        self._dosis = dosis
        self._frecuencia = frecuencia

    @property
    def nombre(self):
        return self._nombre

    @property
    def dosis(self):
        return self._dosis

    @property
    def frecuencia(self):
        return self._frecuencia

    def indicacion(self):
        """Devuelve la indicación del medicamento."""
        return f"{self.nombre} - {self.dosis}, {self.frecuencia}"

    def __str__(self):
        return self.indicacion()