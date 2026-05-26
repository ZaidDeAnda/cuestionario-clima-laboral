# Cuestionario de Clima Laboral

Aplicación desarrollada en **Streamlit** para capturar una pre-evaluación de clima laboral de la Secretaría de Igualdad e Inclusión.

## Descripción

Este proyecto contiene un formulario interactivo para levantar información sobre la percepción del clima laboral dentro de la institución.

La aplicación solicita una contraseña de acceso, muestra un cuestionario dividido por dimensiones organizacionales y almacena las respuestas en **MongoDB**.

El cuestionario evalúa temas como liderazgo, crecimiento profesional, trabajo en equipo, beneficios, satisfacción laboral, comunicación, inclusión e igualdad de género.

## Funcionalidades principales

- Acceso mediante contraseña.
- Captura de área, subsecretaría o dirección del participante.
- Formulario con preguntas por dimensión.
- Respuestas mediante sliders con opciones:
  - Siempre
  - A veces
  - Nunca
- Registro del usuario autenticado.
- Almacenamiento de respuestas en MongoDB.
- Configuración de conexión mediante archivo `config.yml`.

## Archivos principales

```text
.
├── README.md
├── app.py
├── requirements.txt
├── .gitignore
└── utils
    ├── authentication.py
    ├── config.py
    └── database.py
```

## Archivos principales del proyecto

### `app.py`

Aplicación principal de Streamlit.

Contiene:

- Configuración de página.
- Encabezado del cuestionario.
- Validación de acceso mediante `check_password()`.
- Formulario de clima laboral.
- Captura de respuestas por dimensión.
- Inserción de respuestas en MongoDB.

Las respuestas se guardan en:

```text
ambiente_laboral
└── formulario_slider
```

### `utils/authentication.py`

Contiene la lógica de autenticación.

La función `check_password()` consulta MongoDB para validar si la contraseña ingresada existe en la colección de usuarios.

La colección esperada es:

```text
ambiente_laboral
└── usuarios
```

Si la contraseña es válida, el sistema guarda el usuario en la sesión de Streamlit.

### `utils/config.py`

Contiene la clase `Config`, encargada de leer el archivo de configuración `config.yml`.

Por defecto, el sistema busca el archivo:

```text
config.yml
```

en la raíz del proyecto.

### `utils/database.py`

Contiene la función `get_mongo_client(config)`, que construye la conexión a MongoDB usando las credenciales definidas en `config.yml`.

### `requirements.txt`

Archivo con las dependencias necesarias para ejecutar el proyecto.

Incluye:

```text
streamlit
pymongo
pyyaml
```

## Requisitos

Para ejecutar el proyecto se recomienda contar con Python 3.8 o superior.

Instala las dependencias con:

```bash
pip install -r requirements.txt
```

O manualmente:

```bash
pip install streamlit pymongo pyyaml
```

## Configuración requerida

Para que el proyecto funcione correctamente, es necesario crear un archivo llamado:

```text
config.yml
```

en la raíz del repositorio.

Este archivo debe contener las credenciales de conexión a MongoDB.

## Formato requerido de `config.yml`

```yaml
db_mongo:
  user: "TU_USUARIO_MONGO"
  password: "TU_PASSWORD_MONGO"
  cluster: "TU_CLUSTER_MONGO"
```

## Ejemplo de `config.yml`

```yaml
db_mongo:
  user: "usuario_demo"
  password: "password_demo"
  cluster: "cluster0.xxxxx.mongodb.net"
```

La conexión a MongoDB se construye con el siguiente formato:

```python
mongodb+srv://{user}:{password}@{cluster}/?retryWrites=true&w=majority
```

## Base de datos esperada en MongoDB

El proyecto espera trabajar con una base de datos llamada:

```text
ambiente_laboral
```

Con al menos las siguientes colecciones:

```text
ambiente_laboral
├── usuarios
└── formulario_slider
```

### Colección `usuarios`

La colección `usuarios` se utiliza para validar el acceso al cuestionario.

Ejemplo de documento:

```json
{
  "user": "usuario_demo",
  "password": "clave_demo"
}
```

El sistema valida únicamente la contraseña ingresada y, si existe un documento asociado, toma el campo `user` como usuario de sesión.

### Colección `formulario_slider`

