def generate_messages(creators, brand_context):
    for c in creators:
        topic = c["content_themes"][0] if c["content_themes"] else "finance"
        video = c["recent_content"]

        c["email_msg"] = f"""
Hi {c['name']},

I recently watched your video titled "{video}" and really liked how you explain {topic} in a simple and practical way.

We are building {brand_context}, focused on helping users improve their saving and investing habits.

We believe a collaboration with you would strongly resonate with your audience and add real value.

Would love to explore this together!

Best,
Team
"""

        c["dm_msg"] = f"""
Hi {c['name']}! Loved your video on "{video}". Would love to collaborate on {topic}-related content.
"""

    return creators