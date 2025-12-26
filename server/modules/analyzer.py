from server.modules.keywordExpand import expand_keywords
from server.modules.blogCount import get_blog_count
from server.modules.demandScore import calc_score


def analyze_keyword(keyword: str):
    keywords = expand_keywords(keyword)

    results = []
    for kw in keywords:
        try:
            blog_cnt = get_blog_count(kw)
            score = calc_score(blog_cnt)

            results.append({
                "키워드": kw,
                "블로그경쟁": blog_cnt,
                "상위가능성": score,
                "추천": "★" if score >= 80 else ""
            })

        except Exception as e:
            results.append({
                "키워드": kw,
                "블로그경쟁": 0,
                "상위가능성": 0,
                "추천": "",
                "error": str(e)
            })

    return sorted(results, key=lambda x: x["상위가능성"], reverse=True)
