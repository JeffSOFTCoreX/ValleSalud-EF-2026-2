import unittest

from src.dominio import Paciente


class TestValidaciones(unittest.TestCase):

    def test_paciente_valido(self):
        paciente = Paciente(
            "P001",
            "Juan Perez",
            35,
            "300-000-0001"
        )

        self.assertEqual(
            paciente.identificacion,
            "P001"
        )

        self.assertEqual(
            paciente.nombre,
            "Juan Perez"
        )

        self.assertEqual(
            paciente.edad,
            35
        )

    def test_nombre_vacio(self):
        with self.assertRaises(ValueError):
            Paciente(
                "P001",
                "",
                35,
                "300-000-0001"
            )

    def test_identificacion_vacia(self):
        with self.assertRaises(ValueError):
            Paciente(
                "",
                "Juan Perez",
                35,
                "300-000-0001"
            )

    def test_edad_negativa(self):
        with self.assertRaises(ValueError):
            Paciente(
                "P001",
                "Juan Perez",
                -5,
                "300-000-0001"
            )

    def test_edad_no_numerica(self):
        with self.assertRaises(ValueError):
            Paciente(
                "P001",
                "Juan Perez",
                "treinta",
                "300-000-0001"
            )

    def test_telefono_vacio(self):
        with self.assertRaises(ValueError):
            Paciente(
                "P001",
                "Juan Perez",
                35,
                ""
            )


if __name__ == "__main__":
    unittest.main()