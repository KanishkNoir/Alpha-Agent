# Alpha - Agentic AI Email Management System

An intelligent email management system with AI agents that can read emails, conduct research, and send responses automatically.

## 🚀 Features

- **Multi-Agent AI**: Email Agent + Research Agent + Supervisor coordination (Email Agent + Research Agent)
- **Gmail Integration**: Read/send emails via IMAP/SMTP
- **Smart Email Generation**: AI-powered email content with structured output
- **Chat API**: RESTful interface for email management
- **Docker Ready**: Full containerization with PostgreSQL database

## 🛠️ Quick Start

### Prerequisites
- Docker & Docker Compose
- Gmail account with App Password
- OpenAI API key


## 📡 API Usage

**Live Demo**: [https://alpha-agent-production.up.railway.app/](https://alpha-agent-production.up.railway.app/)

### Health Check
```bash
curl https://alpha-agent-production.up.railway.app/
# Returns: {"Hello":"World Alpha"}
```

### Chat Service Status
```bash
curl https://alpha-agent-production.up.railway.app/api/chat/
# Returns: {"status":"ok"}
```

### Recent Chat Messages
```bash
curl https://alpha-agent-production.up.railway.app/api/chat/recent/
```

### Generate Email Content
```bash
curl -X POST https://alpha-agent-production.up.railway.app/api/chat/ \
  -H "Content-Type: application/json" \
  -d '{"message": "Write a professional meeting invitation email"}'
```

### Multi-Agent Processing
```bash
curl -X POST https://alpha-agent-production.up.railway.app/api/chat/supervisor/ \
  -H "Content-Type: application/json" \
  -d '{"message": "Check emails from last 24 hours and send summaries"}'
```

### API Documentation
Interactive docs available at: https://alpha-agent-production.up.railway.app/docs

## 🤖 AI Capabilities

- **Email Agent**: `get_unread_emails()`, `send_email()`
- **Research Agent**: `research_email()` for content generation
- **Supervisor**: Coordinates complex email workflows

### Example Tasks
- "Find emails from the last 24 hours and send a summary"
- "Research coffee recipes and email me the best one"
- "Draft responses to urgent emails"

## 🏗️ Architecture

### Directory Structure
```
Alpha/
├── backend/
│   ├── src/
│   │   ├── main.py                    # FastAPI app entry point
│   │   └── api/
│   │       ├── db.py                  # Database config
│   │       ├── chat/                  # Chat API & models
│   │       ├── ai/                    # AI agents & services
│   │       │   ├── agents.py          # Multi-agent system
│   │       │   ├── services.py        # AI services
│   │       │   ├── tools.py           # Agent tools
│   │       │   └── schemas.py         # Response schemas
│   │       └── email_agent/           # Email processing
│   │           ├── gmail_parser.py    # IMAP email parsing
│   │           ├── inbox_reader.py    # Email fetching
│   │           └── sender.py          # SMTP email sending
│   ├── Dockerfile                     # Container setup
│   ├── requirements.txt               # Dependencies
│   └── railway.json                   # Deployment config
└── compose.yaml                       # Docker Compose
```

### System Flow
```
API Request → FastAPI → Supervisor Agent
                           ├── Email Agent (Gmail IMAP/SMTP)
                           └── Research Agent (OpenAI)
                                     ↓
                           PostgreSQL Database
```

## 🚀 Deployment

**Live on Railway**: [https://alpha-agent-production.up.railway.app/](https://alpha-agent-production.up.railway.app/)

- Pre-configured with `railway.json`
- Production-ready Dockerfile included
- Automated deployments from git push

---

**Alpha** - Intelligent Email Management with Agentic AI 🚀 