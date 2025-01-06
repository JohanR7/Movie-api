import requests
from django.conf import settings

url_base = "https://api.themoviedb.org/3"

def fetch(endpoint, params=None):
    params = params or {}
    params["api_key"] = settings.TMDB_API_KEY 

    try:
        url = f"{url_base}/{endpoint}"
        response = requests.get(url, params=params)
        response.raise_for_status()  
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
