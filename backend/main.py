from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.connectors.arbeitnow import fetch_jobs as arbeitnow_jobs
from backend.connectors.adzuna import fetch_jobs as adzuna_jobs

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
    jobs = arbeitnow_jobs(keywords=keywords)
    return {"source": "Arbeitnow", "count": len(jobs), "jobs": jobs}

@app.get("/jobs/adzuna/{country}")
def get_adzuna_jobs(country: str = "de", keywords: str = "data analyst"):
    jobs = adzuna_jobs(keywords=keywords, country=country)
    return {"source": f"Adzuna {country.upper()}", "count": len(jobs), "jobs": jobs}