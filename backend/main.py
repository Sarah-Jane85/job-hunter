from fastapi.concurrency import run_in_threadpool
import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.connectors.arbeitnow import fetch_jobs as arbeitnow_jobs
from backend.connectors.adzuna import fetch_jobs as adzuna_jobs
from backend.connectors.himalayas import fetch_jobs as himalayas_jobs
from backend.connectors.jobicy import fetch_jobs as jobicy_jobs
from backend.connectors.arbeitsagentur import fetch_jobs as arbeitsagentur_jobs
from backend.connectors.nationale_vacaturebank import fetch_jobs as nvb_jobs
from backend.connectors.eures import fetch_jobs as eures_jobs
from backend.utils import normalize_german

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
def get_adzuna_jobs(country: str = "de", keywords: str = "data analyst", location: str = ""):
    jobs = adzuna_jobs(keywords=keywords, country=country, location=location)
    return {"source": f"Adzuna {country.upper()}", "count": len(jobs), "jobs": jobs}

@app.get("/jobs/himalayas")
def get_himalayas_jobs(keywords: str = "data analyst"):
    jobs = himalayas_jobs(keywords=keywords)
    return {"source": "Himalayas", "count": len(jobs), "jobs": jobs}

@app.get("/jobs/jobicy")
def get_jobicy_jobs(keywords: str = "data analyst"):
    jobs = jobicy_jobs(keywords=keywords)
    return {"source": "Jobicy", "count": len(jobs), "jobs": jobs}

@app.get("/jobs/arbeitsagentur")
def get_arbeitsagentur_jobs(keywords: str = "data analyst", location: str = "Deutschland"):
    jobs = arbeitsagentur_jobs(keywords=keywords, location=location)
    return {"source": "Arbeitsagentur", "count": len(jobs), "jobs": jobs}

@app.get("/jobs/nationalevacaturebank")
def get_nvb_jobs(keywords: str = "data analyst", location: str = ""):
    jobs = nvb_jobs(keywords=keywords, location=location)
    return {"source": "Nationale Vacaturebank", "count": len(jobs), "jobs": jobs}

@app.get("/jobs/eures")
def get_eures_jobs(keywords: str = "data analyst", country: str = ""):
    jobs = eures_jobs(keywords=keywords, country=country)
    return {"source": "EURES", "count": len(jobs), "jobs": jobs}

@app.get("/jobs/all")
async def get_all_jobs(keywords: str = "data analyst", location: str = ""):
    location = normalize_german(location)
    keywords = normalize_german(keywords)
    """Search all sources at once and return combined results"""

    results = await asyncio.gather(
        run_in_threadpool(arbeitnow_jobs, keywords=keywords, location=location),
        run_in_threadpool(adzuna_jobs, keywords=keywords, country="de", location=location),
        run_in_threadpool(adzuna_jobs, keywords=keywords, country="nl", location=location),
        run_in_threadpool(adzuna_jobs, keywords=keywords, country="es", location=location),
        run_in_threadpool(himalayas_jobs, keywords=keywords),
        run_in_threadpool(jobicy_jobs, keywords=keywords),
        run_in_threadpool(arbeitsagentur_jobs, keywords=keywords, location=location or "Deutschland"),
        return_exceptions=True
    )

    all_jobs = []
    for result in results:
        if isinstance(result, Exception):
            print(f"Connector error: {result}")
            continue
        all_jobs.extend(result)

    return {
        "keywords": keywords,
        "location": location,
        "count": len(all_jobs),
        "jobs": all_jobs
    }