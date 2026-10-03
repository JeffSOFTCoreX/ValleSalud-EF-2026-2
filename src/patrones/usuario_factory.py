from src.dominio.usuario import (
    UsuarioAdministrativo,
    UsuarioAsistencial,
)


class UsuarioFactory:
    """
    Implementa el patrón Factory para crear
    usuarios según el rol solicitado.
    """

    @staticmethod
    def crear_usuario(
        rol,
        identificacion,
        nombre
    ):
        rol = rol.strip().lower()

        if rol == "administrativo":
            return UsuarioAdministrativo(
                identificacion,
                nombre
            )

        if rol == "asistencial":
            return UsuarioAsistencial(
                identificacion,
                nombre
            )

        raise ValueError(
            f"Rol de usuario no válido: {rol}"
        )