# constants.py
"""
SrinivasKalyan Buthkur - RAG Database and Portfolio Constants
This module houses all the structured resume data, professional experiences,
awards, and projects for Srinivas. This serves as the primary ground-truth
knowledge base for the RAG engine.
"""

RESUME_DATA = {
    "profile": {
        "name": "SrinivasKalyan Buthkur",
        "email": "imsrinuu@gmail.com",
        "phone": "+91-9652613100",
        "location": "Hyderabad, Telangana, India",
        "role": "Senior Polyglot Backend Engineer & Automation Specialist",
        "experience_duration": "4+ Years",
        "availability": "Immediate for Senior Backend / Python roles"
    },
    "skills": [
        {
            "category": "Languages",
            "items": ["Python (Primary)", "Java", "Ruby", "TypeScript", "SQL (PostgreSQL/MySQL)"]
        },
        {
            "category": "Frameworks & APIs",
            "items": ["FastAPI", "Django", "Spring Boot", "Ruby on Rails", "Express.js", "RESTful APIs"]
        },
        {
            "category": "Automation & ML",
            "items": ["n8n (Autonomous Agents)", "Indico NLP", "pandas", "numpy", "LangChain"]
        },
        {
            "category": "Tools & Security",
            "items": ["Docker", "Git", "Jenkins CI/CD", "Linux (Kali NetHunter)", "Postman"]
        }
    ],
    "experience": [
        {
            "company": "CGI",
            "period": "March 2025 - Present",
            "role": "Senior Polyglot Backend Engineer",
            "highlights": [
                "Designed and developed highly scalable polyglot microservices in Python and Java (Spring Boot).",
                "Maintained robust enterprise Ruby on Rails applications with high test coverage.",
                "Built asynchronous Python worker scripts for high-throughput ETL data pipeline synchronization.",
                "Integrated secure, authenticated REST APIs between core Java services and external AI models."
            ]
        },
        {
            "company": "CGI",
            "period": "March 2022 - February 2025",
            "role": "Software Engineer",
            "highlights": [
                "Developed advanced Python data extraction scripts utilizing pandas, numpy, and regular expressions.",
                "Engineered ML model transformations on 'DOC AI' with Indico NLP, boosting extraction accuracy by 85%.",
                "Automated software delivery pipelines and containerized microservices using Docker and Jenkins.",
                "Resolved high-impact production database bottlenecks and application bugs using Python, Java, and raw SQL queries."
            ]
        }
    ],
    "projects": [
        {
            "title": "Autonomous AI Workflows",
            "stack": "n8n, Generative AI (LLMs), FastAPI, PostgreSQL",
            "description": "Architected and deployed intelligent agentic workflows to automate tedious business document parsing, validation, and database ingestion, completely eliminating manual operational overhead."
        },
        {
            "title": "Mobile Security & Analysis Environment",
            "stack": "Kali NetHunter, Python, Android, Bash",
            "description": "Configured a customized Kali Linux NetHunter sandbox environment on mobile devices to test and audit local Android application APIs, and automate complex local network penetration scripts."
        }
    ],
    "awards": [
        "GCC Excellence Award (2026) - Global honor for stellar delivery and technical stewardship over a 1-year tenure.",
        "CII AI Awards (2025) - Regional Bronze Recognition (Hyderabad) for machine learning models on CGI's 'DOC AI' project.",
        "CGI Gold Award for Excellence (3x Recipient) - CGI's highest delivery award for technical excellence and team mentoring.",
        "CGI 'Key Differentiator' Award (2023) - For ensuring zero-defect major product releases via automated unit/integration testing scaffolding."
    ],
    "education": {
        "degree": "Bachelor of Technology (B.Tech)",
        "college": "Malla Reddy Institute of Technology (JNTUH)",
        "grad_year": "2022"
    }
}
