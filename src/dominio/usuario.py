class Usuario:
    """
    Clase base para los usuarios del Sistema ValleSalud.
    """

    def __init__(self, identificacion, nombre, rol):
        if not identificacion or not identificacion.strip():
            raise ValueError(
                "La identificación del usuario es obligatoria."
            )

        if not nombre or not nombre.strip():
            raise ValueError(
                "El nombre del usuario es obligatorio."
            )

        self.identificacion = identificacion.strip().upper()
        self.nombre = nombre.strip()
        self.rol = rol

    def tiene_permiso(self, permiso):
        """
        Método que será redefinido según el tipo de usuario.
        """
        return False

    def __str__(self):
        return (
            f"Usuario: {self.nombre} | "
            f"ID: {self.identificacion} | "
            f"Rol: {self.rol}"
        )


class UsuarioAdministrativo(Usuario):
    """
    Usuario encargado de tareas administrativas.
    """

    def __init__(self, identificacion, nombre):
        super().__init__(
            identificacion,
            nombre,
            "administrativo"
        )

    def tiene_permiso(self, permiso):
        permisos = {
            "registrar_paciente",
            "consultar_paciente",
            "programar_cita",
            "consultar_cita",
            "generar_reporte",
        }

        return permiso in permisos


class UsuarioAsistencial(Usuario):
    """
    Usuario correspondiente al personal asistencial.
    """

    def __init__(self, identificacion, nombre):
        super().__init__(
            identificacion,
            nombre,
            "asistencial"
        )

    def tiene_permiso(self, permiso):
        permisos = {
            "consultar_paciente",
            "consultar_cita",
            "registrar_atencion",
            "consultar_medicamento",
        }

        return permiso in permisos