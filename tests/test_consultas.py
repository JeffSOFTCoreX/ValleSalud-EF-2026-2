import unittest

from src.main import crear_datos_ficticios

from src.servicios import (
    filtrar_pacientes_por_nombre,
    buscar_paciente_por_id,
    consultar_citas_paciente,
    filtrar_citas_por_fecha,
    buscar_medicamentos_por_nombre,
    obtener_pacientes_adultos,
    obtener_nombres_pacientes,
)


class TestConsultas(unittest.TestCase):

    def setUp(self):
        (
            self.pacientes,
            self.citas,
            self.medicamentos
        ) = crear_datos_ficticios()

    def test_filtrar_paciente_por_nombre(self):
        resultado = filtrar_pacientes_por_nombre(
            self.pacientes,
            "Juan"
        )

        self.assertEqual(
            len(resultado),
            1
        )

        self.assertEqual(
            resultado[0].nombre,
            "Juan Perez"
        )

    def test_buscar_paciente_por_id(self):
        resultado = buscar_paciente_por_id(
            self.pacientes,
            "P002"
        )

        self.assertIsNotNone(
            resultado
        )

        self.assertEqual(
            resultado.nombre,
            "Maria Lopez"
        )

    def test_consultar_citas_paciente(self):
        resultado = consultar_citas_paciente(
            self.pacientes[0]
        )

        self.assertEqual(
            len(resultado),
            1
        )

    def test_filtrar_citas_por_fecha(self):
        resultado = filtrar_citas_por_fecha(
            self.citas,
            "2026-10-05"
        )

        self.assertEqual(
            len(resultado),
            2
        )

    def test_buscar_medicamento_por_nombre(self):
        resultado = buscar_medicamentos_por_nombre(
            self.medicamentos,
            "Loratadina"
        )

        self.assertEqual(
            len(resultado),
            1
        )

    def test_paciente_id_inexistente(self):
        resultado = buscar_paciente_por_id(
            self.pacientes,
            "P999"
        )

        self.assertIsNone(
            resultado
        )

    def test_nombre_inexistente(self):
        resultado = filtrar_pacientes_por_nombre(
            self.pacientes,
            "Paciente inexistente"
        )

        self.assertEqual(
            resultado,
            []
        )

    def test_medicamento_inexistente(self):
        resultado = buscar_medicamentos_por_nombre(
            self.medicamentos,
            "Medicamento inexistente"
        )

        self.assertEqual(
            resultado,
            []
        )

    def test_obtener_pacientes_adultos(self):
        resultado = obtener_pacientes_adultos(
            self.pacientes
        )

        self.assertEqual(
            len(resultado),
            3
        )

        for paciente in resultado:
            self.assertGreaterEqual(
                paciente.edad,
                18
            )

    def test_obtener_nombres_pacientes(self):
        resultado = obtener_nombres_pacientes(
            self.pacientes
        )

        self.assertEqual(
            resultado,
            [
                "Juan Perez",
                "Maria Lopez",
                "Carlos Ramirez"
            ]
        )


if __name__ == "__main__":
    unittest.main()