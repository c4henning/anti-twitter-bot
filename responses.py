# the only response listens for twitter links
import os
from dotenv import load_dotenv


def handle_response(user_message) -> str:
    lc_message = user_message.lower()

    load_dotenv()
    MY_USER_ID = os.getenv('MY_USER_ID')

    if "twitter.com/" in lc_message:
        return f"<@{MY_USER_ID}> wanted me to tell you he hates these twitter links. Get threads:\n" \
               "https://apps.apple.com/us/app/instagram/id6446901002\n" \
               "https://play.google.com/store/apps/details?id=com.instagram.barcelona&pli=1"
