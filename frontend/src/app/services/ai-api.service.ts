import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { firstValueFrom } from 'rxjs';
import { Activity, AIResponse, EvaluationMode } from '../models/ai.models';

@Injectable({ providedIn: 'root' })
export class AiApiService {
  private readonly http = inject(HttpClient);
  activities(module: 'alumno' | 'docente'): Promise<Activity[]> {
    return firstValueFrom(this.http.get<Activity[]>(`/api/activities/${module}`));
  }
  study(data: Record<string, unknown>, mode: EvaluationMode): Promise<AIResponse> {
    return firstValueFrom(this.http.post<AIResponse>('/api/study/generate', { ...data, mode }));
  }
  grade(data: Record<string, unknown>, mode: EvaluationMode): Promise<AIResponse> {
    return firstValueFrom(this.http.post<AIResponse>('/api/grade/evaluate', { ...data, mode }));
  }
  incident(description: string, mode: EvaluationMode): Promise<AIResponse> {
    return firstValueFrom(this.http.post<AIResponse>('/api/incidents/classify', { description, mode }));
  }
}
