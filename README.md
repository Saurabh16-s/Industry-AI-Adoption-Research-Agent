# Industry AI Adoption Research Agent

A simple 3-node LangGraph-style pipeline (search → summarize → report) that
researches how different industries train employees on AI tools, and generates
structured case-study reports.

## Setup
1. `cd backend`
2. `python -m venv venv && source venv/bin/activate` (or `venv\Scripts\activate` on Windows)
3. `pip install -r requirements.txt`
4. Add your API keys to `.env`
5. `uvicorn main:app --reload`
6. Open `frontend/index.html` in your browser

## How it works
- **search_node**: queries Tavily for how a given industry trains employees on AI
- **summarize_node**: Gemini extracts key bullet points from raw search results
- **report_node**: Gemini compiles a structured markdown case-study report, saved to /reports