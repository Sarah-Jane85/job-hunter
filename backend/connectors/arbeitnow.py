import requests

def fetch_jobs(keywords: str = "data analyst", location: str = "germany") -> list:
    """Fetch jobs from Arbeitnow API"""
    
    url = "https://www.arbeitnow.com/api/job-board-api"
    
    response = requests.get(url)
    data = response.json()
    
    jobs = []
    for job in data.get("data", []):
        jobs.append({
            "title": job.get("title"),
            "company": job.get("company_name"),
            "location": job.get("location"),
            "remote": job.get("remote", False),
            "url": job.get("url"),
            "description": job.get("description", "")[:300],
            "source": "Arbeitnow"
        })
    
    return jobs