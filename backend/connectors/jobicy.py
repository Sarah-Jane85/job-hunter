import requests

def fetch_jobs(keywords: str = "data analyst") -> list:
    """Fetch remote jobs from Jobicy API"""

    url = "https://jobicy.com/api/v2/remote-jobs"

    params = {
        "count": 50,
        "tag": keywords,
    }

    response = requests.get(url, params=params)
    data = response.json()

    jobs = []
    for job in data.get("jobs", []):
        jobs.append({
            "title": job.get("jobTitle"),
            "company": job.get("companyName"),
            "location": "Remote 🌍",
            "salary_min": None,
            "salary_max": None,
            "url": job.get("url"),
            "description": job.get("jobExcerpt", "")[:300],
            "source": "Jobicy 🌍"
        })

    return jobs