# SmartEdu AI

Aplicación educativa para comparar respuestas **con y sin contexto** mediante inteligencia artificial. Incluye tres módulos desarrollados con **Angular 20** y **Python/FastAPI**.

## Módulos

| Módulo | Ruta | Función |
| --- | --- | --- |
| Alumno | `/alumno` | Generación de resúmenes, ensayos, cuestionarios y guías de estudio. |
| Docente | `/docente` | Evaluación y retroalimentación de trabajos mediante rúbricas. |
| Incidentes | `/incidentes` | Clasificación orientativa de incidentes de TI. |

## Tecnologías

- **Frontend:** Angular 20, TypeScript y `marked` para visualizar Markdown.
- **Backend:** Python, FastAPI, HTTPX y archivos Markdown para instrucciones y contexto.
- **Proveedores de IA:** Groq, Gemini y DeepSeek.
- **Modo demo:** respuestas simuladas sin llamadas a servicios de IA.

## Estructura del proyecto

```text
frontend/
└── src/app/
    ├── models/                 # Tipos e interfaces
    ├── services/               # Comunicación con FastAPI
    ├── shared/                 # Markdown y panel de resultados
    └── pages/
        ├── alumno/
        ├── docente/
        └── incidentes/

backend/
├── main.py                     # Endpoints
├── app/
│   ├── config.py               # Variables de entorno
│   ├── ai_service.py           # Selección de proveedor
│   ├── operations.py           # Lógica de los módulos
│   ├── demo.py                 # Modo sin IA
│   ├── prompts.py              # Lectura de instrucciones
│   ├── schemas.py              # Modelos de datos
│   └── providers/
│       ├── gemini.py
│       ├── deepseek.py
│       ├── groq.py
│       └── openai_compatible.py
├── contexts/                   # Actividades y rúbricas Markdown
└── prompts/                    # Plantillas de prompts
```

## Instalación

**Requisitos:** Python 3.10+ y una versión de Node.js compatible con Angular 20.

### 1. Backend

Desde `backend/`:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
python -m uvicorn main:app --reload --port 5050
```

En Linux/macOS, activa el entorno con `source .venv/bin/activate` y copia el archivo con `cp .env.example .env`.

### 2. Configuración de IA

Edita `backend/.env` y selecciona el proveedor:

```dotenv
AI_PROVIDER=groq
GROQ_API_KEY=TU_CLAVE
GROQ_MODEL=openai/gpt-oss-20b
GROQ_BASE_URL=https://api.groq.com/openai/v1
```

También puedes seleccionar `AI_PROVIDER=gemini`, `AI_PROVIDER=deepseek` o `AI_PROVIDER=demo`. Para cada proveedor real, configura sus variables `*_API_KEY`, `*_MODEL` y `*_BASE_URL` siguiendo `.env.example`.

> **Importante:** el modo `demo` no utiliza IA. Nunca publiques tu archivo `.env` ni las claves API.

### 3. Frontend

En otra terminal, desde `frontend/`:

```powershell
npm install
npm start
```

Abre `http://localhost:4200`. Angular redirige las solicitudes `/api` al backend local mediante el proxy de desarrollo.

## API

| Método | Endpoint | Descripción |
| --- | --- | --- |
| `GET` | `/api/health` | Estado y proveedor configurado. |
| `GET` | `/api/activities/{module}` | Actividades disponibles. |
| `POST` | `/api/study/generate` | Generación de material de estudio. |
| `POST` | `/api/grade/evaluate` | Evaluación de trabajos. |
| `POST` | `/api/incidents/classify` | Clasificación de incidentes. |

Documentación interactiva: `http://localhost:5050/docs`.

## Cambios principales

- **Backend modular:** endpoints separados de la lógica, los proveedores y el modo demo.
- **Conexiones reutilizables:** DeepSeek y Groq comparten un cliente HTTP compatible con OpenAI; Gemini tiene su propio adaptador.
- **Frontend modular:** páginas, modelos, servicios y componentes compartidos.
- **Markdown renderizado:** los resultados muestran títulos, listas, tablas y formato sin exponer los símbolos Markdown; los prompts originales siguen disponibles para consulta.
- **Configuración centralizada:** cambio de proveedor mediante `.env`, sin modificar los endpoints.

## Consideraciones

Proyecto con fines **educativos y de demostración**. Las respuestas generadas por IA pueden contener errores; las evaluaciones académicas requieren revisión docente y las clasificaciones de incidentes no sustituyen los procedimientos de soporte. Usa datos ficticios o anonimizados.
