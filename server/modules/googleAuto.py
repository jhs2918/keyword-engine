import requests

def get_google_autocomplete(q):
    try:
        r = requests.get(
            "https://suggestqueries.google.com/complete/search",
            params={"client": "firefox", "q": q},
            timeout=5
        )
        return r.json()[1]
    except:
        return []
