ACTION_WORDS = [
    "정리", "방법", "후기", "비교", "추천",
    "가격", "순위", "장단점", "사용법", "주의사항",
    "꿀팁", "체크리스트", "가이드", "리뷰", "총정리",
    "선택법", "차이", "필수", "이유", "조건",
    "시기", "대상", "기준", "한번에", "완벽정리",
    "요약", "쉽게", "빠르게", "핵심", "정확히"
]

def expand_keywords(base):
    result = [base]
    for w in ACTION_WORDS:
        result.append(f"{base} {w}")
        if len(result) >= 30:
            break
    return result
