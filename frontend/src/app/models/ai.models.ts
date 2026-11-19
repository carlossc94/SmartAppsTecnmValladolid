export interface Activity { id: string; name: string; }
export interface AIResponse { mode: string; provider: string; result: string; promptUsed: string; }
export type EvaluationMode = 'simple' | 'context';
