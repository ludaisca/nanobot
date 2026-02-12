# Habilidades (Skills) de nanobot

Este directorio contiene habilidades integradas que extienden las capacidades de nanobot.

## Formato de Habilidad

Cada habilidad es un directorio que contiene un archivo `SKILL.md` con:
- Frontmatter YAML (nombre, descripción, metadatos)
- Instrucciones Markdown para el agente

## Atribución

Estas habilidades están adaptadas del sistema de habilidades de [OpenClaw](https://github.com/openclaw/openclaw).
El formato de habilidad y la estructura de metadatos siguen las convenciones de OpenClaw para mantener compatibilidad.

## Habilidades Disponibles

| Habilidad | Descripción |
|-----------|-------------|
| `github` | Interactuar con GitHub usando la CLI `gh` |
| `weather` | Obtener información del clima usando wttr.in y Open-Meteo |
| `summarize` | Resumir URLs, archivos y videos de YouTube |
| `tmux` | Controlar remotamente sesiones de tmux |
| `skill-creator` | Crear nuevas habilidades |
