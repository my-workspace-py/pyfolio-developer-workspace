\# 🚀 SrinivasKalyan Buthkur — Polyglot Backend \& RAG Intelligence Workspace



\[!\[License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

\[!\[Stack: React 18 + Vite](https://img.shields.io/badge/Frontend-React\_18\_%7C\_Vite\_%7C\_Tailwind-61DAFB)](https://react.dev)

\[!\[Backend: Node.js + Express](https://img.shields.io/badge/Backend-Node.js\_%7C\_Express-339933)](https://expressjs.com)

\[!\[RAG: Offline Local Index + Gemini Fallback](https://img.shields.io/badge/RAG\_Engine-Local\_Offline\_%2B\_Gemini\_3.5\_Flash-8E44AD)](https://github.com/imsrinuu)

\[!\[Security: 0% Hardcoded Secrets](https://img.shields.io/badge/Security-0%25\_Hardcoded\_Keys-10B981)](/.env.example)



A full-stack, developer-grade \*\*Retrieval-Augmented Generation (RAG)\*\* intelligence workspace and interactive portfolio showcasing \*\*SrinivasKalyan Buthkur\*\* — Senior Polyglot Backend Engineer and Automation Specialist.



This application features a \*\*100% client-side offline RAG vector/keyword search engine\*\* with multi-chunk synthesis, alongside an optional \*\*Gemini 3.5 Flash cloud proxy\*\*, an \*\*interactive TTY terminal emulator\*\*, and a \*\*real-time diagnostics dashboard\*\*.



\---



\## 🌟 Key Features



\### 🧠 1. Dual-Mode RAG Intelligence Engine

\- \*\*Local Offline RAG Engine (`localRag.ts`)\*\*: Operates 100% offline without requiring any external API keys or cloud dependencies. Performs tokenization, keyword-scoring, and multi-chunk synthesis across structured candidate credential files.

\- \*\*Visual Chunk Retrieval\*\*: Real-time rendering of retrieved semantic grounding files, match confidence scores, category badges, and keyword tags for complete response transparency.

\- \*\*Gemini 3.5 Flash Optional Hybrid Fallback\*\*: Optional server-side AI model integration via `/api/chat` with automatic, graceful fallback to the local offline RAG engine if the API key is unconfigured or rate-limited.



\### 💻 2. IDE-Style Interactive Workspace

\- \*\*Dual Workspace Modes\*\*:

&#x20; - \*\*RAG Intelligence Assistant\*\*: Interactive conversation interface with dynamic bento prompts, Markdown rendering, and source chunk visualizers.

&#x20; - \*\*Interactive TTY Terminal\*\*: Unix-like shell with built-in commands (`cat resume.json`, `rag --query "..."`, `skills`, `awards`, `system`, `contact`).

\- \*\*Real-Time Telemetry \& Diagnostics\*\*: Monitors latency (ms), active engine status, query match confidence, and live system log streams.



\### 🔒 3. Enterprise-Grade Security \& Privacy

\- \*\*Zero Hardcoded Secrets\*\*: Fully safe for public GitHub deployment.

\- \*\*Server-Side API Key Isolation\*\*: All cloud AI keys remain protected on the backend using environment variables (`process.env.GEMINI\_API\_KEY`).



\---



\## 📐 System Architecture



```

&#x20;                                 ┌─────────────────────────────────────────┐

&#x20;                                 │           User Web Interface            │

&#x20;                                 │  (React 18 / Vite / Tailwind / Motion)  │

&#x20;                                 └────────────────────┬────────────────────┘

&#x20;                                                      │

&#x20;                                  ┌───────────────────┴──────────────────┐

&#x20;                                  ▼                                      ▼

&#x20;                       ┌────────────────────┐                ┌──────────────────────┐

&#x20;                       │ Interactive RAG    │                │ Interactive TTY      │

&#x20;                       │ Chatbot Component  │                │ Terminal Emulator    │

&#x20;                       └──────────┬─────────┘                └───────────┬──────────┘

&#x20;                                  │                                      │

&#x20;                                  └───────────────────┬──────────────────┘

&#x20;                                                      │

&#x20;                                                      ▼

&#x20;                                          ┌──────────────────────┐

&#x20;                                          │ Express API /api/chat│

&#x20;                                          └───────────┬──────────┘

&#x20;                                                      │

&#x20;                              ┌───────────────────────┴───────────────────────┐

&#x20;                              ▼                                               ▼

&#x20;              ┌───────────────────────────────┐               ┌───────────────────────────────┐

&#x20;              │    Local Offline RAG Engine    │               │  Optional Gemini 3.5 Flash    │

&#x20;              │  (Multi-Chunk Keyword Scoring)│               │  (Server-Side Cloud API)      │

&#x20;              └───────────────┬───────────────┘               └───────────────┬───────────────┘

&#x20;                              │                                               │

&#x20;                              └───────────────────────┬───────────────────────┘

&#x20;                                                      │

&#x20;                                                      ▼

&#x20;                                          ┌──────────────────────┐

&#x20;                                          │  Grounded Response \& │

&#x20;                                          │  Source Chunk Meta   │

&#x20;                                          └──────────────────────┘

```



\---



\## 📜 Candidate Snapshot: SrinivasKalyan Buthkur



\- \*\*Role\*\*: Senior Polyglot Backend Engineer \& Automation Specialist

\- \*\*Experience\*\*: 4+ Years at CGI (Zero-defect product releases \& major microservices delivery)

\- \*\*Primary Stack\*\*: \*\*Python\*\* (FastAPI, Django, Async ETL pipelines, pandas/numpy)

\- \*\*Polyglot Ecosystem\*\*: \*\*Java\*\* (Spring Boot, REST APIs), \*\*Ruby on Rails\*\* (Enterprise Maintenance), \*\*PostgreSQL\*\*, \*\*Docker\*\*, \*\*Jenkins\*\*.

\- \*\*AI \& Automation\*\*: \*\*n8n Autonomous AI Agents\*\*, \*\*Indico NLP Document Parsing (85% accuracy boost)\*\*, \*\*Kali NetHunter Android Security Research\*\*.

\- \*\*Notice Period\*\*: Immediately Available



\### 🏅 Global \& Organizational Honors

| Year | Award | Recognition Level | Achievement Summary |

| :--- | :--- | :--- | :--- |

| \*\*2026\*\* | \*\*GCC Excellence Award\*\* | Global (CGI) | Outstanding engineering contributions, backend delivery excellence, and strategic impact over a 1-year tenure. |

| \*\*2025\*\* | \*\*CII AI Awards\*\* | Regional (Hyderabad) | \*\*Bronze Recognition\*\* for innovative ML model transformations on CGI's DOC AI project. |

| \*\*2022–25\*\* | \*\*CGI Gold Award (3x)\*\* | Corporate | CGI's highest internal honor awarded 3 times for exemplary delivery and peer mentoring. |

| \*\*2023\*\* | \*\*CGI Key Differentiator Award\*\* | Corporate | Awarded for achieving consistent zero-defect major releases via automated testing scaffolding. |



\---



\## 🛠️ Tech Stack \& Directory Structure



```text

├── server.ts                 # Express server with /api/chat route \& Vite dev middleware

├── src/

│   ├── components/

│   │   ├── InterviewerChat.tsx # Primary RAG Chatbot UI \& Source Chunk Visualizer

│   │   └── TerminalView.tsx    # Unix-style TTY Terminal Emulator

│   ├── lib/

│   │   └── localRag.ts         # Offline local RAG search engine \& chunk knowledge base

│   ├── data.ts                 # Structured candidate portfolio credentials

│   ├── types.ts                # Shared TypeScript interfaces

│   ├── App.tsx                 # Main IDE layout container

│   └── main.tsx                # React entry point

├── package.json              # Project dependencies \& build scripts

├── metadata.json             # AI Studio metadata configuration

└── .env.example              # Environment variables template

```



\---



\## ⚡ Quick Start \& Local Setup



\### Prerequisites

\- \*\*Node.js\*\*: `v18.0.0` or higher

\- \*\*npm\*\*: `v9.0.0` or higher



\### Installation \& Run



1\. \*\*Clone the Repository\*\*:

&#x20;  ```bash

&#x20;  git clone https://github.com/imsrinuu/srinivas-rag-portfolio.git

&#x20;  cd srinivas-rag-portfolio

&#x20;  ```



2\. \*\*Install Dependencies\*\*:

&#x20;  ```bash

&#x20;  npm install

&#x20;  ```



3\. \*\*Configure Environment Variables (Optional)\*\*:

&#x20;  ```bash

&#x20;  cp .env.example .env

&#x20;  ```

&#x20;  \*Note: The app runs 100% locally with the Offline RAG engine even if `.env` is empty or `GEMINI\_API\_KEY` is omitted!\*



4\. \*\*Start Development Server\*\*:

&#x20;  ```bash

&#x20;  npm run dev

&#x20;  ```

&#x20;  Open `http://localhost:3000` in your browser.



5\. \*\*Build for Production\*\*:

&#x20;  ```bash

&#x20;  npm run build

&#x20;  npm start

&#x20;  ```



\---



\## 🛡️ Security \& Environment Variables



This project strictly adheres to secure open-source coding standards:

\- \*\*No Private Keys in Source Code\*\*: Zero hardcoded credentials.

\- \*\*Environment Declaration\*\*:

&#x20; ```env

&#x20; # .env.example

&#x20; GEMINI\_API\_KEY=

&#x20; PORT=3000

&#x20; NODE\_ENV=development

&#x20; ```



\---



\## ✉️ Contact \& Coordination



\- \*\*Email\*\*: \[imsrinuu@gmail.com](mailto:imsrinuu@gmail.com)

\- \*\*Phone\*\*: +91-9652613100

\- \*\*Location\*\*: Hyderabad, Telangana, India

\- \*\*GitHub\*\*: \[github.com/imsrinuu](https://github.com/imsrinuu)

\- \*\*LinkedIn\*\*: \[linkedin.com/in/imsrinuu](https://linkedin.com/in/imsrinuu)



\---



\*Built with precision using React, Express, TypeScript, and Tailwind CSS.\*



