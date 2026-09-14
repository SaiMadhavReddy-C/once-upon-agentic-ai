# 🌟 Once Upon Agentic AI

> An AI-powered D&D Game Master built with AWS Strands Agents, Amazon Bedrock, MCP, A2A, FastAPI, and Python.

## 🚀 Overview

**Once Upon Agentic AI** is a multi-agent D&D Game Master that demonstrates how AI agents can use tools, communicate with specialized agents, and work together to create an interactive game experience.

The project was developed as part of the AWS Workshop Studio **"Once Upon Agentic AI: A Developer's Epic Journey"** and extended into a working local application with a web interface.

## ✨ Features

* 🤖 **Strands AI Agents** — Build and orchestrate AI agents using the Strands Agents SDK.
* 🎲 **Custom Dice Tools** — Create and execute custom D&D dice-rolling tools.
* 🧰 **Built-in Tools** — Equip agents with reusable tools.
* 🔌 **Model Context Protocol (MCP)** — Expose dice functionality through an MCP server.
* 🤝 **Agent-to-Agent (A2A)** — Connect specialized agents for rules and character management.
* 📚 **Rules Agent** — Handles D&D rules questions.
* 🎭 **Character Agent** — Creates, stores, finds, and manages player characters.
* 🎮 **Game Master Orchestrator** — Coordinates specialized agents to answer player requests.
* 🌐 **FastAPI Backend** — Provides API endpoints for the Game Master.
* 💻 **Web UI Integration** — Connect the local Game Master to the workshop web interface.
* ☁️ **Amazon Bedrock** — Provides foundation-model inference for the agents.

## 🏗️ Architecture

```text
                    ┌──────────────────────┐
                    │      Web UI          │
                    └──────────┬───────────┘
                               │ HTTPS
                               ▼
                    ┌──────────────────────┐
                    │  Game Master API     │
                    │      FastAPI         │
                    └──────────┬───────────┘
                               │
                    ┌──────────┴───────────┐
                    │                      │
                    ▼                      ▼
          ┌─────────────────┐    ┌─────────────────────┐
          │   Rules Agent   │    │   Character Agent   │
          │                 │    │                     │
          │ D&D rule logic  │    │ Character management│
          └─────────────────┘    └─────────────────────┘
                    │                      │
                    └──────────┬───────────┘
                               │ A2A
                               ▼
                    ┌──────────────────────┐
                    │   Agent Orchestration│
                    └──────────────────────┘

             MCP Layer
                    │
                    ▼
             ┌───────────────┐
             │ Dice Service  │
             │   MCP Server  │
             └───────────────┘

                    │
                    ▼
             Amazon Bedrock
```

## 📂 Project Structure

```text
once-upon-agentic-ai/
│
├── 1_strands_basics/
│   └── simple_agent.py
│
├── 2_built_in_tools/
│   └── agent_with_built_in_tools.py
│
├── 3_custom_tools/
│   └── agent_with_dice_roll_tool.py
│
├── 4_mcp_integration/
│   ├── dice_roll_mcp_server.py
│   └── gamemaster_mcp_client.py
│
├── 5_a2a_integration/
│   ├── agents/
│   │   ├── character_agent/
│   │   ├── gamemaster_orchestrator/
│   │   └── rules_agent/
│   └── utils/
│
└── README.md
```

## 🧭 Workshop Journey

### Chapter 1 — First Agent

Created the initial D&D Game Master using Strands Agents.

### Chapter 2 — Built-in Tools

Added built-in tools that allow the agent to perform useful actions instead of relying only on generated text.

### Chapter 3 — Custom Tools

Created a custom dice-rolling tool and used tool calling to generate D&D ability scores.

### Chapter 4 — MCP Integration

Built a remote dice-rolling service using the **Model Context Protocol (MCP)** and connected the Game Master to it.

### Chapter 5 — A2A Multi-Agent System

Built a multi-agent architecture using **Agent-to-Agent (A2A)** communication:

* **Rules Agent** — D&D rules specialist
* **Character Agent** — Character creation and management
* **Game Master** — Orchestrates the specialized agents

### Chapter 6 — Web Interface

Connected the Game Master API to the workshop web interface and exposed the backend through HTTPS.

### Chapter 7 — Advanced Enhancements

Explored future ideas including:

* Visual storytelling
* NPC memory and relationship management
* Multiplayer campaigns
* Dynamic world generation
* Advanced game mechanics
* External service integrations

## 🛠️ Tech Stack

| Technology         | Purpose                      |
| ------------------ | ---------------------------- |
| Python             | Application development      |
| AWS Strands Agents | AI agent framework           |
| Amazon Bedrock     | Foundation-model inference   |
| MCP                | Tool/service integration     |
| A2A                | Agent-to-agent communication |
| FastAPI            | Backend API                  |
| Uvicorn            | ASGI server                  |
| TinyDB             | Local character storage      |
| Cloudflare Tunnel  | HTTPS access to local API    |

## 🎯 What I Learned

This project helped me gain practical experience with:

* Designing AI agents around specialized responsibilities
* Building custom tools for AI agents
* Connecting agents to external services with MCP
* Designing multi-agent systems with A2A
* Building APIs for AI applications
* Connecting an AI backend to a web interface
* Debugging dependency and integration issues
* Handling cross-origin requests with CORS
* Building and testing an end-to-end agentic AI application

## 🔐 Security Notes

This project is intended for learning and experimentation.

Do **not** commit:

* AWS access keys
* Secret keys
* API keys
* `.env` files
* Personal credentials
* Runtime database files containing private information

## 📌 Workshop

Built as part of:

**AWS Workshop Studio — Once Upon Agentic AI: A Developer's Epic Journey**

The project demonstrates the progression from a single AI agent to a multi-agent system with tool use, MCP, A2A communication, and a web interface.

## 👨‍💻 Author

**Challa Sai Madhav Reddy**

GitHub:
https://github.com/SaiMadhavReddy-C

LinkedIn:
https://www.linkedin.com/in/sai-madhav-challa-bb9663384

---

⭐ If you found this project interesting, feel free to explore the code and build your own agentic AI application.
