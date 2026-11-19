import re
from fastapi import HTTPException
from .config import CONTEXTS, PROMPTS

ACTIVITY_NAMES = {
    'alumno': {'resumen': 'Resumen', 'ensayo': 'Ensayo', 'cuestionario': 'Cuestionario', 'guia-estudio': 'Guía de estudio', 'personalizada': 'Tarea personalizada'},
    'docente': {'evaluacion-resumen': 'Evaluar resumen', 'rubrica': 'Evaluación con rúbrica', 'retroalimentacion': 'Retroalimentación', 'personalizada': 'Tarea personalizada'},
}

def render(template: str, **fields: str) -> str:
    text = (PROMPTS / template).read_text(encoding='utf-8')
    for key, value in fields.items():
        text = text.replace('{{' + key + '}}', value)
    return text

def list_activities(module: str):
    if module not in ACTIVITY_NAMES:
        raise HTTPException(404, detail='Módulo desconocido')
    return [{'id': key, 'name': name} for key, name in ACTIVITY_NAMES[module].items() if (CONTEXTS / module / f'{key}.md').is_file()]

def context_from_md(module: str, activity: str, fields: dict[str, str]) -> str:
    if module not in ACTIVITY_NAMES or activity not in ACTIVITY_NAMES[module]:
        raise HTTPException(400, detail='Actividad no permitida')
    file = CONTEXTS / module / f'{activity}.md'
    if not file.is_file():
        raise HTTPException(404, detail='No existe la plantilla Markdown')
    template = file.read_text(encoding='utf-8')
    return re.sub(r'\{\{([A-Z_]+)\}\}', lambda match: fields.get(match.group(1), ''), template)
