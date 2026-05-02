import requests
import base64
import urllib3

# The API uses a public key, no registration needed!
HEADERS = {
    'User-Agent': 'Jobsuche/2.9.2 (de.arbeitsagentur.jobboerse; build:1077; iOS 15.1.0) Alamofire/5.4.4',
    'Host': 'rest.arbeitsagentur.de',
    'X-API-Key': 'jobboerse-jobsuche',
    'Connection': 'keep-alive',
}

def fetch_jobs(keywords: str = "data analyst", location: str = "Deutschland") -> list:
    """Fetch jobs from Bundesagentur für Arbeit (official German job board)"""

    # Suppress SSL warnings
    urllib3.disable_warnings()

    params = {
        'angebotsart': '1',  # Job offers
        'page': '1',
        'pav': 'false',
        'size': '50',
        'umkreis': '50',     # 50km radius
        'was': keywords,
        'wo': location,
    }

    response = requests.get(
        'https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/app/jobs',
        headers=HEADERS,
        params=params,
        verify=False
    )

    data = response.json()
    jobs = []

    for job in data.get("stellenangebote") or []:
        jobs.append({
            "title": job.get("titel"),
            "company": job.get("arbeitgeber"),
            "location": job.get("arbeitsort", {}).get("ort"),
            "remote": False,
            "url": f"https://www.arbeitsagentur.de/jobsuche/jobdetail/{job.get('refnr')}",
            "description": job.get("kurzbeschreibung", "")[:300] if job.get("kurzbeschreibung") else "",
            "source": "Arbeitsagentur 🇩🇪"
        })

    return jobs