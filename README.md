# backend-2026-grupo-4

Proyecto desarrollado para la asignatura de **Desarrollo Backend (ICINF1108)**. CineDB API es una interfaz RESTful construida con **FastAPI** y **Python** que permite gestionar un catálogo audiovisual con directores, títulos (películas y series), reseñas de usuarios y listas de reproducción personalizadas.

---

##  Integrantes del Grupo
* **Danna Ramirez** - Coordinación del proyecto y Documentación (`feature/documentacion-readme`)
* **Matias Manquelaf** - Modelos de Dominio y Datos (`feature/modelos-dominio`)
* **Miguel Torres** - Estructura FastAPI y Lógica de Negocio (`feature/estructura-fastapi`)
* **Vicente Fonseca** - Calidad, Validaciones y Manejo de Errores (`feature/validaciones-errores`)

---

##  Problemáticas y Respuestas (P1 - P7)

### P1: Propósito de la API
* **¿Qué problema resuelve la API?**
  CineDB API resuelve la necesidad de centralizar y estructurar la información del contenido audiovisual (películas y series), permitiendo a los usuarios descubrir títulos, consultar detalles de directores, publicar reseñas con calificaciones numéricas y organizar su contenido favorito en listas personalizadas.
* **Dominio abordado:**
  Entretenimiento digital / Catálogo de Cine y Televisión.

### P2: Entidades Principales
La API gestiona **4 entidades de dominio fundamentales**:
1. **Director**: Representa a los creadores/directores de las obras audiovisuales.
2. **Titulo**: Películas o series registradas en el catálogo.
3. **Reseña**: Evaluaciones y comentarios realizados por los usuarios sobre un título.
4. **ListaUsuario**: Listas de reproducción o seguimiento creadas por usuarios (ej. "Favoritas 2026", "Por ver").

### P3: Arquitectura y Capas del Proyecto
El proyecto sigue una arquitectura modular en capas para mantener una separación clara de responsabilidades:
* `app/domain`: Contiene las clases de dominio puro y modelos base.
* `app/schemas`: Modelos de **Pydantic** para la validación de entrada/salida y serialización de datos HTTP.
* `app/repositories`: Gestión de almacenamiento en memoria (módulos de persisencia simulada).
* `app/services`: Lógica de negocio (reglas de validación, cálculos, asociaciones entre entidades).
* `app/routers`: Controladores de **FastAPI** que exponen los endpoints HTTP.

### P4: Reglas de Negocio Implementadas
1. **Calificación válida de Reseñas:** La nota de una reseña debe estar estrictamente entre 1.0 y 5.0 estrellas.
2. **Único Director por Título:** Un título debe estar asociado obligatoriamente a un `director_id` válido antes de ser creado.
3. **No duplicación de Títulos en Listas:** Una lista de usuario no puede contener el mismo título más de una vez.
4. **Formato de Año de Estreno:** El año de lanzamiento de una película o serie debe ser un valor entero no futuro.

### P5: Manejo de Errores y Validaciones HTTP
Se implementan excepciones HTTP personalizadas (`HTTPException`) utilizando los códigos de estado estándar:
* **400 Bad Request:** Datos de entrada inválidos o incumplimiento de reglas de negocio (ej. nota fuera de rango).
* **404 Not Found:** Recurso no encontrado (ej. `director_id` o `titulo_id` inexistente).
* **422 Unprocessable Entity:** Errores de validación automáticos de Pydantic en los tipos de datos recibidos.

### P6: Decisiones de Diseño y Git Workflow
* **Flujo de Git:** Se utilizó la estrategia de ramas por característica (`feature/`) a partir de `main`. Cada integrante desarrolló su módulo en una rama independiente y la integración se realizó mediante *Pull Requests* para asegurar el control de calidad.
* **Separación de Schemas y Domain:** Se separó la capa de esquemas (Pydantic) de la capa de dominio para evitar acoplar la API con las entidades del sistema.

### P7: Instrucciones de Instalación y Ejecución

#### Requisitos Previos
* Python 3.10+ instalado.
* Git instalado.

#### Paso a Paso
1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/dramirez08/backend-2026-grupo-4.git](https://github.com/dramirez08/backend-2026-grupo-4.git)
   cd backend-2026-grupo-4