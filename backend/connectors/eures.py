import requests

def fetch_jobs(keywords: str = "data analyst", country: str = "") -> list:
    """Fetch jobs from EURES - Official EU Job Portal (31 countries)"""

    url = "https://europa.eu/eures/eures-searchengine/page/jv/search"

    params = {
        "keywords": keywords,
        "pageSize": 50,
        "pageNum": 0,
        "sortSearch": "BEST_MATCH",
    }

    if country:
        params["countryCode"] = country

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    try:
        response = requests.get(url, params=params, headers=headers, timeout=10)
        print(f"EURES status: {response.status_code}")
        print(f"EURES response: {response.text[:500]}")
        data = response.json()
    except Exception as e:
        print(f"EURES error: {e}")
        return []

    jobs = []
    for job in data.get("jobVacancies", []) or []:
        jobs.append({
            "title": job.get("title"),
            "company": job.get("employer", {}).get("name"),
            "location": job.get("positionLocation", {}).get("municipality"),
            "remote": False,
            "url": f"https://europa.eu/eures/portal/jv-se/jv-details/{job.get('id')}",
            "description": job.get("description", "")[:300] if job.get("description") else "",
            "source": "EURES 🇪🇺"
        })

    return jobs