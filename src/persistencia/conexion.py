import sqlite3
from pathlib import Path


RUTA_BD = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "vallesalud.db"
)


def obtener_conexion(ruta_bd=None):
    """
    Crea y devuelve una conexión SQLite.

    Si no se indica una ruta, utiliza:
    data/vallesalud.db
    """

    if ruta_bd == ":memory:":
        conexion = sqlite3.connect(":memory:")
    else:
        ruta = Path(ruta_bd) if ruta_bd else RUTA_BD

        ruta.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        conexion = sqlite3.connect(
            str(ruta)
        )

    conexion.row_factory = sqlite3.Row

    conexion.execute(
        "PRAGMA foreign_keys = ON"
    )

    return conexion


def crear_tablas(conexion):
    """
    Crea las tablas necesarias para el prototipo.
    """

    conexion.executescript(
        """
        CREATE TABLE IF NOT EXISTS pacientes (
            identificacion TEXT PRIMARY KEY,
            nombre TEXT NOT NULL,
            edad INTEGER NOT NULL,
            telefono TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS citas (
            codigo TEXT PRIMARY KEY,
            fecha TEXT NOT NULL,
            hora TEXT NOT NULL,
            profesional TEXT NOT NULL,
            paciente_id TEXT NOT NULL,
            motivo TEXT NOT NULL,
            observaciones TEXT,
            FOREIGN KEY (paciente_id)
                REFERENCES pacientes(identificacion)
        );

        CREATE TABLE IF NOT EXISTS medicamentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            dosis TEXT NOT NULL,
            frecuencia TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS cita_medicamentos (
            cita_codigo TEXT NOT NULL,
            medicamento_id INTEGER NOT NULL,

            PRIMARY KEY (
                cita_codigo,
                medicamento_id
            ),

            FOREIGN KEY (cita_codigo)
                REFERENCES citas(codigo),

            FOREIGN KEY (medicamento_id)
                REFERENCES medicamentos(id)
        );
        """
    )

    conexion.commit()