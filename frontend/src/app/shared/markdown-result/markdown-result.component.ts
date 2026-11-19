import { Component, Input, inject, SecurityContext } from '@angular/core';
import { DomSanitizer } from '@angular/platform-browser';
import { marked } from 'marked';

@Component({
  selector: 'app-markdown-result',
  standalone: true,
  template: `<div class="markdown-content" [innerHTML]="html"></div>`
})
export class MarkdownResultComponent {
  private readonly sanitizer = inject(DomSanitizer);
  html = '';

  @Input() set content(value: string | null | undefined) {
    const parsed = marked.parse(value || '', { async: false, breaks: true, gfm: true }) as string;
   
    this.html = this.sanitizer.sanitize(SecurityContext.HTML, parsed) ?? '';
  }
}
