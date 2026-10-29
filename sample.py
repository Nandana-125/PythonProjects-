# Write paginate(items, *, page=1, size=10) -> dict returning {"items": [...], "total": n, "page": page, "pages": p}.
#  Raise ValueError if page or size is below 1. paginate(list(range(25)), page=3, size=10) should give items [20..24]


def paginate(items: list, *, page=1, size=10) -> dict:

    total = len(items)
    p = -(-total // size)  # ciel value
    start = (page - 1) * size

    return {
        "items": items[start : start + size],
        "total": total,
        "page": page,
        "pages": p,
    }


data = list(range(20))

print(paginate(data, page=1, size=10))
