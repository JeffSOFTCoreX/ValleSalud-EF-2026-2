import unittest

from src.dominio import (
    Paciente,
    Cita,
    Medicamento,
)


class TestDominio(unittest.TestCase):

    def test_paciente_agrega_cita(self):

        paciente = Paciente(
            "P001",
            "Juan Perez",
            35,
            "300-000-0001"
        )

        cita = Cita(
            "C001",
            "2026-10-05",
            "09:00",
            "Dra. Ana Gomez",
            paciente,
            "Consulta general"
        )

        paciente.agregar_cita(cita)

        self.assertEqual(
            paciente.cantidad_citas(),
            1
        )

        self.assertIs(
            paciente.citas[0],
            cita
        )

    def test_cita_agrega_medicamento(self):

        paciente = Paciente(
            "P001",
            "Juan Perez",
            35,
            "300-000-0001"
        )

        cita = Cita(
            "C001",
            "2026-10-05",
            "09:00",
            "Dra. Ana Gomez",
            paciente,
            "Consulta general"
        )

        medicamento = Medicamento(
            "Acetaminofen",
            "500 mg",
            "cada 8 horas"
        )

        cita.agregar_medicamento(
            medicamento
        )

        self.assertEqual(
            len(cita.medicamentos),
            1
        )


if __name__ == "__main__":
    unittest.main()
