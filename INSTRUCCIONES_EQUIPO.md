# Instrucciones del equipo - ValleSalud

## Objetivo

Mantener el proyecto ValleSalud organizado, integrado y coherente entre el código, las pruebas, el UML, el informe y las evidencias.

La versión final del proyecto implementa Programación Orientada a Objetos y programación funcional dentro de un flujo integrado ejecutado por consola.

## Organización del proyecto

### Código fuente

El código principal se encuentra en:

```text
src/
```

La estructura se divide en:

- `src/dominio/`: clases principales del sistema.
- `src/servicios/`: consultas, filtros, reportes y validaciones.
- `src/persistencia/`: conexión y operaciones con SQLite.
- `src/patrones/`: patrones Singleton y Factory.
- `src/main.py`: demostración integrada del sistema.

### Dominio

Las entidades principales son:

- `Paciente`
- `Cita`
- `Medicamento`
- `Usuario`
- `UsuarioAdministrativo`
- `UsuarioAsistencial`

Las relaciones entre estas clases deben mantenerse coherentes con el diagrama UML definitivo.

### Servicios

El módulo de servicios contiene:

- búsquedas;
- filtros;
- transformaciones;
- reportes;
- validaciones.

La programación funcional se evidencia mediante el uso de `filter()` y `map()` sobre colecciones del sistema.

### Persistencia

La persistencia se implementa mediante SQLite.

Las operaciones relacionadas con almacenamiento deben mantenerse dentro de:

```text
src/persistencia/
```

No se deben colocar sentencias SQL directamente dentro de las clases del dominio.

### Patrones de diseño

Los patrones implementados son:

- **Singleton**, utilizado para administrar la conexión SQLite.
- **Factory**, utilizado para crear usuarios según el rol solicitado.

Los archivos correspondientes se encuentran en:

```text
src/patrones/
```

### Programación orientada a eventos

La programación orientada a eventos fue analizada como alternativa durante el diseño, pero no forma parte de la implementación final.

No se debe crear nuevamente una carpeta `src/eventos/` salvo que el alcance del proyecto cambie oficialmente.

## Ejecución

Desde la carpeta raíz del proyecto ejecutar:

```bash
python -m src.main
```

La demostración debe permitir verificar:

- creación de pacientes, citas y medicamentos;
- relaciones entre objetos;
- búsquedas y filtros;
- uso de `filter()` y `map()`;
- validaciones;
- manejo de excepciones;
- persistencia SQLite;
- Singleton;
- Factory;
- roles y permisos;
- generación de reportes.

## Pruebas automatizadas

Las pruebas se encuentran en:

```text
tests/
```

Para ejecutar la suite completa:

```bash
python -m unittest discover -s tests -v
```

La ejecución final debe mantenerse sin errores ni fallos.

Actualmente la suite está compuesta por 34 pruebas automatizadas.

## Documentación

La documentación del proyecto se organiza en:

```text
docs/
```

### UML

```text
docs/uml/
```

Debe contener el diagrama UML correspondiente únicamente a la versión final implementada.

### Evidencias

```text
docs/evidencias/
```

Debe contener evidencias de:

- ejecución de `main.py`;
- programación funcional;
- manejo de `ValueError`;
- Singleton;
- persistencia SQLite;
- Factory;
- roles;
- ejecución completa de las pruebas.

### Informe

```text
docs/informe/
```

Se utiliza para almacenar la versión final del informe cuando corresponda.

### Declaración de IA

```text
docs/declaracion_ia/
```

Debe contener la declaración institucional de uso de Inteligencia Artificial solicitada para la evaluación.

## Reglas antes de realizar un commit

Antes de realizar cambios en la rama compartida:

1. Verificar que la copia local esté actualizada.
2. Revisar los archivos modificados con:

```bash
git status
```

3. Ejecutar la demostración:

```bash
python -m src.main
```

4. Ejecutar las pruebas:

```bash
python -m unittest discover -s tests -v
```

5. Confirmar que no se hayan incorporado:
   - contraseñas;
   - tokens;
   - credenciales;
   - datos personales reales;
   - archivos temporales innecesarios.

6. Verificar que los cambios sean coherentes con el UML y el informe.

7. Utilizar mensajes de commit descriptivos y relacionados con el cambio realizado.

## Reglas para la versión final

No se deben incorporar funcionalidades que no puedan demostrarse mediante código o evidencias.

No se deben mantener archivos antiguos que describan componentes eliminados.

Los cambios finales deben conservar la trazabilidad entre:

```text
Requerimientos
      ↓
Diseño UML
      ↓
Código
      ↓
Pruebas
      ↓
Evidencias
      ↓
Informe
```

ValleSalud debe presentarse como un prototipo académico y no como un sistema clínico listo para producción.