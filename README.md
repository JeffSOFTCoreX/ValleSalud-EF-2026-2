# Sistema ValleSalud

Proyecto académico del curso Lenguajes de Programación.

## Descripción

ValleSalud es un prototipo académico para la gestión básica de información de un centro de salud rural ficticio. El sistema integra diferentes componentes dentro de un mismo flujo, incluyendo registro y consulta de pacientes, gestión de citas y medicamentos, validaciones, persistencia local y control básico de permisos.

La versión final implementa Programación Orientada a Objetos y programación funcional. La programación orientada a eventos y una posible interfaz gráfica fueron analizadas durante el diseño, pero no forman parte de la implementación final por consola.

## Tecnologías utilizadas

- Python 3.x
- SQLite
- `unittest`
- Git y GitHub

## Paradigmas aplicados

### Programación Orientada a Objetos

Se utiliza para representar las principales entidades del sistema mediante clases, atributos, métodos, encapsulamiento, herencia y relaciones entre objetos.

Clases principales:

- `Paciente`
- `Cita`
- `Medicamento`
- `Usuario`
- `UsuarioAdministrativo`
- `UsuarioAsistencial`

### Programación funcional

Se utiliza para realizar consultas y transformaciones sobre colecciones de objetos, incluyendo el uso de funciones de orden superior como `filter()` y `map()`.

### Programación orientada a eventos

Fue evaluada como alternativa para una posible interfaz gráfica, pero no se implementó en la versión final porque el módulo funciona por consola.

## Patrones de diseño

- **Singleton:** gestiona una única instancia de conexión SQLite mediante `ConexionSingleton`.
- **Factory:** `UsuarioFactory` crea usuarios según su rol.

## Funcionalidades principales

- Registro y consulta de pacientes.
- Gestión de citas.
- Registro y consulta de medicamentos y asociación de medicamentos a citas.
- Validación de entradas y manejo controlado de excepciones.
- Búsquedas y filtros, incluyendo `filter()` y `map()`.
- Persistencia local en SQLite.
- Roles y permisos básicos.
- Generación de reporte general.
- Pruebas automatizadas.

## Estructura del proyecto

```text
ValleSalud-EF-2026-2/
├── src/
│   ├── dominio/        Clases principales del sistema
│   ├── servicios/      Consultas, filtros, reportes y validaciones
│   ├── persistencia/   Conexión SQLite y repositorios
│   ├── patrones/       Singleton y Factory
│   └── main.py         Demostración integrada del sistema
├── tests/              Pruebas automatizadas
├── data/               Ubicación de la base local de prueba
├── docs/
│   ├── uml/            Diagrama UML final
│   └── evidencias/     Capturas reales de ejecución, funcionalidades y pruebas
├── requirements.txt
└── README.md
```

## Ejecución

Desde la carpeta raíz del repositorio, ejecutar:

```bash
python -m src.main
```

La demostración se ejecuta en consola. La conexión SQLite predeterminada utiliza `data/vallesalud.db`; los archivos de base local están excluidos del control de versiones.

## Pruebas automatizadas

Para ejecutar toda la suite:

```bash
python -m unittest discover tests -v
```

**Resultado verificado:** `Ran 34 tests` y `OK`. Las pruebas cubren dominio, consultas, validaciones, persistencia, patrones de diseño, roles y permisos.

## UML

El diagrama UML final se encuentra en `docs/uml/`. Representa clases, atributos, métodos, relaciones y los patrones Singleton y Factory de acuerdo con la implementación final.

## Evidencias

La carpeta `docs/evidencias/` contiene siete capturas reales agregadas al repositorio:

- **Ejecución del programa principal:** `01_ejecucion_main.png.jpg` y `01b_ejecucion_main_final.jpg`.
- **Programación funcional con `filter()` y `map()`:** `02_filter_map.png.jpg`.
- **Manejo de una entrada inválida (`ValueError`):** `03_valueerror.png.jpg`.
- **Singleton y persistencia en SQLite:** `04_singleton_persistencia_sqlite.png.jpg`.
- **Factory, roles y permisos:** `05_factory_roles.png.jpg`.
- **Pruebas automatizadas:** `06_tests_34_ok.png.jpg`, que muestra `Ran 34 tests` y `OK`.

La descripción completa de las capturas está en [`docs/evidencias/README.md`](docs/evidencias/README.md).

## Datos y alcance

El proyecto utiliza exclusivamente datos ficticios creados con fines académicos. No se deben incorporar credenciales, contraseñas, tokens, claves privadas ni datos personales reales.

ValleSalud es un prototipo académico y no constituye un sistema clínico listo para producción. No incluye historia clínica electrónica completa, autenticación clínica avanzada, interoperabilidad con sistemas externos, infraestructura en nube ni operación multisede.
