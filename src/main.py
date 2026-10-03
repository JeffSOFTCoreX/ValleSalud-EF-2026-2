from src.dominio import (
    Paciente,
    Cita,
    Medicamento,
)

from src.servicios import (
    filtrar_pacientes_por_nombre,
    buscar_paciente_por_id,
    consultar_citas_paciente,
    filtrar_citas_por_fecha,
    buscar_medicamentos_por_nombre,
    obtener_pacientes_adultos,
    obtener_nombres_pacientes,
    generar_reporte_general,
)

from src.persistencia import (
    crear_tablas,
    guardar_paciente,
    buscar_paciente_db,
    guardar_cita,
    buscar_cita_db,
    guardar_medicamento,
    asociar_medicamento_cita,
    obtener_medicamentos_cita,
)

from src.patrones import (
    ConexionSingleton,
    UsuarioFactory,
)


# ==========================================================
# DATOS FICTICIOS
# ==========================================================

def crear_datos_ficticios():
    """
    Crea los datos ficticios utilizados
    en la demostración y las pruebas.
    """

    juan = Paciente(
        "P001",
        "Juan Perez",
        35,
        "300-000-0001"
    )

    maria = Paciente(
        "P002",
        "Maria Lopez",
        29,
        "300-000-0002"
    )

    carlos = Paciente(
        "P003",
        "Carlos Ramirez",
        42,
        "300-000-0003"
    )

    acetaminofen = Medicamento(
        "Acetaminofen",
        "500 mg",
        "cada 8 horas"
    )

    loratadina = Medicamento(
        "Loratadina",
        "10 mg",
        "una vez al día"
    )

    ibuprofeno = Medicamento(
        "Ibuprofeno",
        "400 mg",
        "cada 8 horas"
    )

    cita_1 = Cita(
        "C001",
        "2026-10-05",
        "09:00",
        "Dra. Ana Gomez",
        juan,
        "Consulta general"
    )

    cita_2 = Cita(
        "C002",
        "2026-10-05",
        "10:30",
        "Dr. Luis Torres",
        maria,
        "Dolor de cabeza"
    )

    cita_3 = Cita(
        "C003",
        "2026-10-06",
        "08:30",
        "Dra. Ana Gomez",
        carlos,
        "Control médico"
    )

    juan.agregar_cita(
        cita_1
    )

    maria.agregar_cita(
        cita_2
    )

    carlos.agregar_cita(
        cita_3
    )

    cita_1.registrar_atencion(
        "Síntomas de resfriado común. "
        "Se recomienda reposo."
    )

    cita_2.registrar_atencion(
        "Paciente estable. "
        "Se indica control de síntomas."
    )

    cita_3.registrar_atencion(
        "Control general sin observaciones relevantes."
    )

    cita_1.agregar_medicamento(
        acetaminofen
    )

    cita_1.agregar_medicamento(
        loratadina
    )

    cita_2.agregar_medicamento(
        ibuprofeno
    )

    pacientes = [
        juan,
        maria,
        carlos
    ]

    citas = [
        cita_1,
        cita_2,
        cita_3
    ]

    medicamentos = [
        acetaminofen,
        loratadina,
        ibuprofeno
    ]

    return (
        pacientes,
        citas,
        medicamentos
    )


# ==========================================================
# DEMOSTRACIÓN DEL SISTEMA
# ==========================================================

