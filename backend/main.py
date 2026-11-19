from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import ai_settings
from app.prompts import list_activities
from app.schemas import AIResponse, StudyRequest, GradeRequest, IncidentRequest
from app import operations

app = FastAPI(title='SmartEdu AI', version='3.0.0')
app.add_middleware(CORSMiddleware,
                   allow_origins=['http://localhost:4200', 'http://127.0.0.1:4200'],
                   allow_credentials=False, allow_methods=['GET', 'POST'], allow_headers=['*'])

@app.get('/api/health')
def health():
    s = ai_settings()
    return {'status': 'ok', 'mode': s.mode, 'provider': s.provider, 'model': s.model}

@app.get('/api/activities/{module}')
def activities(module: str):
    return list_activities(module)

@app.post('/api/study/generate', response_model=AIResponse)
async def study(input: StudyRequest):
    return await operations.study(input)

@app.post('/api/grade/evaluate', response_model=AIResponse)
async def grade(input: GradeRequest):
    return await operations.grade(input)

@app.post('/api/incidents/classify', response_model=AIResponse)
async def classify_incident(input: IncidentRequest):
    return await operations.incident(input)