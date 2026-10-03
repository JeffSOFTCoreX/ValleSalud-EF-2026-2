from src.dominio import (
    Paciente,
    Cita,
    Medicamento,
)


# ==========================================================
# PACIENTES
# ==========================================================

def guardar_paciente(conexion, paciente):
    """
    Guarda un paciente en la base de datos.
    """

    conexion.execute(
        """
        INSERT INTO pacientes (
            identificacion,
            nombre,
            edad,
            telefono
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            paciente.identificacion,
            paciente.nombre,
            paciente.edad,
            paciente.telefono,
        )
    )

    conexion.commit()


def buscar_paciente_db(conexion, identificacion):
    """
    Busca un paciente mediante su identificación.
    """

    cursor = conexion.execute(
        """
        SELECT
            identificacion,
            nombre,
            edad,
            telefono
        FROM pacientes
        WHERE identificacion = ?
        """,
        (
            identificacion.strip().upper(),
        )
    )

    fila = cursor.fetchone()

    if fila is None:
        return None

    return Paciente(
        fila["identificacion"],
        fila["nombre"],
        fila["edad"],
        fila["telefono"],
    )


def listar_pacientes(conexion):
    """
    Devuelve todos los pacientes registrados.
    """

    cursor = conexion.execute(
        """
        SELECT
            identificacion,
            nombre,
            edad,
            telefono
        FROM pacientes
        ORDER BY identificacion
        """
    )

    pacientes = []

    for fila in cursor.fetchall():
        pacientes.append(
            Paciente(
                fila["identificacion"],
                fila["nombre"],
                fila["edad"],
                fila["telefono"],
            )
        )

    return pacientes


def actualizar_paciente(conexion, paciente):
    """
    Actualiza los datos de un paciente.
    """

    cursor = conexion.execute(
        """
        UPDATE pacientes
        SET
            nombre = ?,
            edad = ?,
            telefono = ?
        WHERE identificacion = ?
        """,
        (
            paciente.nombre,
            paciente.edad,
            paciente.telefono,
            paciente.identificacion,
        )
    )

    conexion.commit()

    return cursor.rowcount > 0


def eliminar_paciente(conexion, identificacion):
    """
    Elimina un paciente de la base de datos.
    """

    cursor = conexion.execute(
        """
        DELETE FROM pacientes
        WHERE identificacion = ?
        """,
        (
            identificacion.strip().upper(),
        )
    )

    conexion.commit()

    return cursor.rowcount > 0


# ==========================================================
# CITAS
# ==========================================================

def guardar_cita(conexion, cita):
    """
    Guarda una cita asociada con un paciente.
    """

    conexion.execute(
        """
        INSERT INTO citas (
            codigo,
            fecha,
            hora,
            profesional,
            paciente_id,
            motivo,
            observaciones
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            cita.codigo,
            cita.fecha,
            cita.hora,
            cita.profesional,
            cita.paciente.identificacion,
            cita.motivo,
            cita.observaciones,
        )
    )

    conexion.commit()


def buscar_cita_db(conexion, codigo):
    """
    Busca una cita mediante su código.
    """

    cursor = conexion.execute(
        """
        SELECT
            codigo,
            fecha,
            hora,
            profesional,
            paciente_id,
            motivo,
            observaciones
        FROM citas
        WHERE codigo = ?
        """,
        (
            codigo.strip().upper(),
        )
    )

    fila = cursor.fetchone()

    if fila is None:
        return None

    paciente = buscar_paciente_db(
        conexion,
        fila["paciente_id"]
    )

    cita = Cita(
        fila["codigo"],
        fila["fecha"],
        fila["hora"],
        fila["profesional"],
        paciente,
        fila["motivo"],
    )

    cita.registrar_atencion(
        fila["observaciones"]
    )

    return cita


def listar_citas(conexion):
    """
    Devuelve todas las citas registradas.
    """

    cursor = conexion.execute(
        """
        SELECT codigo
        FROM citas
        ORDER BY fecha, hora
        """
    )

    citas = []

    for fila in cursor.fetchall():
        cita = buscar_cita_db(
            conexion,
            fila["codigo"]
        )

        citas.append(cita)

    return citas


# ==========================================================
# MEDICAMENTOS
# ==========================================================

def guardar_medicamento(conexion, medicamento):
    """
    Guarda un medicamento y devuelve su ID.
    """

    cursor = conexion.execute(
        """
        INSERT INTO medicamentos (
            nombre,
            dosis,
            frecuencia
        )
        VALUES (?, ?, ?)
        """,
        (
            medicamento.nombre,
            medicamento.dosis,
            medicamento.frecuencia,
        )
    )

    conexion.commit()

    return cursor.lastrowid


def buscar_medicamento_db(conexion, medicamento_id):
    """
    Busca un medicamento mediante su ID.
    """

    cursor = conexion.execute(
        """
        SELECT
            id,
            nombre,
            dosis,
            frecuencia
        FROM medicamentos
        WHERE id = ?
        """,
        (
            medicamento_id,
        )
    )

    fila = cursor.fetchone()

    if fila is None:
        return None

    return Medicamento(
        fila["nombre"],
        fila["dosis"],
        fila["frecuencia"],
    )


def listar_medicamentos(conexion):
    """
    Devuelve todos los medicamentos registrados.
    """

    cursor = conexion.execute(
        """
        SELECT
            nombre,
            dosis,
            frecuencia
        FROM medicamentos
        ORDER BY nombre
        """
    )

    medicamentos = []

    for fila in cursor.fetchall():
        medicamentos.append(
            Medicamento(
                fila["nombre"],
                fila["dosis"],
                fila["frecuencia"],
            )
        )

    return medicamentos


# ==========================================================
# RELACIÓN CITA - MEDICAMENTO
# ==========================================================

def asociar_medicamento_cita(
    conexion,
    cita_codigo,
    medicamento_id
):
    """
    Asocia un medicamento con una cita.
    """

    conexion.execute(
        """
        INSERT INTO cita_medicamentos (
            cita_codigo,
            medicamento_id
        )
        VALUES (?, ?)
        """,
        (
            cita_codigo,
            medicamento_id,
        )
    )

    conexion.commit()


def obtener_medicamentos_cita(
    conexion,
    cita_codigo
):
    """
    Devuelve los medicamentos asociados a una cita.
    """

    cursor = conexion.execute(
        """
        SELECT
            m.nombre,
            m.dosis,
            m.frecuencia
        FROM medicamentos m
        INNER JOIN cita_medicamentos cm
            ON m.id = cm.medicamento_id
        WHERE cm.cita_codigo = ?
        ORDER BY m.nombre
        """,
        (
            cita_codigo,
        )
    )

    medicamentos = []

    for fila in cursor.fetchall():
        medicamentos.append(
            Medicamento(
                fila["nombre"],
                fila["dosis"],
                fila["frecuencia"],
            )
        )

    return medicamentos