def compute_brand_fit(creators, brand_context):
    brand_keywords = ["finance", "saving", "investment", "money"]

    for c in creators:
        overlap = len(set(brand_keywords) & set(c["content_themes"]))
        keyword_score = overlap / len(brand_keywords)

        engagement = c["engagement_rate"] / 10
        activity = min(c["recent_posts"] / 5, 1)

        c["brand_fit_score"] = round(
            keyword_score * 0.8 +
            engagement * 0.1 +
            activity * 0.1,
            2
        )

    return sorted(creators, key=lambda x: x["brand_fit_score"], reverse=True)