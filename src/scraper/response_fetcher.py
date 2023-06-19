import requests

def fetch_response(base_url, id):
    url = f"{base_url}{id}"
    response = requests.get(url)
    
    return id, response