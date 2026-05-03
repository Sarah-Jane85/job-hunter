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
        job_geo = job.get("jobGeo", "Anywhere")
        
        # Normalize location restrictions
        if not job_geo or job_geo.lower() in ["anywhere", "worldwide", ""]:
            location_str = "Worldwide 🌍"
            location_restrictions = []
        else:
            location_str = job_geo
            location_restrictions = [job_geo]

        jobs.append({
            "title": job.get("jobTitle"),
            "company": job.get("companyName"),
            "location": location_str,
            "location_restrictions": location_restrictions,
            "remote": True,
            "salary_min": job.get("annualSalaryMin"),
            "salary_max": job.get("annualSalaryMax"),
            "url": job.get("url"),
            "description": job.get("jobExcerpt", "")[:300],
            "source": "Jobicy 🌍"
        })

    return jobs