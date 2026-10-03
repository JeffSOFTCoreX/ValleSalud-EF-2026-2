def validar_texto_obligatorio(valor, nombre_campo):
    """
    Valida que un campo de texto tenga contenido.
    """
    if valor is None or str(valor).strip() == "":
        raise ValueError(
            f"El campo {nombre_campo} es obligatorio."
        )

    return str(valor).strip()


def validar_identificacion(identificacion):
    """
    Valida que la identificación tenga contenido.
    """
    identificacion = validar_texto_obligatorio(
        identificacion,
        "identificación"
    )

    return identificacion.upper()


def validar_nombre(nombre):
    """
    Valida que el nombre tenga contenido
    y una longitud mínima.
    """
    nombre = validar_texto_obligatorio(
        nombre,
        "nombre"
    )

    if len(nombre) < 3:
        raise ValueError(
            "El nombre debe tener al menos 3 caracteres."
        )

    return nombre


def validar_edad(edad):
    """
    Valida que la edad sea un número entero
    dentro de un rango permitido.
    """
    if not isinstance(edad, int):
        raise ValueError(
            "La edad debe ser un número entero."
        )

    if edad < 0 or edad > 120:
        raise ValueError(
            "La edad debe estar entre 0 y 120 años."
        )

    return edad


def validar_telefono(telefono):
    """
    Valida que el teléfono tenga contenido.
    """
    telefono = validar_texto_obligatorio(
        telefono,
        "teléfono"
    )

    if len(telefono) < 7:
        raise ValueError(
            "El teléfono debe tener al menos 7 caracteres."
        )

    return telefono


def validar_fecha(fecha):
    """
    Valida que la fecha tenga contenido.
    """
    return validar_texto_obligatorio(
        fecha,
        "fecha"
    )


def validar_hora(hora):
    """
    Valida que la hora tenga contenido.
    """
    return validar_texto_obligatorio(
        hora,
        "hora"
    )