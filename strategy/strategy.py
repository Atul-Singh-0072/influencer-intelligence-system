def assign_strategy(creators):
    for c in creators:
        niche = c["niche"]

        if niche in ["stock", "investment"]:
            c["collaboration_type"] = "Affiliate partnership"
        elif niche in ["saving", "budget"]:
            c["collaboration_type"] = "App demo collaboration"
        else:
            c["collaboration_type"] = "Brand awareness"

    return creators