from .ai_service import generate
from .config import ai_settings
from .demo import demo_grade, demo_incident, demo_study
from .prompts import context_from_md, render
from .schemas import AIResponse, GradeRequest, IncidentRequest, StudyRequest

async def run(prompt: str, mode: str, tokens: int, demo_result: str) -> AIResponse:
    settings = ai_settings()
    if settings.mode == 'demo':
        return AIResponse(mode=mode, provider='demo' if settings.provider != 'demo' else 'demo',
                          result=demo_result, promptUsed=prompt)
    result = await generate(prompt, tokens)
    return AIResponse(mode=mode, provider=settings.provider, result=result, promptUsed=prompt)

async def study(input: StudyRequest) -> AIResponse:
    prompt = (context_from_md('alumno', input.activity,
              {'TOPIC': input.topic, 'SOURCE': input.sourceText or 'Sin material de apoyo',
               'CUSTOM': input.customInstructions or 'Sin instrucciones adicionales'})
              if input.mode == 'context' else f'Elabora una actividad académica sobre: {input.topic}.')
    return await run(prompt, input.mode, 1100, demo_study(input.topic, input.mode))

async def grade(input: GradeRequest) -> AIResponse:
    prompt = (context_from_md('docente', input.activity,
              {'TOPIC': input.topic, 'STUDENT_TEXT': input.studentText,
               'INSTRUCTIONS': input.instructions or 'Sin instrucciones originales',
               'CUSTOM': input.customInstructions or 'Sin instrucciones adicionales'})
              if input.mode == 'context' else f'Evalúa de forma general el siguiente trabajo sobre {input.topic}:\n{input.studentText}')
    return await run(prompt, input.mode, 1600, demo_grade(input.mode))

async def incident(input: IncidentRequest) -> AIResponse:
    prompt = render('incident-with-context.txt' if input.mode == 'context' else 'incident-without-context.txt',
                    DESCRIPTION=input.description)
    return await run(prompt, input.mode, 1100, demo_incident(input.description, input.mode))
