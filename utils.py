# utils.py
"""
SrinivasKalyan Buthkur - RAG Utility & Query Linker
This module handles pattern recognition, structured semantic-fallback routing, and
dynamically assembles facts from the constants file to construct the RAG responses.
"""

from constants import RESUME_DATA

def get_local_rag_response(query: str) -> str:
    """
    RAG query compiler. Matches core semantic concepts in user queries and 
    merges them with ground-truth data from constants.py.
    """
    q = query.lower()
    p = RESUME_DATA["profile"]
    edu = RESUME_DATA["education"]
    
    # 1. Why Hire / Suitability
    if any(k in q for k in ["why hire", "hire you", "why should", "reason", "hiring", "fit", "achieve", "strength"]):
        return (
            "[⚡ Offline Python RAG Engine Active]\n\n"
            "I bring over **4 years of polyglot backend engineering experience** from CGI, where I consistently delivered zero-defect major product releases:\n"
            f"- **Polyglot Excellence**: Expert-level mastery of **Python (Primary)**, paired with solid professional experience in **Java (Spring Boot)** and **Ruby (Rails)**.\n"
            "- **Enterprise Automation**: Built production-ready autonomous agents using **n8n** and custom Python orchestration scripts, reducing manual operations and ETL latency.\n"
            "- **ML & Document Extraction**: Boosted document accuracy by **85%** on the 'DOC AI' project using Indico NLP transforms and pandas.\n"
            "- **Leadership & Excellence**: Recipient of 3x CGI Gold Awards, CGI Key Differentiator Award, and GCC Excellence Award."
        )
        
    # 2. Python Stack / Technologies / Architecture
    elif any(k in q for k in ["portfolio", "code", "architecture", "how it works", "stack", "api", "rag"]):
        if "python" in q:
            return (
                "[⚡ Offline Python RAG Engine Active]\n\n"
                "**Python is my primary and strongest stack.** Over my 4+ years of professional experience, I have developed:\n"
                "- **Web APIs**: High-performance asynchronous microservices using **FastAPI** and robust web frameworks with **Django**.\n"
                "- **Data Engineering**: Asynchronous worker scripts, data cleaning pipelines with **pandas/numpy**, and batch ETL operations.\n"
                "- **Integrations**: Writing Python scripts to proxy payloads, bridge Java core APIs with Indico NLP systems, and automate local Android network security testing with custom **Kali NetHunter** scripts."
            )
        return (
            "[⚡ Offline Python RAG Engine Active]\n\n"
            "This portfolio showcases a full-stack RAG (Retrieval-Augmented Generation) pipeline:\n"
            "- **Frontend**: A highly polished, single-page React app built with **Vite, Tailwind CSS, and Framer Motion**, simulating an engineer's workspace (RAG Chatbot + TTY Terminal Emulator).\n"
            "- **Backend**: A pythonic FastAPI endpoint `/api/chat` that coordinates conversation history and feeds context to this local RAG engine to provide immediate, fully grounded answers.\n"
            "- **Resilient Offline Architecture**: If the backend is offline, the React app contains a client-side matching twin so the system never fails."
        )
        
    # 3. Doc AI / ML / NLP / Indico
    elif any(k in q for k in ["doc ai", "indico", "ml", "nlp", "cgi ml", "document", "extract"]):
        return (
            "[⚡ Offline Python RAG Engine Active]\n\n"
            "In my Software Engineer role at CGI (2022 - 2025), I engineered critical ML model transformations on the **DOC AI** project:\n"
            "- **ML Transformations**: Used **Indico NLP** and **Python (pandas/numpy)** to preprocess and structure massive unstructured documents.\n"
            "- **Accuracy Boost**: Increased data extraction precision by **85%**, eliminating manual database operations.\n"
            "- **Awards**: This work earned regional **CII AI Awards Bronze Recognition** (Hyderabad, 2025) and CGI Gold Awards."
        )
        
    # 4. n8n / Workflow Automation
    elif any(k in q for k in ["n8n", "workflow", "agent", "automation", "autonomous"]):
        return (
            "[⚡ Offline Python RAG Engine Active]\n\n"
            "I architected and deployed intelligent agents using **n8n** and **Generative AI** (LLMs):\n"
            "- **Intelligent Pipelines**: Completely eliminated manual document indexing and ingestion overhead.\n"
            "- **Stack**: Combined **n8n Webhooks**, **Python Webhooks (FastAPI)**, and PostgreSQL to build custom data transformation and validation pipelines.\n"
            "- **Business Outcome**: Accelerated overall pipeline execution, allowing business analysts to focus on analysis rather than repetitive data entry."
        )
        
    # 5. Awards / Recognitions
    elif any(k in q for k in ["award", "honor", "gcc", "cii", "gold"]):
        awards_list = "\n".join(f"- {a}" for a in RESUME_DATA["awards"])
        return (
            "[⚡ Offline Python RAG Engine Active]\n\n"
            "I have been honored with multiple global and regional awards:\n"
            f"{awards_list}"
        )
        
    # 6. Education / University
    elif any(k in q for k in ["education", "college", "university", "degree", "malla"]):
        return (
            "[⚡ Offline Python RAG Engine Active]\n\n"
            f"I graduated in **{edu['grad_year']}** with a **{edu['degree']}** from **{edu['college']}**, affiliated with JNTUH."
        )
        
    # 7. Contact Details
    elif any(k in q for k in ["contact", "email", "phone", "location", "resume"]):
        return (
            "[⚡ Offline Python RAG Engine Active]\n\n"
            "Here is my direct contact information:\n"
            f"- **Email**: {p['email']}\n"
            f"- **Phone**: {p['phone']}\n"
            f"- **Location**: {p['location']}\n"
            f"- **Availability**: {p['availability']}"
        )

    # 8. Python specific questions
    elif "python" in q:
        return (
            "[⚡ Offline Python RAG Engine Active]\n\n"
            "**Python is my primary and strongest stack.** Over my 4+ years of professional experience, I have developed:\n"
            "- **Web APIs**: High-performance asynchronous microservices using **FastAPI** and robust web frameworks with **Django**.\n"
            "- **Data Engineering**: Asynchronous worker scripts, data cleaning pipelines with **pandas/numpy**, and batch ETL operations.\n"
            "- **Integrations**: Writing Python scripts to proxy payloads, bridge Java core APIs with Indico NLP systems, and automate local Android network security testing with custom **Kali NetHunter** scripts."
        )

    # Default Fallback
    return (
        "[⚡ Offline Python RAG Engine Active]\n\n"
        "I'd be happy to share details about that! Here is a high-level overview of my professional background:\n"
        f"- **Experience**: {p['experience_duration']} of backend and automation engineering at CGI.\n"
        f"- **Primary Stack**: **Python (FastAPI, Django)**, **Java (Spring Boot)**, **Ruby on Rails**, and **PostgreSQL**.\n"
        "- **Key Specializations**: **n8n autonomous AI workflows**, **Indico NLP**, and secure asynchronous ETL processing.\n"
        "- **Awards**: Winner of GCC Excellence Award (2026) and 3x CGI Gold Awards.\n"
        f"- **Immediate Availability**: {p['availability']}\n\n"
        "*Feel free to ask specific questions about my projects, Python scripts, or award criteria!*"
    )
