import { Routes } from '@angular/router';
import { AlumnoComponent } from './pages/alumno/alumno.component';
import { DocenteComponent } from './pages/docente/docente.component';
import { IncidentesComponent } from './pages/incidentes/incidentes.component';

export const routes: Routes = [
  { path: 'alumno', component: AlumnoComponent },
  { path: 'docente', component: DocenteComponent },
  { path: 'incidentes', component: IncidentesComponent },
  { path: '', pathMatch: 'full', redirectTo: 'alumno' },
  { path: '**', redirectTo: 'alumno' }
];
