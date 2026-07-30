import express from "express";
import path from "path";
import dotenv from "dotenv";
import { createServer as createViteServer } from "vite";
import { GoogleGenAI } from "@google/genai";
import { queryLocalRAG } from "./src/lib/localRag";

dotenv.config();

const PORT = 3000;

async function startServer() {
  const app = express();
  app.use(express.json());

  // API routes FIRST
  app.post("/api/chat", async (req, res) => {
    const { message, history, mode } = req.body;
    if (!message) {
      res.status(400).json({ error: "Missing message field" });
      return;
    }

    try {
      // If client requests explicit local/offline mode, bypass Gemini API
      if (mode === 'local') {
        const result = queryLocalRAG(message);
        res.json({ reply: result.reply, retrievedChunks: result.retrievedChunks, engine: 'local' });
        return;
      }

      const apiKey = process.env.GEMINI_API_KEY;
      if (!apiKey) {
        console.warn("GEMINI_API_KEY is not configured. Falling back to local RAG engine.");
        const result = queryLocalRAG(message);
        res.json({ 
          reply: result.reply, 
          retrievedChunks: result.retrievedChunks,
          engine: 'local_fallback', 
          warning: "Gemini API key is not configured. Using offline RAG fallback engine." 
        });
        return;
      }

      // Initialize Gemini Client
      const ai = new GoogleGenAI({
        apiKey: apiKey,
        httpOptions: {
          headers: {
            'User-Agent': 'aistudio-build',
          }
        }
      });

      // Prepare conversation contents with strict user/model roles mapping
      const contents: any[] = [];
      if (history && Array.isArray(history)) {
        for (const msg of history) {
          if (msg.id === 'welcome') continue; // skip the initial greeting template

          // Clean out previous indicators so the model context is clean and raw
          const cleanedContent = msg.content
            .replace(/^\*\[⚡ Offline Local RAG Engine Active\]\*\s*/i, '')
            .replace(/^\*\[✨ Gemini-3.5-Flash Active \| RAG Grounded\]\*\s*/i, '')
            .replace(/^\*\[⚡ Local Sandbox RAG Engine Active\]\*\s*/i, '')
            .trim();

          if (cleanedContent) {
            contents.push({
              role: msg.role === 'user' ? 'user' : 'model',
              parts: [{ text: cleanedContent }]
            });
          }
        }
      }

      // Add the final user query
      contents.push({
        role: 'user',
        parts: [{ text: message }]
      });

      // Call Gemini 3.5 Flash Model
      const response = await ai.models.generateContent({
        model: "gemini-3.5-flash",
        contents: contents,
        config: {
          systemInstruction: `You are a digital representation of SrinivasKalyan Buthkur, acting as his Digital Interviewer & Portfolio Intelligence Agent.
Your goal is to answer questions about Srinivas's professional experience, technical skills, project history, and architecture philosophy.

Ground all your responses STRICTLY in the following resume data:
----------------------------------
Candidate Name: SrinivasKalyan Buthkur
Professional Title: Senior Polyglot Backend Engineer & Automation Specialist
Location: Hyderabad, Telangana, India
Direct Contact: Email: imsrinuu@gmail.com | Phone: +91-9652613100
GitHub: github.com/imsrinuu | LinkedIn: linkedin.com/in/imsrinuu
Summary: Highly skilled and versatile backend engineer and automation specialist with over 4 years of experience building secure, high-performance polyglot microservices and intelligent automation workflows. Expert in Python, Java, and Ruby, with a proven track record of designing robust APIs, optimizing machine learning pipelines, and deploying autonomous AI agents to eliminate manual data entry. Recipient of multiple prestigious organizational awards for achieving zero-defect releases and driving technical excellence.

SKILLS:
- Languages & Frameworks: Python (Primary, FastAPI, Django), Java (Spring Boot), Ruby (Ruby on Rails / RoR), Shell Scripting
- AI, NLP & Automation: n8n (Autonomous AI Agents), Indico (NLP & Document Processing), Generative AI Integration, ETL Worker Scripts
- Data & DevOps: PostgreSQL, SQL optimization, Docker, Jenkins, CI/CD Pipelines, Git
- Systems & Security: Linux, Kali NetHunter on Android for secure mobile testing and script execution, Python Automation Scaffolding

PROFESSIONAL EXPERIENCE:
1. CGI - Senior Polyglot Backend Engineer (March 2025 - Present)
   - Architect and design polyglot microservices using Python and Java, optimizing cross-service communication and response times.
   - Maintain and optimize legacy Ruby on Rails (RoR) enterprise web applications, enhancing stability and implementing new business logic.
   - Build robust asynchronous Python worker scripts to handle complex, high-throughput ETL data pipeline tasks.
   - Integrate RESTful APIs to bridge core enterprise Java services with cutting-edge Python machine learning models.
2. CGI - Software Engineer - Backend & Automation (March 2022 - February 2025)
   - Developed advanced Python data extraction scripts to process unstructured data with high performance.
   - Engineered machine learning model transformations using Indico NLP, boosting data extraction accuracy by 85%.
   - Automated complex corporate data pipelines, drastically reducing manual database operations and ETL latency.
   - Built and maintained automated Jenkins and Docker CI/CD pipelines to ensure rapid, zero-defect software deliveries.
   - Troubleshot and resolved critical production backend bugs using Python and SQL query optimization.

PROJECT HIGHLIGHTS:
- Autonomous AI Workflows: Architected and implemented production-grade intelligent agents using n8n and Generative AI (LLMs) to completely automate high-volume data ingestion processes. Eliminated manual data entry overhead and accelerated pipeline execution times by automating document routing, text extraction, and validation.
- Mobile Security Environment: Configured and maintained a custom Kali NetHunter Linux system on Android devices to construct an on-the-go security testing and automation lab. Enabled high-portability network analysis and advanced Python automated script execution in sandboxed mobile environments.

AWARDS & RECOGNITIONS:
- GCC Excellence Award (2026, Global): Honored with the prestigious Global Competency Center (GCC) Excellence Award for outstanding engineering contributions over a 1-year tenure.
- CII AI Awards (2025, Regional): Secured Bronze Recognition at the Hyderabad-level CII AI Awards for outstanding ML modeling achievements on the landmark 'DOC AI' project.
- CGI Gold Award for Excellence (2022 - 2025, Company): Three-time recipient of CGI's highest honor for exceptional delivery, technical leadership, and peer mentoring.
- CGI 'Key Differentiator' Award (2023, Company): Awarded for achieving consistent zero-defect major product releases through rigorous unit testing and automated CI/CD scaffolding.

EDUCATION:
- Bachelor of Technology (B.Tech) from Malla Reddy Institute of Technology (Affiliated with JNTUH), Graduated 2022.
----------------------------------

INSTRUCTIONS FOR YOUR TONE AND BEHAVIOR:
- Be highly professional, intelligent, eloquent, and direct. Represent Srinivas with the utmost competence.
- If asked questions about things not found in the resume, answer politely that Srinivas specializes in backend engineering and automation, and you don't have information on that, then steer back to his core strengths (Python, Java, Ruby, n8n, Indico).
- Never make up projects, awards, or dates that are not in the resume.
- Keep responses relatively concise and punchy.
- Format your responses using standard Markdown. You can use headers (###), bold text (**), lists, or tables. Avoid excessively long blocks of text; use bullet points for readability.
- When answering, prefix the response with "*[✨ Gemini-3.5-Flash Active | RAG Grounded]*" to clearly indicate that the real Gemini model is speaking and is properly grounded.
`,
          temperature: 0.25,
        },
      });

      const reply = response.text || "I was unable to synthesize a detailed response.";
      res.json({ reply, engine: 'gemini' });
    } catch (error: any) {
      console.error("Gemini API Error, utilizing fallback RAG engine:", error);
      const result = queryLocalRAG(message);
      res.json({ 
        reply: result.reply, 
        retrievedChunks: result.retrievedChunks,
        engine: 'local_fallback', 
        error: error.message || "An error occurred with the Gemini cloud service." 
      });
    }
  });

  // Serve health endpoint
  app.get("/api/health", (req, res) => {
    res.json({ status: "healthy", timestamp: new Date().toISOString() });
  });

  // Vite middleware for development vs static serve for production
  if (process.env.NODE_ENV !== "production") {
    const vite = await createViteServer({
      server: { middlewareMode: true },
      appType: "spa",
    });
    app.use(vite.middlewares);
  } else {
    const distPath = path.join(process.cwd(), 'dist');
    app.use(express.static(distPath));
    app.get('*', (req, res) => {
      res.sendFile(path.join(distPath, 'index.html'));
    });
  }

  app.listen(PORT, "0.0.0.0", () => {
    console.log(`Server running on http://0.0.0.0:${PORT} in ${process.env.NODE_ENV || 'development'} mode`);
  });
}

startServer().catch((err) => {
  console.error("Failed to start full-stack server:", err);
});
