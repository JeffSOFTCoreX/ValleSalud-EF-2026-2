from src.servicios.validaciones import (
    validar_identificacion,
    validar_nombre,
    validar_edad,
    validar_telefono,
)


class Paciente:
    """Representa a una persona registrada como paciente."""

    def __init__(
        self,
        identificacion,
        nombre,
        edad,
        telefono
    ):
        self._identificacion = validar_identificacion(
            identificacion
        )

        self._nombre = validar_nombre(
            nombre
        )

        self._edad = validar_edad(
            edad
        )

        self._telefono = validar_telefono(
            telefono
        )

        self._citas = []

    @property
    def identificacion(self):
        return self._identificacion

    @identificacion.setter
    def identificacion(self, valor):
        self._identificacion = validar_identificacion(
            valor
        )

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = validar_nombre(
            valor
        )

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        self._edad = validar_edad(
            valor
        )

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        self._telefono = validar_telefono(
            valor
        )

    @property
    def citas(self):
        return tuple(self._citas)

    def agregar_cita(self, cita):
        if cita not in self._citas:
            self._citas.append(cita)

    def cantidad_citas(self):
        return len(self.citas)

    def __str__(self):
        return (
            f"Paciente: {self.nombre} | "
            f"ID: {self.identificacion} | "
            f"Edad: {self.edad} | "
            f"Teléfono: {self.telefono}"
        )