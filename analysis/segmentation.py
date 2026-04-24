def segment_creators(creators):
    for c in creators:
        text = " ".join(c["content_themes"]).lower()

        if "stock" in text or "investment" in text:
            c["segment"] = "Investment Educators"
        elif "saving" in text or "budget" in text:
            c["segment"] = "Budgeting Creators"
        else:
            c["segment"] = "General Finance"

    return creators