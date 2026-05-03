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
    location_restrictions = job.get("locationRestrictions", [])
    location_str = ", ".join([r.get("name", "") for r in location_restrictions]) if location_restrictions else "Worldwide 🌍"

    jobs = []
    for job in data.get("jobs", []):
        jobs.append({
            "title": job.get("title"),
            "company": job.get("company", {}).get("name"),
            "location": location_str,
            "location_restrictions": [r.get("name", "") for r in location_restrictions],
            "remote": True,
            "salary_min": job.get("minSalary"),
            "salary_max": job.get("maxSalary"),
            "url": job.get("applicationLink"),
            "description": job.get("description", "")[:500],
            "source": "Himalayas 🌍"
        })

    return jobs