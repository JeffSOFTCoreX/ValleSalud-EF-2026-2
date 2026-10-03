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
        self.identificacion = validar_identificacion(
            identificacion
        )

        self.nombre = validar_nombre(
            nombre
        )

        self.edad = validar_edad(
            edad
        )

        self.telefono = validar_telefono(
            telefono
        )

        self.citas = []

    def agregar_cita(self, cita):
        if cita not in self.citas:
            self.citas.append(cita)

    def cantidad_citas(self):
        return len(self.citas)

    def __str__(self):
        return (
            f"Paciente: {self.nombre} | "
            f"ID: {self.identificacion} | "
            f"Edad: {self.edad} | "
            f"Teléfono: {self.telefono}"
        )