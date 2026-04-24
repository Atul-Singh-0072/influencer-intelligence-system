from discovery.youtube_discovery import search_youtube_creators
from filtering.filter_engine import filter_creators
from analysis.content_analyzer import analyze_content
from analysis.segmentation import segment_creators
from enrichment.profile_enricher import enrich_profiles
from scoring.brand_fit import compute_brand_fit
from messaging.generator import generate_messages
from strategy import assign_strategy

import json

def run_pipeline(keyword, brand_context):
    print("\n🚀 Starting Pipeline...\n")

    creators = search_youtube_creators(keyword)
    print("Found:", len(creators))

    creators = filter_creators(creators)
    creators = analyze_content(creators)
    creators = segment_creators(creators)
    creators = enrich_profiles(creators)
    creators = compute_brand_fit(creators, brand_context)
    creators = assign_strategy(creators)
    creators = generate_messages(creators, brand_context)

    return creators


if __name__ == "__main__":
    keyword = "personal finance India Hindi"
    brand_context = "fintech app for saving and investing in India"

    output = run_pipeline(keyword, brand_context)

    top = output[:2]

    with open("data/sample_output.json", "w") as f:
        json.dump(top, f, indent=2)

    for c in top:
        print("\n🔥", c["name"])
        print("Score:", c["brand_fit_score"])
        print("Segment:", c["segment"])
        print("Niche:", c["niche"])
        print("Strategy:", c["collaboration_type"])
        print("Email:\n", c["email_msg"])