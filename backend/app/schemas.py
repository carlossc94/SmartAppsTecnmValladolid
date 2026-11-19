from typing import Literal
from pydantic import BaseModel, Field

class StudyRequest(BaseModel):
    topic: str = Field(min_length=1, max_length=300)
    sourceText: str = Field(default='', max_length=12000)
    workType: Literal['summary', 'assignment'] = 'summary'
    mode: Literal['simple', 'context'] = 'simple'
    activity: str = 'resumen'
    customInstructions: str = Field(default='', max_length=4000)

class GradeRequest(BaseModel):
    topic: str = Field(min_length=1, max_length=300)
    studentText: str = Field(min_length=1, max_length=12000)
    instructions: str = Field(default='', max_length=3000)
    mode: Literal['simple', 'context'] = 'simple'
    activity: str = 'evaluacion-resumen'
    customInstructions: str = Field(default='', max_length=4000)

class IncidentRequest(BaseModel):
    description: str = Field(min_length=5, max_length=6000)
    mode: Literal['simple', 'context'] = 'simple'

class AIResponse(BaseModel):
    mode: str
    provider: str
    result: str
    promptUsed: str
