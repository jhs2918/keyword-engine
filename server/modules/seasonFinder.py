from datetime import datetime, timedelta
from pytrends.request import TrendReq
import time

print("### SEASON FINDER LOADED ###")

def _season_ranges():
    today = datetime.today()
    ranges = []
    for y in [1, 2]:
        base = today.replace(year=today.year - y)
        ranges.append((
            base - timedelta(days=30),
            base + timedelta(days=30)
        ))
    return ranges


def find_season_seeds():
    print("### SEASON FINDER RUNNING ###")

    pytrends = TrendReq(
        hl="ko-KR",
        tz=540,
        timeout=(10, 25),
        retries=1,
        backoff_factor=0.8
    )

    # 🔥 계절 무관 범용 seed
    base_terms = [
        "겨울 여행",
        "겨울 추천",
        "겨울 할인",
        "연말 이벤트",
        "12월 할인",
        "겨울 준비"
    ]

    rising = []

    for term in base_terms:
        score = 0

        for start, end in _season_ranges():
            timeframe = f"{start:%Y-%m-%d} {end:%Y-%m-%d}"

            try:
                pytrends.build_payload([term], timeframe=timeframe, geo="KR")
                df = pytrends.interest_over_time()
                if df.empty:
                    continue

                avg = df[term].mean()
                last = df[term].iloc[-1]

                # ✅ 완화 조건: 평균 이상 유지
                if last >= avg:
                    score += 1

                time.sleep(2)

            except Exception:
                break

        if score >= 1:
            rising.append(term)

    return rising
