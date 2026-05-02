import requests

def fetch_jobs(keywords: str = "data analyst", location: str = "") -> list:
    """Fetch jobs from Arbeitnow API"""

    url = "https://www.arbeitnow.com/api/job-board-api"

    response = requests.get(url, timeout=10)
    data = response.json()

    keywords_lower = keywords.lower().split()

    jobs = []
    for job in data.get("data", []):
        title = job.get("title", "").lower()
        description = job.get("description", "").lower()
        job_location = job.get("location", "").lower()

        # Filter by keywords
        if not any(kw in title or kw in description for kw in keywords_lower):
            continue

        # Filter by location if provided
        if location and location.lower() not in job_location:
            continue

        jobs.append({
            "title": job.get("title"),
            "company": job.get("company_name"),
            "location": job.get("location"),
            "remote": job.get("remote", False),
            "url": job.get("url"),
            "description": job.get("description", "")[:300],
            "source": "Arbeitnow 🇩🇪"
        })

    return jobs