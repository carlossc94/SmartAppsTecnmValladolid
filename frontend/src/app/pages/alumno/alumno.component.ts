import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { AiApiService } from '../../services/ai-api.service';
import { Activity, AIResponse } from '../../models/ai.models';
import { ResultPanelComponent } from '../../shared/result-panel/result-panel.component';

@Component({
  selector: 'app-alumno',
  standalone: true,
  imports: [CommonModule, FormsModule, ResultPanelComponent],
  templateUrl: './alumno.component.html'
})
export class AlumnoComponent {
 private readonly api=inject(AiApiService); topic='El ciclo del agua'; workType='summary'; sourceText=''; activity='resumen';customInstructions='';activities:Activity[]=[];
 async ngOnInit(){try{this.activities=await this.api.activities('alumno');}catch{this.error='No se pudieron cargar las actividades';}}
 simple?:AIResponse;context?:AIResponse;loading=false;error='';
 async generate(mode:'simple'|'context') {this.loading=true;this.error='';try {const r=await this.api.study({topic:this.topic,workType:this.workType,sourceText:this.sourceText,activity:this.activity,customInstructions:this.customInstructions},mode);if(mode==='simple')this.simple=r;else this.context=r;}catch(e:any){this.error=e?.error?.error||'No se pudo conectar con la API.';}finally{this.loading=false;}}
 async compare(){await this.generate('simple');await this.generate('context');}
}
