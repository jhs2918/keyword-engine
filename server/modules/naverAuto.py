import requests

def get_naver_autocomplete(q):
    try:
        r = requests.get(
            "https://ac.search.naver.com/nx/ac",
            params={"q": q, "st": 100},
            timeout=5
        )
        data = r.json()
        return [x[0] for x in data["items"][0]]
    except:
        return []
