from instagrapi import Client
from config import INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD

def send_dm(username, message):
    cl = Client()
    cl.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)

    user_id = cl.user_id_from_username(username)
    cl.direct_send(message, [user_id])