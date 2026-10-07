# Sistema ValleSalud

Proyecto del curso Lenguajes de Programación.

## Descripción

ValleSalud es un prototipo académico para la gestión básica de información de un centro de salud rural ficticio.

El sistema integra diferentes componentes dentro de un mismo flujo, incluyendo registro y consulta de pacientes, gestión de citas y medicamentos, validación de entradas, persistencia local con SQLite, control básico de roles y permisos, patrones de diseño y pruebas automatizadas.

La versión final implementa Programación Orientada a Objetos y programación funcional. La programación orientada a eventos fue analizada durante el diseño, pero no forma parte de la implementación final debido a que el módulo funciona mediante consola.

## Tecnologías utilizadas

- Python 3.x
- SQLite
- `unittest`
- Git
- GitHub

## Paradigmas aplicados

### Programación Orientada a Objetos

Se utiliza para representar las entidades principales del sistema mediante clases, atributos, métodos, encapsulamiento, herencia y relaciones entre objetos.

Las principales entidades son:

- `Paciente`
- `Cita`
- `Medicamento`
- `Usuario`
- `UsuarioAdministrativo`
- `UsuarioAsistencial`

### Programación funcional

Se utiliza para realizar consultas, filtros y transformaciones sobre colecciones de objetos.

La implementación utiliza funciones de orden superior como:

- `filter()`
- `map()`

### Programación orientada a eventos

Fue analizada como una alternativa para una posible interfaz gráfica. Sin embargo, no se incorporó en la versión final porque el sistema funciona mediante consola y los criterios de aceptación definidos no requieren una interfaz basada en eventos.

## Patrones de diseño

El proyecto utiliza dos patrones de diseño:

- **Singleton:** permite administrar una única instancia de conexión SQLite mediante `ConexionSingleton`.
- **Factory:** permite crear usuarios administrativos o asistenciales mediante `UsuarioFactory`, según el rol solicitado.

## Funcionalidades principales

El prototipo permite:

- Registrar y consultar pacientes.
- Gestionar citas vinculadas con pacientes.
- Registrar información básica de atención.
- Registrar y consultar medicamentos.
- Asociar medicamentos a citas.
- Buscar y filtrar información.
- Aplicar transformaciones mediante `filter()` y `map()`.
- Validar entradas.
- Manejar excepciones de forma controlada.
- Guardar y recuperar información mediante SQLite.
- Diferenciar permisos según el rol del usuario.
- Generar un reporte general.
- Ejecutar pruebas automatizadas.

## Estructura del proyecto

```text
ValleSalud-EF-2026-2/
│
├── src/
│   ├── dominio/        Clases principales del sistema
│   ├── servicios/      Consultas, filtros, reportes y validaciones
│   ├── persistencia/   Conexión SQLite y repositorios
│   ├── patrones/       Singleton y Factory
│   └── main.py         Demostración integrada del sistema
│
├── tests/              Pruebas automatizadas
├── data/               Datos o base SQLite local
│
├── docs/
│   ├── uml/            Diagrama UML definitivo
│   ├── informe/        Documentación del informe
│   ├── declaracion_ia/ Declaración institucional de uso de IA
│   └── evidencias/     Evidencias de ejecución y pruebas
│
├── requirements.txt
├── ESTRUCTURA_REPOSITORIO.txt
├── INSTRUCCIONES_EQUIPO.md
└── README.md
```

## Requisitos

Para ejecutar el proyecto se requiere:

- Python 3.x.
- Git, únicamente si se desea clonar el repositorio.

La versión actual utiliza principalmente módulos incluidos en la biblioteca estándar de Python, entre ellos `sqlite3` y `unittest`.

## Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/JeffSOFTCoreX/ValleSalud-EF-2026-2.git
```

2. Ingresar a la carpeta del proyecto:

```bash
cd ValleSalud-EF-2026-2
```

3. Verificar la instalación de Python:

```bash
python --version
```

No se requiere configurar un servidor de base de datos externo, ya que el proyecto utiliza SQLite.

## Ejecución

Desde la carpeta raíz del repositorio ejecutar:

```bash
python -m src.main
```

La demostración principal integra en un mismo flujo:

- creación de pacientes, citas y medicamentos;
- relaciones entre objetos;
- consultas y filtros;
- programación funcional mediante `filter()` y `map()`;
- validación de entradas;
- manejo de excepciones;
- persistencia SQLite;
- patrones Singleton y Factory;
- roles y permisos;
- generación del reporte general.

## Pruebas automatizadas

Para ejecutar toda la suite de pruebas:

```bash
python -m unittest discover -s tests -v
```

Las pruebas verifican componentes del dominio, consultas, filtros, validaciones, persistencia, patrones de diseño, roles y permisos.

En la ejecución final del equipo se obtuvieron:

```text
Ran 34 tests

OK
```

Esto corresponde a 34 pruebas ejecutadas correctamente, sin errores ni fallos.

## Persistencia

La aplicación utiliza SQLite para almacenar la información de las entidades principales.

La capa de persistencia administra pacientes, citas y medicamentos, así como las relaciones correspondientes.

Durante las pruebas puede utilizarse una base de datos en memoria mediante `:memory:` para ejecutar escenarios reproducibles sin generar archivos residuales.

## UML

El diagrama UML definitivo del proyecto se almacena en:

```text
docs/uml/
```

El modelo debe representar únicamente las clases correspondientes a la implementación final, incluyendo sus relaciones, multiplicidades y los patrones Singleton y Factory.

## Evidencias

Las evidencias de ejecución del sistema y de las pruebas automatizadas se almacenan en:

```text
docs/evidencias/
```

Estas evidencias permiten comprobar el funcionamiento de la demostración principal, la programación funcional, el manejo de excepciones, la persistencia, los patrones de diseño, los roles y la ejecución de las pruebas automatizadas.

## Datos personales

El proyecto utiliza exclusivamente datos ficticios creados con fines académicos.

No deben incorporarse al repositorio:

- datos personales reales;
- contraseñas;
- tokens;
- credenciales;
- claves privadas;
- información sensible.

## Alcance

ValleSalud es un prototipo académico y no constituye un sistema clínico listo para producción.

La versión actual no incluye historia clínica electrónica completa, autenticación clínica avanzada, interoperabilidad con sistemas externos de salud, infraestructura en nube, laboratorio, imágenes médicas, facturación ni operación multisede.