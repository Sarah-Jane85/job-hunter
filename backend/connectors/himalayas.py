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
        location_restrictions = job.get("locationRestrictions", [])
        
        if isinstance(location_restrictions, list) and len(location_restrictions) > 0:
            if isinstance(location_restrictions[0], dict):
                location_names = [r.get("name", "") for r in location_restrictions]
            else:
                location_names = location_restrictions
            location_str = ", ".join(location_names)
        else:
            location_names = []
            location_str = "Worldwide 🌍"

        jobs.append({
            "title": job.get("title"),
            "company": job.get("company", {}).get("name"),
            "location": location_str,
            "location_restrictions": location_names,
            "remote": True,
            "salary_min": job.get("minSalary"),
            "salary_max": job.get("maxSalary"),
            "url": job.get("applicationLink"),
            "description": job.get("description", "")[:500],
            "source": "Himalayas 🌍"
        })

    return jobs