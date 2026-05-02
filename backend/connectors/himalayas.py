import requests

def fetch_jobs(keywords: str = "data analyst") -> list:
    """Fetch remote jobs from Himalayas API"""

    url = "https://himalayas.app/jobs/api/search"

    params = {
        "q": keywords,
        "limit": 50,
    }

    response = requests.get(url, params=params)
    data = response.json()

    jobs = []
    for job in data.get("jobs", []):
        jobs.append({
            "title": job.get("title"),
            "company": job.get("company", {}).get("name"),
            "location": "Remote 🌍",
            "salary_min": job.get("salaryMin"),
            "salary_max": job.get("salaryMax"),
            "url": job.get("applicationLink"),
            "description": job.get("description", "")[:300],
            "source": "Himalayas 🌍"
        })

    return jobs