# nanobot: Asistente de IA Personal Ultra-Ligero

## Descripción del Proyecto

`nanobot` es un asistente de IA minimalista pero poderoso diseñado para uso personal. Está construido para ser ligero, extensible y listo para investigación, presentando una arquitectura modular que separa la lógica central del agente, los canales de comunicación, las habilidades y los proveedores de LLM.

**Características Clave:**
*   **Ultra-Ligero**: La lógica central del agente tiene ~4,000 líneas de código.
*   **Extensible**: Diseño modular para fácil adición de nuevos proveedores, canales y habilidades.
*   **Multi-Canal**: Soporta comunicación vía CLI, Telegram, Discord, WhatsApp, Feishu, Slack, Email, y más.
*   **LLMs Locales y en la Nube**: Soporta OpenAI, Anthropic, OpenRouter, y modelos locales vía vLLM.

## Arquitectura

El proyecto sigue una arquitectura limpia basada en componentes:

### 1. Agente Central (`nanobot/agent/`)
El corazón de `nanobot` es el `AgentLoop` (en `nanobot/agent/loop.py`). Orquesta todo el proceso de interacción:
*   Recibe mensajes del **Bus de Mensajes**.
*   Construye el **Contexto** usando `ContextBuilder`, incorporando historial de conversación, memoria y habilidades.
*   Llama al **Proveedor de LLM** configurado.
*   Analiza la respuesta del LLM en busca de **Llamadas a Herramientas**.
*   Ejecuta herramientas vía el **Registro de Herramientas**.
*   Actualiza la **Memoria** (sesión a corto plazo y consolidación a largo plazo).
*   Envía la respuesta final de vuelta a través del **Bus de Mensajes**.

### 2. Bus de Mensajes (`nanobot/bus/`)
Facilita la comunicación asíncrona entre canales externos y la lógica interna del agente. Los mensajes son enrutados usando eventos `InboundMessage` y `OutboundMessage`.

### 3. Canales (`nanobot/channels/`)
Cada plataforma de comunicación (Telegram, Discord, etc.) tiene una integración de canal correspondiente que:
*   Recibe mensajes de la API de la plataforma.
*   Los normaliza al formato `InboundMessage`.
*   Los publica en el bus.
*   Se suscribe a eventos `OutboundMessage` del bus.
*   Envía la respuesta de vuelta al usuario en la plataforma.

### 4. Proveedores (`nanobot/providers/`)
Capa de abstracción para diferentes backends de LLM. Estandariza interacciones con OpenAI, Anthropic, OpenRouter, Local vLLM, y otros, haciendo fácil cambiar modelos o proveedores.

### 5. Herramientas (`nanobot/agent/tools/`)
Clases Python que dan capacidades al agente. Herramientas estándar incluyen:
*   **Sistema de Archivos**: Leer, escribir, editar, listar archivos.
*   **Shell**: Ejecutar comandos bash.
*   **Web**: Buscar (Brave) y obtener contenido.
*   **Mensaje**: Enviar mensajes.
*   **Spawn**: Crear sub-agentes para tareas paralelas.
*   **Cron**: Programar tareas recurrentes.

### 6. Habilidades (`nanobot/skills/`)
Las habilidades se definen en archivos `SKILL.md`. Proveen contexto e instrucciones al LLM sobre cómo realizar tareas específicas de alto nivel, a menudo combinando múltiples llamadas a herramientas (ej. usar `gh` CLI para interacciones con GitHub).

### 7. Memoria (`nanobot/agent/memory.py`)
Implementa un sistema de memoria dual:
*   **Corto plazo**: Historial de sesión activo.
*   **Largo plazo**: Resúmenes y hechos consolidados periódicamente almacenados en `MEMORY.md` y `HISTORY.md`.

## Funcionalidades Clave

*   **Análisis de Mercado en Tiempo Real**: Capaz de obtener y analizar datos financieros.
*   **Ingeniería Full-Stack**: Puede escribir código, ejecutar pruebas y gestionar despliegues.
*   **Gestor de Rutina Inteligente**: Maneja programación y recordatorios vía cron.
*   **Asistente de Conocimiento Personal**: Mantiene una memoria persistente de preferencias y hechos del usuario.
*   **Transcripción de Voz**: Soporta Whisper para transcribir mensajes de voz (ej. desde Telegram).

## Cómo Funciona (Flujo de Trabajo)

1.  **Entrada**: Un usuario envía un mensaje vía un canal (ej. Telegram).
2.  **Enrutamiento**: El adaptador de canal convierte el mensaje a un evento interno y lo empuja al bus de mensajes.
3.  **Procesamiento**: El `AgentLoop` recoge el mensaje.
4.  **Construcción de Contexto**: El agente recupera el historial de sesión y contexto relevante.
5.  **Razonamiento**: El LLM es invocado con el contexto y herramientas disponibles.
6.  **Acción**: Si el LLM decide usar una herramienta (ej. `web_search`), el agente la ejecuta y alimenta el resultado de vuelta al LLM. Este bucle continúa hasta que la tarea se completa.
7.  **Respuesta**: La respuesta final se envía de vuelta a través del bus al canal original.

## Extensibilidad

*   **Añadir un Proveedor**: Registra un nuevo `ProviderSpec` en `nanobot/providers/registry.py` y añade configuración en `nanobot/config/schema.py`.
*   **Añadir una Herramienta**: Subclasea `Tool` en `nanobot/agent/tools/base.py`, implementa `execute`, y regístralo en `AgentLoop`.
*   **Añadir una Habilidad**: Crea un nuevo directorio en `nanobot/skills/` con un archivo `SKILL.md` conteniendo instrucciones.
*   **Añadir un Canal**: Implementa un nuevo adaptador de canal en `nanobot/channels/` que interconecte con la API de la plataforma y el bus de mensajes.
