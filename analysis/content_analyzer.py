IMPORTANT_WORDS = [
    "finance","money","saving","investment","inflation",
    "stock","mutual","fund","sip","budget","tax","income"
]

def analyze_content(creators):
    for c in creators:
        combined = " ".join(c["titles"] + c["descriptions"]).lower()

        found = [word for word in IMPORTANT_WORDS if word in combined]

        if not found:
            found = ["finance"]

        c["content_themes"] = found[:3]
        c["recent_content"] = c["titles"][0]

    return creators