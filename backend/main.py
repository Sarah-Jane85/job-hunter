from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.connectors.arbeitnow import fetch_jobs

app = FastAPI(title="Job Hunter API")

# This allows our frontend to talk to our backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Job Hunter API is running!"}

@app.get("/jobs/arbeitnow")
def get_arbeitnow_jobs(keywords: str = "data analyst"):
    jobs = fetch_jobs(keywords=keywords)
    return {"source": "Arbeitnow", "count": len(jobs), "jobs": jobs}