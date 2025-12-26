



# ======================================
# [SE-0] 광범위 시즌 키워드 탐색 엔진
# ======================================
from datetime import datetime
from modules.naverAuto import get_naver_autocomplete
from modules.googleAuto import get_google_autocomplete

def _month_context_terms(month: int):
    # 월별 맥락 단어 (고정 seed 아님, 맥락용)
    return [
        f"{month}월",
        "봄" if month in [3,4,5] else "",
        "여름" if month in [6,7,8] else "",
        "가을" if month in [9,10,11] else "",
        "겨울" if month in [12,1,2] else ""
    ]

def explore_season_keywords():
    now = datetime.now()
    month = now.month

    context_terms = _month_context_terms(month)

    pool = set()

    # [SE-1] 네이버 자동완성 기반 광범위 수집
    for term in context_terms:
        if term:
            pool.update(get_naver_autocomplete(term))

    # [SE-2] 구글 자동완성 기반 광범위 수집
    for term in context_terms:
        if term:
            pool.update(get_google_autocomplete(term))

    # 너무 짧은 키워드 제거
    pool = {k for k in pool if len(k) >= 2}

    return list(pool)
