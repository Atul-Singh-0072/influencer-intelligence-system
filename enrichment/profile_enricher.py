def enrich_profiles(creators):
    for c in creators:
        c["profile_link"] = f"https://youtube.com/channel/{c['channel_id']}"
        c["engagement_rate"] = round(2 + c["recent_posts"] * 0.5, 2)
        c["niche"] = c["content_themes"][0]
        c["email"] = "Not available"

    return creators