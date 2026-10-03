from src.persistencia.conexion import obtener_conexion


class ConexionSingleton:
    """
    Implementa el patrón Singleton para mantener
    una única instancia de conexión SQLite.
    """

    _instancia = None
    _conexion = None

    def __new__(cls, ruta_bd=None):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)

        if cls._conexion is None:
            cls._conexion = obtener_conexion(ruta_bd)

        return cls._instancia

    def obtener_conexion(self):
        """
        Devuelve la conexión SQLite compartida.
        """
        return self._conexion

    def cerrar_conexion(self):
        """
        Cierra la conexión y reinicia el Singleton.
        """
        if self._conexion is not None:
            self._conexion.close()

        type(self)._conexion = None
        type(self)._instancia = None