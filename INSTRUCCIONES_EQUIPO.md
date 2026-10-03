# Instrucciones para integrar los aportes del equipo

## Regla principal
No crear archivos separados por integrante dentro de `src/`.
Cada integrante debe colocar su aporte en el módulo que corresponda para que el proyecto quede integrado.

## Dónde colocar cada tipo de trabajo

### Programación Orientada a Objetos
Colocar clases en:
`src/dominio/`

Ejemplos:
- Paciente -> `src/dominio/paciente.py`
- Cita -> `src/dominio/cita.py`
- Medicamento -> `src/dominio/medicamento.py`

### Programación funcional
Colocar filtros, búsquedas, transformaciones y reportes en:
`src/servicios/`

### Validaciones y manejo de errores
Colocar reglas comunes en:
`src/servicios/validaciones.py`

### Persistencia
Colocar conexión SQLite y repositorios en:
`src/persistencia/`

### Patrones de diseño
Colocar Singleton, Factory u otros patrones realmente implementados en:
`src/patrones/`

### Eventos o interfaz
Colocar eventos o controladores en:
`src/eventos/`

### Pruebas
Toda prueba automatizada debe ir en:
`tests/`

### Evidencias
Capturas, resultados de consola y material gráfico:
`docs/evidencias/`

### UML
Diagramas y archivos fuente del modelado:
`docs/uml/`

## Antes de hacer commit
1. Descargar o actualizar la última versión del repositorio.
2. Ejecutar el código.
3. Ejecutar las pruebas.
4. Verificar que no se suban datos reales, contraseñas ni credenciales.
5. Escribir un commit descriptivo en español.
