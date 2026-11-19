import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AIResponse } from '../../models/ai.models';
import { MarkdownResultComponent } from '../markdown-result/markdown-result.component';

@Component({
  selector: 'app-result-panel',
  standalone: true,
  imports: [CommonModule, MarkdownResultComponent],
  template: `
    <article class="card result">
      <h2>{{ title }}</h2>
      <ng-container *ngIf="response as current; else empty">
        <span class="badge">{{ current.provider }}</span>
        <app-markdown-result [content]="current.result"></app-markdown-result>
        <details><summary>Ver prompt</summary><pre>{{ current.promptUsed }}</pre></details>
      </ng-container>
      <ng-template #empty><p>{{ emptyMessage }}</p></ng-template>
    </article>
  `
})
export class ResultPanelComponent {
  @Input({ required: true }) title = '';
  @Input() response?: AIResponse;
  @Input() emptyMessage = 'Sin resultado todavía';
}
