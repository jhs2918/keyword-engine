def calc_score(blog_count: int) -> int:
    if blog_count <= 500:
        return 95
    if blog_count <= 1000:
        return 90
    if blog_count <= 3000:
        return 80
    if blog_count <= 7000:
        return 65
    if blog_count <= 15000:
        return 50
    return 30