def demostrar_sistema():
    """
    Ejecuta una demostración integrada
    del Sistema ValleSalud.
    """

    print(
        "\n==============================================="
    )

    print(
        "       SISTEMA VALLESALUD"
    )

    print(
        "       DEMOSTRACIÓN INTEGRADA"
    )

    print(
        "==============================================="
    )

    pacientes, citas, medicamentos = (
        crear_datos_ficticios()
    )

    juan = pacientes[0]
    maria = pacientes[1]

    # ======================================================
    # 1. PROGRAMACIÓN ORIENTADA A OBJETOS
    # ======================================================

    print(
        "\n1. PROGRAMACIÓN ORIENTADA A OBJETOS"
    )

    print(
        "Pacientes registrados:"
    )

    for paciente in pacientes:
        print(
            paciente
        )

    print(
        "\nRelación entre paciente y cita:"
    )

    print(
        f"{juan.nombre} tiene "
        f"{juan.cantidad_citas()} cita(s)."
    )

    print(
        f"La cita {citas[0].codigo} pertenece a "
        f"{citas[0].paciente.nombre}."
    )

    print(
        f"Medicamentos asociados a la cita "
        f"{citas[0].codigo}: "
        f"{len(citas[0].medicamentos)}"
    )

    # ======================================================
    # 2. FILTROS Y CONSULTAS
    # ======================================================

    print(
        "\n2. FILTROS Y CONSULTAS"
    )

    resultado = filtrar_pacientes_por_nombre(
        pacientes,
        "Juan"
    )

    print(
        "\nFiltro por nombre 'Juan':"
    )

    for paciente in resultado:
        print(
            paciente
        )

    encontrado = buscar_paciente_por_id(
        pacientes,
        "P002"
    )

    print(
        "\nBúsqueda por ID P002:"
    )

    if encontrado:
        print(
            encontrado
        )
    else:
        print(
            "Paciente no encontrado."
        )

    print(
        "\nCitas de Juan Perez:"
    )

    for cita in consultar_citas_paciente(
        juan
    ):
        print(
            cita
        )

    print(
        "\nCitas del 2026-10-05:"
    )

    for cita in filtrar_citas_por_fecha(
        citas,
        "2026-10-05"
    ):
        print(
            cita
        )

    print(
        "\nBúsqueda de medicamento:"
    )

    for medicamento in buscar_medicamentos_por_nombre(
        medicamentos,
        "Loratadina"
    ):
        print(
            medicamento
        )

    # ======================================================
    # 3. PROGRAMACIÓN FUNCIONAL
    # ======================================================

    print(
        "\n3. PROGRAMACIÓN FUNCIONAL"
    )

    adultos = obtener_pacientes_adultos(
        pacientes
    )

    print(
        "\nPacientes adultos usando filter():"
    )

    for paciente in adultos:
        print(
            f"- {paciente.nombre} | "
            f"Edad: {paciente.edad}"
        )

    nombres = obtener_nombres_pacientes(
        pacientes
    )

    print(
        "\nNombres obtenidos usando map():"
    )

    for nombre in nombres:
        print(
            f"- {nombre}"
        )

    # ======================================================
    # 4. VALIDACIONES Y MANEJO DE EXCEPCIONES
    # ======================================================

    print(
        "\n4. VALIDACIONES Y MANEJO DE EXCEPCIONES"
    )

    try:
        Paciente(
            "",
            "",
            -5,
            ""
        )

    except ValueError as error:
        print(
            "Entrada inválida detectada correctamente:"
        )

        print(
            f"- {error}"
        )

    # ======================================================
    # 5. PATRÓN SINGLETON Y SQLITE
    # ======================================================

    print(
        "\n5. SINGLETON Y PERSISTENCIA SQLITE"
    )

    singleton_1 = ConexionSingleton(
        ":memory:"
    )

    singleton_2 = ConexionSingleton(
        ":memory:"
    )

    print(
        "¿Las dos variables utilizan la misma "
        "instancia Singleton?"
    )

    print(
        singleton_1 is singleton_2
    )

    conexion = singleton_1.obtener_conexion()

    crear_tablas(
        conexion
    )

    print(
        "Tablas SQLite creadas correctamente."
    )

    # Guardar pacientes

    for paciente in pacientes:
        guardar_paciente(
            conexion,
            paciente
        )

    print(
        f"{len(pacientes)} pacientes guardados "
        "en SQLite."
    )

    paciente_db = buscar_paciente_db(
        conexion,
        "P001"
    )

    print(
        "\nPaciente recuperado desde SQLite:"
    )

    print(
        paciente_db
    )

    # Guardar citas

    for cita in citas:
        guardar_cita(
            conexion,
            cita
        )

    print(
        f"{len(citas)} citas guardadas en SQLite."
    )

    cita_db = buscar_cita_db(
        conexion,
        "C001"
    )

    print(
        "\nCita recuperada desde SQLite:"
    )

    print(
        cita_db
    )

    # Guardar medicamentos

    medicamentos_ids = []

    for medicamento in medicamentos:
        medicamento_id = guardar_medicamento(
            conexion,
            medicamento
        )

        medicamentos_ids.append(
            medicamento_id
        )

    print(
        f"{len(medicamentos)} medicamentos "
        "guardados en SQLite."
    )

    # Asociar medicamentos a C001

    asociar_medicamento_cita(
        conexion,
        "C001",
        medicamentos_ids[0]
    )

    asociar_medicamento_cita(
        conexion,
        "C001",
        medicamentos_ids[1]
    )

    medicamentos_cita = obtener_medicamentos_cita(
        conexion,
        "C001"
    )

    print(
        "\nMedicamentos recuperados "
        "de la cita C001:"
    )

    for medicamento in medicamentos_cita:
        print(
            f"- {medicamento}"
        )

    # ======================================================
    # 6. PATRÓN FACTORY
    # ======================================================

    print(
        "\n6. PATRÓN FACTORY Y ROLES"
    )

    administrativo = UsuarioFactory.crear_usuario(
        "administrativo",
        "U001",
        "Carlos Administrativo"
    )

    asistencial = UsuarioFactory.crear_usuario(
        "asistencial",
        "U002",
        "Ana Asistencial"
    )

    print(
        administrativo
    )

    print(
        asistencial
    )

    print(
        "\nPermisos:"
    )

    print(
        "Administrativo puede programar cita:",
        administrativo.tiene_permiso(
            "programar_cita"
        )
    )

    print(
        "Administrativo puede registrar atención:",
        administrativo.tiene_permiso(
            "registrar_atencion"
        )
    )

    print(
        "Asistencial puede registrar atención:",
        asistencial.tiene_permiso(
            "registrar_atencion"
        )
    )

    print(
        "Asistencial puede generar reporte:",
        asistencial.tiene_permiso(
            "generar_reporte"
        )
    )

    # ======================================================
    # 7. REPORTE GENERAL
    # ======================================================

    print(
        "\n7. REPORTE GENERAL"
    )

    generar_reporte_general(
        pacientes,
        citas,
        medicamentos
    )

    # ======================================================
    # 8. VALIDACIONES AUTOMÁTICAS
    # ======================================================

    print(
        "\n8. VALIDACIONES AUTOMÁTICAS"
    )

    assert len(
        filtrar_pacientes_por_nombre(
            pacientes,
            "Juan"
        )
    ) == 1

    assert buscar_paciente_por_id(
        pacientes,
        "P002"
    ) is maria

    assert len(
        consultar_citas_paciente(
            juan
        )
    ) == 1

    assert len(
        filtrar_citas_por_fecha(
            citas,
            "2026-10-05"
        )
    ) == 2

    assert len(
        buscar_medicamentos_por_nombre(
            medicamentos,
            "Loratadina"
        )
    ) == 1

    assert len(
        obtener_pacientes_adultos(
            pacientes
        )
    ) == 3

    assert obtener_nombres_pacientes(
        pacientes
    ) == [
        "Juan Perez",
        "Maria Lopez",
        "Carlos Ramirez",
    ]

    assert paciente_db is not None

    assert cita_db is not None

    assert len(
        medicamentos_cita
    ) == 2

    assert singleton_1 is singleton_2

    print(
        "Resultado: todas las validaciones "
        "finalizaron correctamente."
    )

    # ======================================================
    # FINAL
    # ======================================================

    print(
        "\n==============================================="
    )

    print(
        "DEMOSTRACIÓN FINALIZADA CORRECTAMENTE"
    )

    print(
        "==============================================="
    )

    singleton_1.cerrar_conexion()


if __name__ == "__main__":
    demostrar_sistema()