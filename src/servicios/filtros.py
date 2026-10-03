def filtrar_pacientes_por_nombre(pacientes, texto):
    """
    Filtra pacientes mediante una coincidencia
    parcial o total de nombre.
    """
    texto = texto.strip().lower()

    return [
        paciente
        for paciente in pacientes
        if texto in paciente.nombre.lower()
    ]


def buscar_paciente_por_id(pacientes, identificacion):
    """
    Busca un paciente mediante su identificación.
    """
    identificacion = identificacion.strip().upper()

    for paciente in pacientes:
        if paciente.identificacion.upper() == identificacion:
            return paciente

    return None


def consultar_citas_paciente(paciente):
    """
    Devuelve las citas asociadas al paciente.
    """
    return paciente.citas


def filtrar_citas_por_fecha(citas, fecha):
    """
    Devuelve las citas correspondientes
    a una fecha determinada.
    """
    return [
        cita
        for cita in citas
        if cita.fecha == fecha
    ]


def buscar_medicamentos_por_nombre(medicamentos, texto):
    """
    Busca medicamentos mediante una coincidencia
    parcial o total de nombre.
    """
    texto = texto.strip().lower()

    return [
        medicamento
        for medicamento in medicamentos
        if texto in medicamento.nombre.lower()
    ]


def obtener_pacientes_adultos(pacientes):
    """
    Devuelve los pacientes mayores o iguales a 18 años
    utilizando la función de orden superior filter().
    """
    return list(
        filter(
            lambda paciente: paciente.edad >= 18,
            pacientes
        )
    )


def obtener_nombres_pacientes(pacientes):
    """
    Devuelve una lista con los nombres de los pacientes
    utilizando la función de orden superior map().
    """
    return list(
        map(
            lambda paciente: paciente.nombre,
            pacientes
        )
    )