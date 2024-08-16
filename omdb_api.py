import requests


def fetch_movie_details(api_key, title):
    url = f"http://www.omdbapi.com/?apikey={api_key}&t={title}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
