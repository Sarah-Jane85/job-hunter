import requests
import os
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("ADZUNA_APP_ID")
APP_KEY = os.getenv("ADZUNA_APP_KEY")

COUNTRIES = {
    "de": "Germany 🇩🇪",
    "nl": "Netherlands 🇳🇱",
    "es": "Spain 🇪🇸",
    "pt": "Portugal 🇵🇹",
}

def fetch_jobs(keywords: str = "data analyst", country: str = "de") -> list:
    """Fetch jobs from Adzuna API for a given country"""

    url = f"https://api.adzuna.com/v1/api/jobs/{country}/search/1"

    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "what": keywords,
        "results_per_page": 50,
    }

    response = requests.get(url, params=params)
    data = response.json()

    jobs = []
    for job in data.get("results", []):
        jobs.append({
            "title": job.get("title"),
            "company": job.get("company", {}).get("display_name"),
            "location": job.get("location", {}).get("display_name"),
            "salary_min": job.get("salary_min"),
            "salary_max": job.get("salary_max"),
            "url": job.get("redirect_url"),
            "description": job.get("description", "")[:300],
            "source": f"Adzuna {COUNTRIES.get(country, country)}"
        })

    return jobs