import random
import string
import re


def clean(s: str) -> str:
    return re.sub(r'[^A-Za-zА-Яа-я0-9]', '', s).upper()

def levenshtein(a: str, b: str) -> int:
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

    for i in range(len(a) + 1):
        dp[i][0] = i
    for j in range(len(b) + 1):
        dp[0][j] = j

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            cost = 0 if a[i - 1] == b[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,
                dp[i][j - 1] + 1,
                dp[i - 1][j - 1] + cost)
    return dp[-1][-1]

def sim(a: str, b: str) -> float:
    dist = levenshtein(a, b)
    max_len = max(len(a), len(b))
    if max_len == 0:
        return 1.0
    return 1 - dist / max_len

def generate_code():
    base = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
    noise = ''.join(random.choices("!@#$%", k=2))
    return base + noise

def create_data():
    biglist = {}
    for i in range(50):
        biglist[i] = generate_code()
    wishlist = {}
    for i in range(10):
        key = random.choice(list(biglist.keys()))
        val = list(biglist[key])
        idx = random.randint(0, len(val) - 1)
        val[idx] = random.choice(string.ascii_letters)
        wishlist[i] = ''.join(val)
    return biglist, wishlist

def group_biglist(biglist):
    grouped = {}
    for key, value in biglist.items():
        cleaned = clean(value)
        prefix = cleaned[:2]
        if prefix not in grouped:
            grouped[prefix] = []
        grouped[prefix].append((key, cleaned))
    return grouped

def fuzzy_search_improved(wishlist, biglist, top_n=3):
    grouped = group_biglist(biglist)
    results = {}
    for wish_id, wish_val in wishlist.items():
        wish_clean = clean(wish_val)
        found_exact = False
        for key, value in biglist.items():
            if wish_clean == clean(value):
                results[wish_id] = [(key, value)]
                found_exact = True
                break
        if found_exact:
            continue
        threshold = max(0.5, 1 - 2 / len(wish_clean))
        prefix = wish_clean[:2]
        if prefix in grouped:
            candidates = grouped[prefix]
        else:
            candidates = [(k, clean(v)) for k, v in biglist.items()]
        cand = []
        for key, item_clean in candidates:
            sc = sim(wish_clean, item_clean)
            if sc >= threshold:
                cand.append((key, sc))
        cand.sort(key=lambda x: x[1], reverse=True)
        top_items = [(key, biglist[key]) for key, _ in cand[:top_n]]
        results[wish_id] = top_items
    return results
biglist, wishlist = create_data()
results = fuzzy_search_improved(wishlist, biglist)
print("\nRESULTS:")
for wish_id, items in results.items():
    print(f"{wish_id} -> {items}")