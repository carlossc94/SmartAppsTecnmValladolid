import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { AiApiService } from '../../services/ai-api.service';
import { Activity, AIResponse } from '../../models/ai.models';
import { ResultPanelComponent } from '../../shared/result-panel/result-panel.component';

@Component({
  selector: 'app-incidentes',
  standalone: true,
  imports: [CommonModule, FormsModule, ResultPanelComponent],
  templateUrl: './incidentes.component.html'
})
export class IncidentesComponent {
 private readonly api=inject(AiApiService); description='No funciona la VPN para 20 colaboradores desde las 8:00. No pueden acceder al sistema de trabajo.';
 simple?:AIResponse;context?:AIResponse;loading=false;error='';
 async classify(mode:'simple'|'context') {this.loading=true;this.error='';try {const r=await this.api.incident(this.description,mode);if(mode==='simple')this.simple=r;else this.context=r;}catch(e:any){this.error=e?.error?.detail||'No se pudo conectar con la API.';}finally{this.loading=false;}}
 async compare(){await this.classify('simple');await this.classify('context');}
}