La colección `formulario_slider` almacena las respuestas enviadas por los participantes.

Ejemplo de documento:

```json
{
  "user": "usuario_demo",
  "secretaria": "Dirección o subsecretaría",
  "liderazgo_1": "Siempre",
  "liderazgo_2": "A veces",
  "liderazgo_3": "Nunca",
  "crecimiento_1": "A veces",
  "equipo_1": "Siempre",
  "beneficios_1": "Nunca",
  "satisfaccion_1": "A veces",
  "comunicacion_1": "Siempre",
  "inclusion_1": "Siempre",
  "igualdad_1": "A veces"
}
```

## Dimensiones evaluadas

El cuestionario está organizado en las siguientes dimensiones:

```text
Liderazgo
Crecimiento y desarrollo
Trabajo en equipo
Beneficio y recompensas
Satisfacción laboral
Comunicación
Inclusión
Igualdad de género
```

## Preguntas por dimensión

### Liderazgo

Evalúa aspectos relacionados con:

- Transmisión de valores, misión y objetivos.
- Claridad de tareas y objetivos.
- Trato justo y ausencia de favoritismos.
- Retroalimentación del jefe inmediato.

### Crecimiento y desarrollo

Evalúa aspectos relacionados con:

- Capacitación.
- Planes de carrera.
- Evaluación de desempeño.
- Promoción interna.

### Trabajo en equipo

Evalúa aspectos relacionados con:

- Contribución individual a los objetivos del área.
- Sentido de pertenencia.
- Mejora de formas de trabajo dentro del equipo.

### Beneficio y recompensas

Evalúa aspectos relacionados con:

- Formas de recompensa.
- Ajustes o incrementos salariales.
- Estímulos al desempeño.

### Satisfacción laboral

Evalúa aspectos relacionados con:

- Disfrute del trabajo.
- Satisfacción dentro de la institución.
- Intención de permanencia.

### Comunicación

Evalúa aspectos relacionados con:

- Canales de comunicación.
- Comunicación entre departamentos.
- Comunicación de cambios y asuntos importantes.

### Inclusión

Evalúa aspectos relacionados con:

- Respeto y no discriminación.
- Espacios adecuados para personas con discapacidad.
- Seguimiento a reportes sobre igualdad de género o discriminación.

### Igualdad de género

Evalúa aspectos relacionados con:

- Distribución de funciones según responsabilidad del puesto.
- Comunicación con jefatura inmediata.
- Posibles situaciones de castigo, acoso u hostigamiento.
- Conocimiento de campañas internas.
- Conocimiento de autoridades para denuncia.

## Ejecución

Para ejecutar la aplicación localmente:

```bash
streamlit run app.py
```

Después de ejecutar el comando, Streamlit abrirá la aplicación en el navegador.

## Uso esperado

1. Crear el archivo `config.yml` con las credenciales de MongoDB.
2. Crear la base de datos y colecciones esperadas en MongoDB.
3. Registrar usuarios y contraseñas en la colección `usuarios`.
4. Instalar las dependencias del proyecto.
5. Ejecutar la aplicación con Streamlit.
6. Ingresar la contraseña de acceso.
7. Completar el cuestionario.
8. Presionar el botón **Enviar formulario**.
9. Confirmar que la información fue almacenada correctamente.

## Posibles mejoras

- Agregar una vista administrativa para consultar resultados.
- Agregar exportación de respuestas a CSV o Excel.
- Calcular indicadores por dimensión.
- Crear gráficas de resultados agregados.
- Agregar validación de campos obligatorios.
- Registrar fecha y hora de envío del formulario.
- Evitar múltiples respuestas por el mismo usuario.
- Mejorar el sistema de autenticación.
- Separar preguntas y dimensiones en un archivo de configuración.
- Agregar pruebas unitarias para autenticación y guardado de datos.

## Tecnologías utilizadas

- Python
- Streamlit
- MongoDB
- PyMongo
- YAML

## Objetivo del proyecto

Facilitar la captura estructurada de una pre-evaluación de clima laboral, permitiendo almacenar las respuestas en MongoDB para su posterior análisis institucional.

## Estado del proyecto

Proyecto en desarrollo para uso interno en actividades de diagnóstico y evaluación del clima laboral.