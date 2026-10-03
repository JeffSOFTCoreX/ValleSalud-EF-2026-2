def generar_reporte_general(
    pacientes,
    citas,
    medicamentos
):
    """Genera un reporte general en consola."""

    print(
        "\n========== REPORTE GENERAL VALLESALUD =========="
    )

    print(
        f"Total de pacientes registrados: "
        f"{len(pacientes)}"
    )

    print(
        f"Total de citas registradas: "
        f"{len(citas)}"
    )

    print(
        f"Total de medicamentos registrados: "
        f"{len(medicamentos)}"
    )

    print("\nPACIENTES")

    for paciente in pacientes:
        print(
            f"- {paciente.nombre} | "
            f"ID: {paciente.identificacion} | "
            f"Citas: {paciente.cantidad_citas()}"
        )

    print("\nCITAS")

    for cita in citas:
        print(
            f"- {cita.codigo} | "
            f"{cita.fecha} {cita.hora} | "
            f"{cita.paciente.nombre} | "
            f"{cita.profesional}"
        )

    print("\nMEDICAMENTOS")

    for medicamento in medicamentos:
        print(f"- {medicamento}")

    print(
        "==============================================="
    )