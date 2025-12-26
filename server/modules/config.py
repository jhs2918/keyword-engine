


# ======================================
# [C-0] 공통 설정
# ======================================

# 네이버 검색 Open API (Blog Search)
# https://developers.naver.com/docs/serviceapi/search/blog/blog.md
NAVER_CLIENT_ID = "72hzNZBkDBw4Ru2HxdQR"
NAVER_CLIENT_SECRET = "jBKeh6Ta0K"

REQUEST_TIMEOUT = 10  # seconds

# UA는 막힘/429 완화에 도움
DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) keyword-engine/1.0"
}
