import requests 
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

API_KEY = "a434088afc05a21e91006b975795b5c1"

url = "https://api.themoviedb.org/3/movie/9304"

try:
    response = requests.get(
        url,
        params={"api_key": API_KEY},
        timeout=20
    )

    print("STATUS:", response.status_code)
    print("RESPONSE:", response.text[:500])

except Exception as e:
    print("ERROR:", repr(e))


