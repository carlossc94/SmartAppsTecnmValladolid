import unicodedata

INCIDENT_RULES = {
    'seguridad': ['phishing', 'contraseña robada', 'acceso no autorizado', 'malware', 'virus', 'ransomware', 'cuenta comprometida'],
    'red': ['wifi', 'wi-fi', 'internet', 'vpn', 'conexión', 'red', 'latencia'],
    'hardware': ['impresora', 'pantalla', 'teclado', 'disco duro', 'batería', 'monitor', 'laptop'],
    'software': ['aplicación', 'sistema', 'error', 'login', 'inicio de sesión', 'software', 'actualización'],
}

def demo_incident(description: str, mode: str) -> str:
    def normalize(value: str) -> str:
        return ''.join(ch for ch in unicodedata.normalize('NFD', value.lower()) if unicodedata.category(ch) != 'Mn')
    text = normalize(description)
    matches = {category: sum(normalize(word) in text for word in words) for category, words in INCIDENT_RULES.items()}
    category = max(matches, key=matches.get) if any(matches.values()) else 'sin clasificar'
    urgent = any(normalize(term) in text for term in ['caida total', 'todos los usuarios', 'datos filtrados', 'ransomware', 'no funciona ningun'])
    priority = 'alta (orientativa)' if urgent else 'pendiente de confirmar'
    if mode == 'simple':
        return f'SIMULACIÓN LOCAL (reglas, no IA)\nCategoría probable: {category}\nNo se realizó análisis de impacto ni urgencia.'
    return (f'SIMULACIÓN LOCAL (reglas, no IA)\nCategoría probable: {category}\nPrioridad orientativa: {priority}\n'
            'Impacto: no determinado; requiere número de usuarios afectados y servicio.\n'
            'Urgencia: no determinada; requiere tiempo límite y alternativa disponible.\n'
            'Acción sugerida: registrar ticket, confirmar alcance y escalar a soporte según procedimiento.\n'
            'Confianza: no calculada. Revisar clasificación manualmente.')


def demo_study(topic: str, mode: str) -> str:
    if mode == 'context':
        return (f'SIMULACIÓN SIN IA REAL — {topic}\n\nIdea principal: define el concepto y explica sus aplicaciones.\n'
                'Conceptos clave: identifica tres conceptos relevantes.\nEjemplo: añade un caso cotidiano.\n'
                'Conclusión: relaciona el tema con la asignatura.\n\nPlantilla ilustrativa, NO un resumen verificado.')
    return f'SIMULACIÓN SIN IA REAL — {topic} es un tema importante. Texto ilustrativo; no se utilizó IA.'

def demo_grade(mode: str) -> str:
    if mode == 'context':
        return ('SIMULACIÓN SIN IA REAL — EVALUACIÓN CON RÚBRICA\nComprensión: pendiente /30\n'
                'Conceptos: pendiente /30\nOrganización: pendiente /20\nEjemplos: pendiente /20\n'
                'Calificación: no disponible. El docente debe revisar cada criterio.')
    return 'SIMULACIÓN SIN IA REAL — EVALUACIÓN GENERAL\nNo se asigna calificación sin IA ni revisión humana.'
