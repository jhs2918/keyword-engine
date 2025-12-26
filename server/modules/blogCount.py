import requests
from urllib.parse import quote
from .config import NAVER_CLIENT_ID, NAVER_CLIENT_SECRET, REQUEST_TIMEOUT, DEFAULT_HEADERS


def get_blog_count(keyword: str) -> int:
    url = (
        "https://openapi.naver.com/v1/search/blog.json"
        f"?query={quote(keyword)}&display=1"
    )

    headers = dict(DEFAULT_HEADERS)
    headers.update({
        "X-Naver-Client-Id": NAVER_CLIENT_ID,
        "X-Naver-Client-Secret": NAVER_CLIENT_SECRET
    })

    r = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)

    if r.status_code != 200:
        # API 실패 시 아주 큰 값으로 처리
        return 999999

    data = r.json()
    total = int(data.get("total", 0))

    if total <= 0:
        return 999999

    return total
