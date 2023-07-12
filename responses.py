def handle_response(message) -> str:
    lc_message = message.lower()

    if "twitter.com/" in lc_message:
        return "get threads!"
