# nanobot: Ultra-Lightweight Personal AI Assistant

## Project Overview

`nanobot` is a minimalist yet powerful AI assistant designed for personal use. It is built to be lightweight, extensible, and research-ready, featuring a modular architecture that separates the core agent logic, communication channels, skills, and LLM providers.

**Key Characteristics:**
*   **Ultra-Lightweight**: Core agent logic is ~4,000 lines of code.
*   **Extensible**: Modular design for easy addition of new providers, channels, and skills.
*   **Multi-Channel**: Supports communication via CLI, Telegram, Discord, WhatsApp, Feishu, Slack, Email, and more.
*   **Local & Cloud LLMs**: Supports OpenAI, Anthropic, OpenRouter, and local models via vLLM.

## Architecture

The project follows a clean, component-based architecture:

### 1. Core Agent (`nanobot/agent/`)
The heart of `nanobot` is the `AgentLoop` (in `nanobot/agent/loop.py`). It orchestrates the entire interaction process:
*   Receives messages from the **Message Bus**.
*   Builds **Context** using `ContextBuilder`, incorporating conversation history, memory, and skills.
*   Calls the configured **LLM Provider**.
*   Parses the LLM response for **Tool Calls**.
*   Executes tools via the **Tool Registry**.
*   Updates **Memory** (short-term session and long-term consolidation).
*   Sends the final response back via the **Message Bus**.

### 2. Message Bus (`nanobot/bus/`)
Facilitates asynchronous communication between external channels and the internal agent logic. Messages are routed using `InboundMessage` and `OutboundMessage` events.

### 3. Channels (`nanobot/channels/`)
Each communication platform (Telegram, Discord, etc.) has a corresponding channel integration that:
*   Receives messages from the platform API.
*   Normalizes them into `InboundMessage` format.
*   Publishes them to the bus.
*   Subscribes to `OutboundMessage` events from the bus.
*   Sends the response back to the user on the platform.

### 4. Providers (`nanobot/providers/`)
Abstraction layer for different LLM backends. Standardizes interactions with OpenAI, Anthropic, OpenRouter, Local vLLM, and others, making it easy to switch models or providers.

### 5. Tools (`nanobot/agent/tools/`)
Python classes that give the agent capabilities. Standard tools include:
*   **File System**: Read, write, edit, list files.
*   **Shell**: Execute bash commands.
*   **Web**: Search (Brave) and fetch content.
*   **Message**: Send messages.
*   **Spawn**: Create sub-agents for parallel tasks.
*   **Cron**: Schedule recurring tasks.

### 6. Skills (`nanobot/skills/`)
Skills are defined in `SKILL.md` files. They provide context and instructions to the LLM on how to perform specific high-level tasks, often by combining multiple tool calls (e.g., using `gh` CLI for GitHub interactions).

### 7. Memory (`nanobot/agent/memory.py`)
Implements a dual-memory system:
*   **Short-term**: Active session history.
*   **Long-term**: Periodically consolidated summaries and facts stored in `MEMORY.md` and `HISTORY.md`.

## Key Features

*   **Real-time Market Analysis**: Capable of fetching and analyzing financial data.
*   **Full-Stack Engineering**: Can write code, run tests, and manage deployments.
*   **Smart Routine Manager**: Handles scheduling and reminders via cron.
*   **Personal Knowledge Assistant**: Maintains a persistent memory of user preferences and facts.
*   **Voice Transcription**: Supports Whisper for transcribing voice messages (e.g., from Telegram).

## How it Works (Workflow)

1.  **Input**: A user sends a message via a channel (e.g., Telegram).
2.  **Routing**: The channel adapter converts the message to an internal event and pushes it to the message bus.
3.  **Processing**: The `AgentLoop` picks up the message.
4.  **Context Construction**: The agent retrieves session history and relevant context.
5.  **Reasoning**: The LLM is invoked with the context and available tools.
6.  **Action**: If the LLM decides to use a tool (e.g., `web_search`), the agent executes it and feeds the result back to the LLM. This loop continues until the task is complete.
7.  **Response**: The final answer is sent back through the bus to the original channel.

## Extensibility

*   **Add a Provider**: Register a new `ProviderSpec` in `nanobot/providers/registry.py` and add configuration in `nanobot/config/schema.py`.
*   **Add a Tool**: Subclass `Tool` in `nanobot/agent/tools/base.py`, implement `execute`, and register it in `AgentLoop`.
*   **Add a Skill**: Create a new directory in `nanobot/skills/` with a `SKILL.md` file containing instructions.
*   **Add a Channel**: Implement a new channel adapter in `nanobot/channels/` that interfaces with the platform's API and the message bus.
