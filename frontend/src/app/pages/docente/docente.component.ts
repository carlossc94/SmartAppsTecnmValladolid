import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { AiApiService } from '../../services/ai-api.service';
import { Activity, AIResponse } from '../../models/ai.models';
import { ResultPanelComponent } from '../../shared/result-panel/result-panel.component';

@Component({
  selector: 'app-docente',
  standalone: true,
  imports: [CommonModule, FormsModule, ResultPanelComponent],
  templateUrl: './docente.component.html'
})
export class DocenteComponent {
 private readonly api=inject(AiApiService);activity='evaluacion-resumen';customInstructions='';activities:Activity[]=[];
 async ngOnInit(){try{this.activities=await this.api.activities('docente');}catch{this.error='No se pudieron cargar las actividades';}}
 topic='Arquitectura de software';studentText='La arquitectura de software organiza los componentes de un sistema y define cómo se comunican. Ayuda a mantener el código y mejorar su escalabilidad.';instructions='';
 simple?:AIResponse;context?:AIResponse;loading=false;error='';
 async generate(mode:'simple'|'context') {this.loading=true;this.error='';try {const r=await this.api.grade({topic:this.topic,studentText:this.studentText,instructions:this.instructions,activity:this.activity,customInstructions:this.customInstructions},mode);if(mode==='simple')this.simple=r;else this.context=r;}catch(e:any){this.error=e?.error?.error||'No se pudo conectar con la API.';}finally{this.loading=false;}}
 async compare(){await this.generate('simple');await this.generate('context');}
}
