import unittest

from src.dominio import (
    Paciente,
    Cita,
    Medicamento,
)

from src.persistencia import (
    obtener_conexion,
    crear_tablas,
    guardar_paciente,
    buscar_paciente_db,
    listar_pacientes,
    actualizar_paciente,
    eliminar_paciente,
    guardar_cita,
    buscar_cita_db,
    guardar_medicamento,
    buscar_medicamento_db,
    asociar_medicamento_cita,
    obtener_medicamentos_cita,
)


class TestPersistencia(unittest.TestCase):

    def setUp(self):
        self.conexion = obtener_conexion(
            ":memory:"
        )

        crear_tablas(
            self.conexion
        )

    def tearDown(self):
        self.conexion.close()

    # ------------------------------------------------------
    # PACIENTES
    # ------------------------------------------------------

    def test_guardar_paciente(self):
        paciente = Paciente(
            "P001",
            "Juan Perez",
            35,
            "300-000-0001"
        )

        guardar_paciente(
            self.conexion,
            paciente
        )

        encontrado = buscar_paciente_db(
            self.conexion,
            "P001"
        )

        self.assertIsNotNone(
            encontrado
        )

        self.assertEqual(
            encontrado.nombre,
            "Juan Perez"
        )

    def test_buscar_paciente_inexistente(self):
        encontrado = buscar_paciente_db(
            self.conexion,
            "P999"
        )

        self.assertIsNone(
            encontrado
        )

    def test_listar_pacientes(self):
        paciente_1 = Paciente(
            "P001",
            "Juan Perez",
            35,
            "300-000-0001"
        )

        paciente_2 = Paciente(
            "P002",
            "Maria Lopez",
            29,
            "300-000-0002"
        )

        guardar_paciente(
            self.conexion,
            paciente_1
        )

        guardar_paciente(
            self.conexion,
            paciente_2
        )

        pacientes = listar_pacientes(
            self.conexion
        )

        self.assertEqual(
            len(pacientes),
            2
        )

    def test_actualizar_paciente(self):
        paciente = Paciente(
            "P001",
            "Juan Perez",
            35,
            "300-000-0001"
        )

        guardar_paciente(
            self.conexion,
            paciente
        )

        paciente.nombre = (
            "Juan Perez Actualizado"
        )

        paciente.edad = 36

        actualizado = actualizar_paciente(
            self.conexion,
            paciente
        )

        self.assertTrue(
            actualizado
        )

        encontrado = buscar_paciente_db(
            self.conexion,
            "P001"
        )

        self.assertEqual(
            encontrado.nombre,
            "Juan Perez Actualizado"
        )

        self.assertEqual(
            encontrado.edad,
            36
        )

    def test_eliminar_paciente(self):
        paciente = Paciente(
            "P001",
            "Juan Perez",
            35,
            "300-000-0001"
        )

        guardar_paciente(
            self.conexion,
            paciente
        )

        eliminado = eliminar_paciente(
            self.conexion,
            "P001"
        )

        self.assertTrue(
            eliminado
        )

        encontrado = buscar_paciente_db(
            self.conexion,
            "P001"
        )

        self.assertIsNone(
            encontrado
        )

    # ------------------------------------------------------
    # CITAS
    # ------------------------------------------------------

    def test_guardar_cita(self):
        paciente = Paciente(
            "P001",
            "Juan Perez",
            35,
            "300-000-0001"
        )

        guardar_paciente(
            self.conexion,
            paciente
        )

        cita = Cita(
            "C001",
            "2026-10-05",
            "09:00",
            "Dra. Ana Gomez",
            paciente,
            "Consulta general"
        )

        cita.registrar_atencion(
            "Paciente estable."
        )

        guardar_cita(
            self.conexion,
            cita
        )

        encontrada = buscar_cita_db(
            self.conexion,
            "C001"
        )

        self.assertIsNotNone(
            encontrada
        )

        self.assertEqual(
            encontrada.paciente.nombre,
            "Juan Perez"
        )

        self.assertEqual(
            encontrada.observaciones,
            "Paciente estable."
        )

    # ------------------------------------------------------
    # MEDICAMENTOS
    # ------------------------------------------------------

    def test_guardar_medicamento(self):
        medicamento = Medicamento(
            "Acetaminofen",
            "500 mg",
            "cada 8 horas"
        )

        medicamento_id = guardar_medicamento(
            self.conexion,
            medicamento
        )

        encontrado = buscar_medicamento_db(
            self.conexion,
            medicamento_id
        )

        self.assertIsNotNone(
            encontrado
        )

        self.assertEqual(
            encontrado.nombre,
            "Acetaminofen"
        )

    # ------------------------------------------------------
    # RELACIÓN CITA - MEDICAMENTO
    # ------------------------------------------------------

    def test_asociar_medicamento_cita(self):
        paciente = Paciente(
            "P001",
            "Juan Perez",
            35,
            "300-000-0001"
        )

        guardar_paciente(
            self.conexion,
            paciente
        )

        cita = Cita(
            "C001",
            "2026-10-05",
            "09:00",
            "Dra. Ana Gomez",
            paciente,
            "Consulta general"
        )

        guardar_cita(
            self.conexion,
            cita
        )

        medicamento = Medicamento(
            "Acetaminofen",
            "500 mg",
            "cada 8 horas"
        )

        medicamento_id = guardar_medicamento(
            self.conexion,
            medicamento
        )

        asociar_medicamento_cita(
            self.conexion,
            "C001",
            medicamento_id
        )

        medicamentos = obtener_medicamentos_cita(
            self.conexion,
            "C001"
        )

        self.assertEqual(
            len(medicamentos),
            1
        )

        self.assertEqual(
            medicamentos[0].nombre,
            "Acetaminofen"
        )


if __name__ == "__main__":
    unittest.main()