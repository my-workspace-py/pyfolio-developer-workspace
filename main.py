# main.py
"""
SrinivasKalyan Buthkur - FastAPI RAG Web App Entry Point
-------------------------------------------------------
A clean, modular FastAPI web application providing the RAG Chatbot API.
Can be executed locally or on any external server environment:

To run:
    pip install fastapi uvicorn
    python main.py
"""

import sys
import os
import time
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

# Import modular configuration, constants, and utilities
from config import settings
from constants import RESUME_DATA
from utils import get_local_rag_response

# Initialize the FastAPI App
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Corporate Interview Portfolio & RAG AI Agent Backed by Python FastAPI"
)

# Set up CORS Middleware for remote connection capability
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------------------------------------
# PYDANTIC SCHEMAS
# -------------------------------------------------------------
class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    reply: str

# -------------------------------------------------------------
# API ROUTERS
# -------------------------------------------------------------
@app.post("/api/chat", response_model=ChatResponse, tags=["RAG Chatbot"])
async def handle_rag_chat(request: ChatRequest):
    """
    POST /api/chat
    Receives user prompts, processes them via local semantic search indexing,
    and returns rich markdown responses regarding Srinivas's professional portfolio.
    """
    if not request.message or not request.message.strip():
        raise HTTPException(status_code=400, detail="Message content cannot be blank.")
    
    try:
        # Simulate network thinking latency for realistic human-like conversation flow
        time.sleep(0.3)
        reply_content = get_local_rag_response(request.message)
        return ChatResponse(reply=reply_content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"RAG processing failure: {str(e)}")

@app.get("/api/health", tags=["Telemetry"])
async def check_health():
    """
    GET /api/health
    Basic telemetry status check for CI/CD environments.
    """
    return {
        "status": "healthy",
        "timestamp": time.time(),
        "framework": "FastAPI (Python)",
        "candidate": RESUME_DATA["profile"]["name"]
    }

# -------------------------------------------------------------
# STATIC FILE SERVING FOR REACT SINGLE PAGE APPLICATION (SPA)
# -------------------------------------------------------------
# If React's build 'dist' directory exists, serve those static assets automatically
if os.path.exists(settings.STATIC_DIR):
    app.mount("/assets", StaticFiles(directory=os.path.join(settings.STATIC_DIR, "assets")), name="assets")

    @app.get("/{full_path:path}")
    async def serve_spa(full_path: str):
        # Prevent API routing interception
        if full_path.startswith("api/"):
            raise HTTPException(status_code=404, detail="API Route Not Found")
        
        index_file = os.path.join(settings.STATIC_DIR, "index.html")
        if os.path.exists(index_file):
            return FileResponse(index_file)
        return {"message": "Srinivas Portfolio Backend is Running. React client not built yet."}
else:
    @app.get("/")
    async def root_fallback():
        return {
            "message": "Srinivas Portfolio FastAPI is running!",
            "api_endpoint": "POST /api/chat",
            "documentation": "/docs"
        }

# -------------------------------------------------------------
# DIRECT EXECUTION
# -------------------------------------------------------------
if __name__ == "__main__":
    import uvicorn
    print("=" * 80)
    print(f"      LAUNCHING {settings.PROJECT_NAME.upper()} (v{settings.VERSION})")
    print(f"      Host: {settings.HOST} | Port: {settings.PORT}")
    print("=" * 80)
    uvicorn.run("main:app", host=settings.HOST, port=settings.PORT, reload=settings.DEBUG)
