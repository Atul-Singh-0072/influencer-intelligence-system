INDIA_KEYWORDS = ["india", "indian", "₹", "rupee", "hindi", "delhi", "mumbai"]

def filter_creators(creators):
    filtered = []

    for c in creators:
        text = " ".join(c["titles"]).lower()

        # Followers filter
        if not (5000 <= c["followers"] <= 100000):
            continue

        # Must have recent content
        if c["recent_posts"] == 0:
            continue

        # Soft India relevance scoring
        india_score = sum(1 for word in INDIA_KEYWORDS if word in text)
        c["india_score"] = india_score

        filtered.append(c)

    return filtered