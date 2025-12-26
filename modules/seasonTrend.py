# ======================================
# [ST-0] 시즌 키워드 추천 엔진
# ======================================
from datetime import datetime
from modules.blogCount import get_blog_metrics
from modules.demandScore import calculate_scores

SEED_KEYWORDS = [
    "연말정산", "신년운세", "설날", "겨울여행",
    "난방비", "전기요금", "환급금", "다이어트",
    "이직", "연봉", "보험", "세금"
]

def get_season_recommendations():
    now = datetime.now()
    results = []

    for kw in SEED_KEYWORDS:
        metrics = get_blog_metrics(kw, days=14)
        score = calculate_scores(metrics)

        if score["주간수요"] > metrics["prev_period"] * 1.2:
            results.append({
                "키워드": kw,
                "황금점수": score["황금키워드점수"],
                "경쟁도": score["경쟁도"]
            })

    results.sort(key=lambda x: x["황금점수"], reverse=True)
    return results[:10]
