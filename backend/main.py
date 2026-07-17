from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from graph import run_pipeline

app = FastAPI(title="Industry AI Adoption Research Agent")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/generate-report")
def generate_report(industry: str = Query(..., description="e.g. IT, Finance, Healthcare")):
    report = run_pipeline(industry)
    return {"industry": industry, "report": report}

@app.get("/")
def root():
    return {"status": "running", "usage": "/generate-report?industry=finance"}