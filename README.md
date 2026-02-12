<div align="center">
  <img src="nanobot_logo.png" alt="nanobot" width="500">
  <h1>nanobot: Asistente de IA Personal Ultra-Ligero</h1>
  <p>
    <a href="https://pypi.org/project/nanobot-ai/"><img src="https://img.shields.io/pypi/v/nanobot-ai" alt="PyPI"></a>
    <a href="https://pepy.tech/project/nanobot-ai"><img src="https://static.pepy.tech/badge/nanobot-ai" alt="Downloads"></a>
    <img src="https://img.shields.io/badge/python-≥3.11-blue" alt="Python">
    <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
    <a href="./COMMUNICATION.md"><img src="https://img.shields.io/badge/Feishu-Group-E9DBFC?style=flat&logo=feishu&logoColor=white" alt="Feishu"></a>
    <a href="./COMMUNICATION.md"><img src="https://img.shields.io/badge/WeChat-Group-C5EAB4?style=flat&logo=wechat&logoColor=white" alt="WeChat"></a>
    <a href="https://discord.gg/MnCvHqpUGB"><img src="https://img.shields.io/badge/Discord-Community-5865F2?style=flat&logo=discord&logoColor=white" alt="Discord"></a>
  </p>
</div>

🐈 **nanobot** es un asistente de IA personal **ultra-ligero** inspirado en [OpenClaw](https://github.com/openclaw/openclaw)

⚡️ Entrega funcionalidad central de agente en solo **~4,000** líneas de código — **99% más pequeño** que las 430k+ líneas de Clawdbot.

📏 Conteo de líneas en tiempo real: **3,562 líneas** (ejecuta `bash core_agent_lines.sh` para verificar en cualquier momento)

## 📢 Noticias

- **2026-02-12** 🧠 Sistema de memoria rediseñado — Menos código, más confiable. ¡Únete a la [discusión](https://github.com/HKUDS/nanobot/discussions/566)!
- **2026-02-10** 🎉 ¡Lanzado v0.1.3.post6 con mejoras! Revisa las [notas](https://github.com/HKUDS/nanobot/releases/tag/v0.1.3.post6) de actualización y nuestro [roadmap](https://github.com/HKUDS/nanobot/discussions/431).
- **2026-02-09** 💬 Soporte añadido para Slack, Email y QQ — ¡nanobot ahora soporta múltiples plataformas de chat!
- **2026-02-08** 🔧 Proveedores refactorizados—¡agregar un nuevo proveedor de LLM ahora toma solo 2 pasos sencillos! Revisa [aquí](#providers).
- **2026-02-07** 🚀 ¡Lanzado v0.1.3.post5 con soporte para Qwen y varias mejoras clave! Revisa [aquí](https://github.com/HKUDS/nanobot/releases/tag/v0.1.3.post5) para detalles.
- **2026-02-06** ✨ ¡Añadido proveedor Moonshot/Kimi, integración con Discord y seguridad reforzada!
- **2026-02-05** ✨ ¡Añadido canal Feishu, proveedor DeepSeek y soporte mejorado para tareas programadas!
- **2026-02-04** 🚀 ¡Lanzado v0.1.3.post4 con soporte multi-proveedor y Docker! Revisa [aquí](https://github.com/HKUDS/nanobot/releases/tag/v0.1.3.post4) para detalles.
- **2026-02-03** ⚡ ¡Integrado vLLM para soporte de LLM local y programación de tareas en lenguaje natural mejorada!
- **2026-02-02** 🎉 ¡nanobot lanzado oficialmente! ¡Bienvenido a probar 🐈 nanobot!

## Características Clave de nanobot:

🪶 **Ultra-Ligero**: Solo ~4,000 líneas de código central del agente — 99% más pequeño que Clawdbot.

🔬 **Listo para Investigación**: Código limpio y legible que es fácil de entender, modificar y extender para investigación.

⚡️ **Rápido como el Rayo**: Huella mínima significa inicio más rápido, menor uso de recursos e iteraciones más rápidas.

💎 **Fácil de Usar**: Un clic para desplegar y estás listo para comenzar.

## 🏗️ Arquitectura

<p align="center">
  <img src="nanobot_arch.png" alt="arquitectura de nanobot" width="800">
</p>

## ✨ Funcionalidades

<table align="center">
  <tr align="center">
    <th><p align="center">📈 Análisis de Mercado en Tiempo Real 24/7</p></th>
    <th><p align="center">🚀 Ingeniero de Software Full-Stack</p></th>
    <th><p align="center">📅 Gestor Inteligente de Rutina Diaria</p></th>
    <th><p align="center">📚 Asistente de Conocimiento Personal</p></th>
  </tr>
  <tr>
    <td align="center"><p align="center"><img src="case/search.gif" width="180" height="400"></p></td>
    <td align="center"><p align="center"><img src="case/code.gif" width="180" height="400"></p></td>
    <td align="center"><p align="center"><img src="case/scedule.gif" width="180" height="400"></p></td>
    <td align="center"><p align="center"><img src="case/memory.gif" width="180" height="400"></p></td>
  </tr>
  <tr>
    <td align="center">Descubrimiento • Insights • Tendencias</td>
    <td align="center">Desarrollar • Desplegar • Escalar</td>
    <td align="center">Programar • Automatizar • Organizar</td>
    <td align="center">Aprender • Memoria • Razonamiento</td>
  </tr>
</table>

## 📦 Instalación

**Instalar desde la fuente** (últimas funcionalidades, recomendado para desarrollo)

```bash
git clone https://github.com/HKUDS/nanobot.git
cd nanobot
pip install -e .
```

**Instalar con [uv](https://github.com/astral-sh/uv)** (estable, rápido)

```bash
uv tool install nanobot-ai
```

**Instalar desde PyPI** (estable)

```bash
pip install nanobot-ai
```

## 🚀 Inicio Rápido

> [!TIP]
> Configura tu clave API en `~/.nanobot/config.json`.
> Obtén claves API: [OpenRouter](https://openrouter.ai/keys) (Global) · [Brave Search](https://brave.com/search/api/) (opcional, para búsqueda web)

**1. Inicializar**

```bash
nanobot onboard
```

**2. Configurar** (`~/.nanobot/config.json`)

Para OpenRouter - recomendado para usuarios globales:
```json
{
  "providers": {
    "openrouter": {
      "apiKey": "sk-or-v1-xxx"
    }
  },
  "agents": {
    "defaults": {
      "model": "anthropic/claude-opus-4-5"
    }
  }
}
```

**3. Chatear**

```bash
nanobot agent -m "¿Cuánto es 2+2?"
```

¡Eso es todo! Tienes un asistente de IA funcionando en 2 minutos.

## 🖥️ Modelos Locales (vLLM)

Ejecuta nanobot con tus propios modelos locales usando vLLM o cualquier servidor compatible con OpenAI.

**1. Inicia tu servidor vLLM**

```bash
vllm serve meta-llama/Llama-3.1-8B-Instruct --port 8000
```

**2. Configurar** (`~/.nanobot/config.json`)

```json
{
  "providers": {
    "vllm": {
      "apiKey": "dummy",
      "apiBase": "http://localhost:8000/v1"
    }
  },
  "agents": {
    "defaults": {
      "model": "meta-llama/Llama-3.1-8B-Instruct"
    }
  }
}
```

**3. Chatear**

```bash
nanobot agent -m "¡Hola desde mi LLM local!"
```

> [!TIP]
> La `apiKey` puede ser cualquier cadena no vacía para servidores locales que no requieren autenticación.

## 💬 Apps de Chat

Habla con tu nanobot a través de Telegram, Discord, WhatsApp, Feishu, Mochat, DingTalk, Slack, Email o QQ — en cualquier momento, en cualquier lugar.

| Canal | Configuración |
|---------|-------|
| **Telegram** | Fácil (solo un token) |
| **Discord** | Fácil (bot token + intents) |
| **WhatsApp** | Medio (escanear QR) |
| **Feishu** | Medio (credenciales de app) |
| **Mochat** | Medio (claw token + websocket) |
| **DingTalk** | Medio (credenciales de app) |
| **Slack** | Medio (bot + app tokens) |
| **Email** | Medio (credenciales IMAP/SMTP) |
| **QQ** | Fácil (credenciales de app) |

<details>
<summary><b>Telegram</b> (Recomendado)</summary>

**1. Crea un bot**
- Abre Telegram, busca `@BotFather`
- Envía `/newbot`, sigue las instrucciones
- Copia el token

**2. Configurar**

```json
{
  "channels": {
    "telegram": {
      "enabled": true,
      "token": "TU_TOKEN_DE_BOT",
      "allowFrom": ["TU_ID_DE_USUARIO"]
    }
  }
}
```

> Puedes encontrar tu **User ID** en los ajustes de Telegram. Se muestra como `@yourUserId`.
> Copia este valor **sin el símbolo `@`** y pégalo en el archivo de configuración.


**3. Ejecutar**

```bash
nanobot gateway
```

</details>

<details>
<summary><b>Mochat (Claw IM)</b></summary>

Usa **Socket.IO WebSocket** por defecto, con respaldo de sondeo HTTP.

**1. Pídele a nanobot que configure Mochat por ti**

Simplemente envía este mensaje a nanobot (reemplaza `xxx@xxx` con tu email real):

```
Read https://raw.githubusercontent.com/HKUDS/MoChat/refs/heads/main/skills/nanobot/skill.md and register on MoChat. My Email account is xxx@xxx Bind me as your owner and DM me on MoChat.
```

nanobot se registrará automáticamente, configurará `~/.nanobot/config.json`, y se conectará a Mochat.

**2. Reiniciar gateway**

```bash
nanobot gateway
```

¡Eso es todo — nanobot se encarga del resto!

<br>

<details>
<summary>Configuración manual (avanzado)</summary>

Si prefieres configurar manualmente, añade lo siguiente a `~/.nanobot/config.json`:

> Mantén `claw_token` privado. Solo debe enviarse en el encabezado `X-Claw-Token` a tu endpoint de API Mochat.

```json
{
  "channels": {
    "mochat": {
      "enabled": true,
      "base_url": "https://mochat.io",
      "socket_url": "https://mochat.io",
      "socket_path": "/socket.io",
      "claw_token": "claw_xxx",
      "agent_user_id": "6982abcdef",
      "sessions": ["*"],
      "panels": ["*"],
      "reply_delay_mode": "non-mention",
      "reply_delay_ms": 120000
    }
  }
}
```



</details>

</details>

<details>
<summary><b>Discord</b></summary>

**1. Crea un bot**
- Ve a https://discord.com/developers/applications
- Crea una aplicación → Bot → Add Bot
- Copia el token del bot

**2. Habilita intents**
- En los ajustes del Bot, habilita **MESSAGE CONTENT INTENT**
- (Opcional) Habilita **SERVER MEMBERS INTENT** si planeas usar listas de permitidos basadas en datos de miembros

**3. Obtén tu User ID**
- Ajustes de Discord → Avanzado → habilita **Developer Mode**
- Clic derecho en tu avatar → **Copy User ID**

**4. Configurar**

```json
{
  "channels": {
    "discord": {
      "enabled": true,
      "token": "TU_TOKEN_DE_BOT",
      "allowFrom": ["TU_ID_DE_USUARIO"]
    }
  }
}
```

**5. Invita al bot**
- OAuth2 → URL Generator
- Scopes: `bot`
- Bot Permissions: `Send Messages`, `Read Message History`
- Abre la URL de invitación generada y añade el bot a tu servidor

**6. Ejecutar**

```bash
nanobot gateway
```

</details>

<details>
<summary><b>WhatsApp</b></summary>

Requiere **Node.js ≥18**.

**1. Vincular dispositivo**

```bash
nanobot channels login
# Escanea el QR con WhatsApp → Ajustes → Dispositivos vinculados
```

**2. Configurar**

```json
{
  "channels": {
    "whatsapp": {
      "enabled": true,
      "allowFrom": ["+1234567890"]
    }
  }
}
```

**3. Ejecutar** (dos terminales)

```bash
# Terminal 1
nanobot channels login

# Terminal 2
nanobot gateway
```

</details>

<details>
<summary><b>Feishu (飞书)</b></summary>

Usa conexión larga **WebSocket** — no requiere IP pública.

**1. Crea un bot de Feishu**
- Visita [Feishu Open Platform](https://open.feishu.cn/app)
- Crea una nueva app → Habilita la capacidad **Bot**
- **Permisos**: Añade `im:message` (enviar mensajes)
- **Eventos**: Añade `im.message.receive_v1` (recibir mensajes)
  - Selecciona modo **Long Connection** (requiere ejecutar nanobot primero para establecer conexión)
- Obtén **App ID** y **App Secret** de "Credentials & Basic Info"
- Publica la app

**2. Configurar**

```json
{
  "channels": {
    "feishu": {
      "enabled": true,
      "appId": "cli_xxx",
      "appSecret": "xxx",
      "encryptKey": "",
      "verificationToken": "",
      "allowFrom": []
    }
  }
}
```

> `encryptKey` y `verificationToken` son opcionales para el modo Long Connection.
> `allowFrom`: Deja vacío para permitir todos los usuarios, o añade `["ou_xxx"]` para restringir acceso.

**3. Ejecutar**

```bash
nanobot gateway
```

> [!TIP]
> Feishu usa WebSocket para recibir mensajes — ¡no se necesita webhook ni IP pública!

</details>

<details>
<summary><b>QQ (QQ Chat Privado)</b></summary>

Usa **botpy SDK** con WebSocket — no requiere IP pública. Actualmente soporta **solo mensajes privados**.

**1. Registrar y crear bot**
- Visita [QQ Open Platform](https://q.qq.com) → Regístrate como desarrollador (personal o empresa)
- Crea una nueva aplicación bot
- Ve a **Desarrollo (Developer Settings)** → copia **AppID** y **AppSecret**

**2. Configurar sandbox para pruebas**
- En la consola de gestión del bot, encuentra **Configuración de Sandbox**
- Bajo **Configuración de lista de mensajes**, haz clic en **Añadir miembro** y añade tu propio número QQ
- Una vez añadido, escanea el código QR del bot con QQ móvil → abre el perfil del bot → toca "Enviar mensaje" para empezar a chatear

**3. Configurar**

> - `allowFrom`: Deja vacío para acceso público, o añade openids de usuario para restringir. Puedes encontrar los openids en los logs de nanobot cuando un usuario envía un mensaje al bot.
> - Para producción: envía una revisión en la consola del bot y publica. Ver [Docs de QQ Bot](https://bot.q.qq.com/wiki/) para el flujo completo de publicación.

```json
{
  "channels": {
    "qq": {
      "enabled": true,
      "appId": "TU_APP_ID",
      "secret": "TU_APP_SECRET",
      "allowFrom": []
    }
  }
}
```

**4. Ejecutar**

```bash
nanobot gateway
```

Ahora envía un mensaje al bot desde QQ — ¡debería responder!

</details>

<details>
<summary><b>DingTalk (钉钉)</b></summary>

Usa **Modo Stream** — no requiere IP pública.

**1. Crea un bot de DingTalk**
- Visita [DingTalk Open Platform](https://open-dev.dingtalk.com/)
- Crea una nueva app -> Añade capacidad **Robot**
- **Configuración**:
  - Activa **Stream Mode** ON
- **Permisos**: Añade permisos necesarios para enviar mensajes
- Obtén **AppKey** (Client ID) y **AppSecret** (Client Secret) de "Credentials"
- Publica la app

**2. Configurar**

```json
{
  "channels": {
    "dingtalk": {
      "enabled": true,
      "clientId": "TU_APP_KEY",
      "clientSecret": "TU_APP_SECRET",
      "allowFrom": []
    }
  }
}
```

> `allowFrom`: Deja vacío para permitir todos los usuarios, o añade `["staffId"]` para restringir acceso.

**3. Ejecutar**

```bash
nanobot gateway
```

</details>

<details>
<summary><b>Slack</b></summary>

Usa **Socket Mode** — no requiere URL pública.

**1. Crea una Slack app**
- Ve a [Slack API](https://api.slack.com/apps) → **Create New App** → "From scratch"
- Elige un nombre y selecciona tu espacio de trabajo

**2. Configurar la app**
- **Socket Mode**: Activa ON → Genera un **App-Level Token** con alcance `connections:write` → cópialo (`xapp-...`)
- **OAuth & Permissions**: Añade alcances de bot: `chat:write`, `reactions:write`, `app_mentions:read`
- **Event Subscriptions**: Activa ON → Suscríbete a eventos de bot: `message.im`, `message.channels`, `app_mention` → Guardar cambios
- **App Home**: Desplázate a **Show Tabs** → Habilita **Messages Tab** → Marca **"Allow users to send Slash commands and messages from the messages tab"**
- **Install App**: Clic en **Install to Workspace** → Autorizar → copia el **Bot Token** (`xoxb-...`)

**3. Configurar nanobot**

```json
{
  "channels": {
    "slack": {
      "enabled": true,
      "botToken": "xoxb-...",
      "appToken": "xapp-...",
      "groupPolicy": "mention"
    }
  }
}
```

**4. Ejecutar**

```bash
nanobot gateway
```

Envía DM al bot directamente o menciónalo (@mención) en un canal — ¡debería responder!

> [!TIP]
> - `groupPolicy`: `"mention"` (por defecto — responde solo cuando se le @menciona), `"open"` (responde a todos los mensajes del canal), o `"allowlist"` (restringir a canales específicos).
> - Política DM por defecto es abierto. Configura `"dm": {"enabled": false}` para deshabilitar DMs.

</details>

<details>
<summary><b>Email</b></summary>

Dale a nanobot su propia cuenta de correo. Consulta **IMAP** para correos entrantes y responde vía **SMTP** — como un asistente de correo personal.

**1. Obtén credenciales (ejemplo Gmail)**
- Crea una cuenta de Gmail dedicada para tu bot (ej. `mi-nanobot@gmail.com`)
- Habilita Verificación en 2 Pasos → Crea una [Contraseña de Aplicación](https://myaccount.google.com/apppasswords)
- Usa esta contraseña de aplicación para tanto IMAP como SMTP

**2. Configurar**

> - `consentGranted` debe ser `true` para permitir acceso al buzón. Esto es una medida de seguridad — configura `false` para deshabilitar totalmente.
> - `allowFrom`: Deja vacío para aceptar correos de cualquiera, o restringe a remitentes específicos.
> - `smtpUseTls` y `smtpUseSsl` por defecto son `true` / `false` respectivamente, lo cual es correcto para Gmail (puerto 587 + STARTTLS). No necesitas configurarlos explícitamente.
> - Configura `"autoReplyEnabled": false` si solo quieres leer/analizar correos sin enviar respuestas automáticas.

```json
{
  "channels": {
    "email": {
      "enabled": true,
      "consentGranted": true,
      "imapHost": "imap.gmail.com",
      "imapPort": 993,
      "imapUsername": "mi-nanobot@gmail.com",
      "imapPassword": "tu-app-password",
      "smtpHost": "smtp.gmail.com",
      "smtpPort": 587,
      "smtpUsername": "mi-nanobot@gmail.com",
      "smtpPassword": "tu-app-password",
      "fromAddress": "mi-nanobot@gmail.com",
      "allowFrom": ["tu-email-real@gmail.com"]
    }
  }
}
```


**3. Ejecutar**

```bash
nanobot gateway
```

</details>

## 🌐 Red Social de Agentes

🐈 nanobot es capaz de vincularse a la red social de agentes (comunidad de agentes). **¡Solo envía un mensaje y tu nanobot se une automáticamente!**

| Plataforma | Cómo Unirse (envía este mensaje a tu bot) |
|----------|-------------|
| [**Moltbook**](https://www.moltbook.com/) | `Read https://moltbook.com/skill.md and follow the instructions to join Moltbook` |
| [**ClawdChat**](https://clawdchat.ai/) | `Read https://clawdchat.ai/skill.md and follow the instructions to join ClawdChat` |

Simplemente envía el comando anterior a tu nanobot (vía CLI o cualquier canal de chat), y él se encargará del resto.

## ⚙️ Configuración

Archivo de configuración: `~/.nanobot/config.json`

### Proveedores

> [!TIP]
> - **Groq** provee transcripción de voz gratuita vía Whisper. Si se configura, los mensajes de voz de Telegram serán transcritos automáticamente.
> - **Plan de Coding Zhipu**: Si estás en el plan de coding de Zhipu, configura `"apiBase": "https://open.bigmodel.cn/api/coding/paas/v4"` en tu configuración de proveedor zhipu.
> - **MiniMax (China Continental)**: Si tu clave API es de la plataforma de China continental de MiniMax (minimaxi.com), configura `"apiBase": "https://api.minimaxi.com/v1"` en tu configuración de proveedor minimax.

| Proveedor | Propósito | Obtener API Key |
|----------|---------|-------------|
| `openrouter` | LLM (recomendado, acceso a todos los modelos) | [openrouter.ai](https://openrouter.ai) |
| `anthropic` | LLM (Claude directo) | [console.anthropic.com](https://console.anthropic.com) |
| `openai` | LLM (GPT directo) | [platform.openai.com](https://platform.openai.com) |
| `deepseek` | LLM (DeepSeek directo) | [platform.deepseek.com](https://platform.deepseek.com) |
| `groq` | LLM + **Transcripción de voz** (Whisper) | [console.groq.com](https://console.groq.com) |
| `gemini` | LLM (Gemini directo) | [aistudio.google.com](https://aistudio.google.com) |
| `minimax` | LLM (MiniMax directo) | [platform.minimax.io](https://platform.minimax.io) |
| `aihubmix` | LLM (API gateway, acceso a todos los modelos) | [aihubmix.com](https://aihubmix.com) |
| `dashscope` | LLM (Qwen) | [dashscope.console.aliyun.com](https://dashscope.console.aliyun.com) |
| `moonshot` | LLM (Moonshot/Kimi) | [platform.moonshot.cn](https://platform.moonshot.cn) |
| `zhipu` | LLM (Zhipu GLM) | [open.bigmodel.cn](https://open.bigmodel.cn) |
| `vllm` | LLM (local, cualquier servidor compatible con OpenAI) | — |

<details>
<summary><b>Añadiendo un Nuevo Proveedor (Guía de Desarrollador)</b></summary>

nanobot usa un **Registro de Proveedores** (`nanobot/providers/registry.py`) como la única fuente de verdad.
Añadir un nuevo proveedor solo toma **2 pasos** — sin cadenas if-elif que tocar.

**Paso 1.** Añade una entrada `ProviderSpec` a `PROVIDERS` en `nanobot/providers/registry.py`:

```python
ProviderSpec(
    name="myprovider",                   # config field name
    keywords=("myprovider", "mymodel"),  # model-name keywords for auto-matching
    env_key="MYPROVIDER_API_KEY",        # env var for LiteLLM
    display_name="My Provider",          # shown in `nanobot status`
    litellm_prefix="myprovider",         # auto-prefix: model → myprovider/model
    skip_prefixes=("myprovider/",),      # don't double-prefix
)
```

**Paso 2.** Añade un campo a `ProvidersConfig` en `nanobot/config/schema.py`:

```python
class ProvidersConfig(BaseModel):
    ...
    myprovider: ProviderConfig = ProviderConfig()
```

¡Eso es todo! Variables de entorno, prefijado de modelo, coincidencia de configuración y visualización en `nanobot status` funcionarán automáticamente.

**Opciones comunes de `ProviderSpec`:**

| Campo | Descripción | Ejemplo |
|-------|-------------|---------|
| `litellm_prefix` | Auto-prefijar nombres de modelo para LiteLLM | `"dashscope"` → `dashscope/qwen-max` |
| `skip_prefixes` | No prefijar si el modelo ya empieza con estos | `("dashscope/", "openrouter/")` |
| `env_extras` | Variables env adicionales para establecer | `(("ZHIPUAI_API_KEY", "{api_key}"),)` |
| `model_overrides` | Sobrescritura de parámetros por modelo | `(("kimi-k2.5", {"temperature": 1.0}),)` |
| `is_gateway` | Puede enrutar cualquier modelo (como OpenRouter) | `True` |
| `detect_by_key_prefix` | Detectar gateway por prefijo de clave API | `"sk-or-"` |
| `detect_by_base_keyword` | Detectar gateway por URL base de API | `"openrouter"` |
| `strip_model_prefix` | Eliminar prefijo existente antes de re-prefijar | `True` (para AiHubMix) |

</details>


### Seguridad

> Para despliegues en producción, configura `"restrictToWorkspace": true` en tu configuración para aislar el agente.

| Opción | Por defecto | Descripción |
|--------|---------|-------------|
| `tools.restrictToWorkspace` | `false` | Cuando es `true`, restringe **todas** las herramientas del agente (shell, lectura/escritura/edición de archivos, listar) al directorio de espacio de trabajo. Previene recorrido de rutas y acceso fuera de alcance. |
| `channels.*.allowFrom` | `[]` (permitir todos) | Lista blanca de IDs de usuario. Vacío = permitir a todos; no vacío = solo los usuarios listados pueden interactuar. |


## Referencia CLI

| Comando | Descripción |
|---------|-------------|
| `nanobot onboard` | Inicializar configuración y espacio de trabajo |
| `nanobot agent -m "..."` | Chatear con el agente |
| `nanobot agent` | Modo de chat interactivo |
| `nanobot agent --no-markdown` | Mostrar respuestas en texto plano |
| `nanobot agent --logs` | Mostrar logs de ejecución durante el chat |
| `nanobot gateway` | Iniciar el gateway |
| `nanobot status` | Mostrar estado |
| `nanobot channels login` | Vincular WhatsApp (escanear QR) |
| `nanobot channels status` | Mostrar estado de canales |

Salidas de modo interactivo: `exit`, `quit`, `/exit`, `/quit`, `:q`, o `Ctrl+D`.

<details>
<summary><b>Tareas Programadas (Cron)</b></summary>

```bash
# Añadir un trabajo
nanobot cron add --name "daily" --message "Good morning!" --cron "0 9 * * *"
nanobot cron add --name "hourly" --message "Check status" --every 3600

# Listar trabajos
nanobot cron list

# Eliminar un trabajo
nanobot cron remove <job_id>
```

</details>

## 🐳 Docker

> [!TIP]
> La bandera `-v ~/.nanobot:/root/.nanobot` monta tu directorio de configuración local en el contenedor, para que tu configuración y espacio de trabajo persistan tras reinicios del contenedor.

Construir y ejecutar nanobot en un contenedor:

```bash
# Construir la imagen
docker build -t nanobot .

# Inicializar configuración (solo primera vez)
docker run -v ~/.nanobot:/root/.nanobot --rm nanobot onboard

# Editar configuración en host para añadir claves API
vim ~/.nanobot/config.json

# Ejecutar gateway (conecta a canales habilitados, ej. Telegram/Discord/Mochat)
docker run -v ~/.nanobot:/root/.nanobot -p 18790:18790 nanobot gateway

# O ejecutar un solo comando
docker run -v ~/.nanobot:/root/.nanobot --rm nanobot agent -m "Hello!"
docker run -v ~/.nanobot:/root/.nanobot --rm nanobot status
```

## 📁 Estructura del Proyecto

```
nanobot/
├── agent/          # 🧠 Lógica central del agente
│   ├── loop.py     #    Bucle del agente (LLM ↔ ejecución de herramientas)
│   ├── context.py  #    Constructor de contexto (prompt)
│   ├── memory.py   #    Memoria persistente
│   ├── skills.py   #    Cargador de habilidades
│   ├── subagent.py #    Ejecución de tareas en segundo plano
│   └── tools/      #    Herramientas integradas (incl. spawn)
├── skills/         # 🎯 Habilidades incluidas (github, weather, tmux...)
├── channels/       # 📱 Integraciones de canales de chat
├── bus/            # 🚌 Enrutamiento de mensajes
├── cron/           # ⏰ Tareas programadas
├── heartbeat/      # 💓 Despertador proactivo
├── providers/      # 🤖 Proveedores de LLM (OpenRouter, etc.)
├── session/        # 💬 Sesiones de conversación
├── config/         # ⚙️ Configuración
└── cli/            # 🖥️ Comandos
```

## 🤝 Contribuir y Roadmap

¡PRs bienvenidos! La base de código es intencionalmente pequeña y legible. 🤗

**Roadmap** — ¡Elige un ítem y [abre un PR](https://github.com/HKUDS/nanobot/pulls)!

- [x] **Transcripción de Voz** — Soporte para Groq Whisper (Issue #13)
- [ ] **Multi-modal** — Ver y escuchar (imágenes, voz, video)
- [ ] **Memoria a largo plazo** — Nunca olvidar contexto importante
- [ ] **Mejor razonamiento** — Planificación de múltiples pasos y reflexión
- [ ] **Más integraciones** — Calendario y más
- [ ] **Auto-mejora** — Aprender de retroalimentación y errores

### Contribuidores

<a href="https://github.com/HKUDS/nanobot/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=HKUDS/nanobot&max=100&columns=12&updated=20260210" alt="Contributors" />
</a>


## ⭐ Historial de Estrellas

<div align="center">
  <a href="https://star-history.com/#HKUDS/nanobot&Date">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=HKUDS/nanobot&type=Date&theme=dark" />
      <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=HKUDS/nanobot&type=Date" />
      <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=HKUDS/nanobot&type=Date" style="border-radius: 15px; box-shadow: 0 0 30px rgba(0, 217, 255, 0.3);" />
    </picture>
  </a>
</div>

<p align="center">
  <em> ¡Gracias por visitar ✨ nanobot!</em><br><br>
  <img src="https://visitor-badge.laobi.icu/badge?page_id=HKUDS.nanobot&style=for-the-badge&color=00d4ff" alt="Views">
</p>


<p align="center">
  <sub>nanobot es solo para propósitos educativos, de investigación e intercambio técnico</sub>
</p>
