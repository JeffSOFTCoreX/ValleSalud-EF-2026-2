import unittest

from src.patrones import (
    ConexionSingleton,
    UsuarioFactory,
)

from src.persistencia import crear_tablas

from src.dominio import (
    UsuarioAdministrativo,
    UsuarioAsistencial,
)


class TestSingleton(unittest.TestCase):

    def tearDown(self):
        instancia = ConexionSingleton(":memory:")
        instancia.cerrar_conexion()

    def test_singleton_misma_instancia(self):
        conexion_1 = ConexionSingleton(":memory:")
        conexion_2 = ConexionSingleton(":memory:")

        self.assertIs(
            conexion_1,
            conexion_2
        )

    def test_singleton_misma_conexion(self):
        singleton_1 = ConexionSingleton(":memory:")
        singleton_2 = ConexionSingleton(":memory:")

        conexion_1 = singleton_1.obtener_conexion()
        conexion_2 = singleton_2.obtener_conexion()

        self.assertIs(
            conexion_1,
            conexion_2
        )

    def test_singleton_permite_crear_tablas(self):
        singleton = ConexionSingleton(":memory:")

        conexion = singleton.obtener_conexion()

        crear_tablas(
            conexion
        )

        cursor = conexion.execute(
            """
            SELECT name
            FROM sqlite_master
            WHERE type = 'table'
            AND name = 'pacientes'
            """
        )

        resultado = cursor.fetchone()

        self.assertIsNotNone(
            resultado
        )


class TestUsuarioFactory(unittest.TestCase):

    def test_crear_usuario_administrativo(self):
        usuario = UsuarioFactory.crear_usuario(
            "administrativo",
            "U001",
            "Carlos Administrativo"
        )

        self.assertIsInstance(
            usuario,
            UsuarioAdministrativo
        )

        self.assertEqual(
            usuario.rol,
            "administrativo"
        )

    def test_crear_usuario_asistencial(self):
        usuario = UsuarioFactory.crear_usuario(
            "asistencial",
            "U002",
            "Ana Asistencial"
        )

        self.assertIsInstance(
            usuario,
            UsuarioAsistencial
        )

        self.assertEqual(
            usuario.rol,
            "asistencial"
        )

    def test_permiso_administrativo(self):
        usuario = UsuarioFactory.crear_usuario(
            "administrativo",
            "U001",
            "Carlos Administrativo"
        )

        self.assertTrue(
            usuario.tiene_permiso(
                "programar_cita"
            )
        )

        self.assertFalse(
            usuario.tiene_permiso(
                "registrar_atencion"
            )
        )

    def test_permiso_asistencial(self):
        usuario = UsuarioFactory.crear_usuario(
            "asistencial",
            "U002",
            "Ana Asistencial"
        )

        self.assertTrue(
            usuario.tiene_permiso(
                "registrar_atencion"
            )
        )

        self.assertFalse(
            usuario.tiene_permiso(
                "generar_reporte"
            )
        )

    def test_factory_rol_invalido(self):
        with self.assertRaises(ValueError):
            UsuarioFactory.crear_usuario(
                "otro",
                "U003",
                "Usuario Prueba"
            )


if __name__ == "__main__":
    unittest.main()