# ======================================
# [AC-0] 자동완성 (확장용)
# ======================================
def get_autocomplete(keyword: str) -> list:
    if not keyword:
        return []
    suffix = ["방법", "후기", "가격", "추천", "정리"]
    return [f"{keyword} {s}" for s in suffix]
