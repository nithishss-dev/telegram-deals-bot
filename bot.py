import os
import requests
import feedparser

BOT_TOKEN = os.getenv("8204941014:AAGWCWYqWSUKLYf0Eb1tL0mQX2lXjrYvXzw")
CHAT_ID = os.getenv("@primedayofferss")
AFF_TAG = os.getenv("primedaydisco-21")

# RSS feed (example)
RSS_FEED = "https://www.coupondunia.in/rss/amazon-in"

# Send Telegram message
def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    }
    response = requests.post(url, data=data)
    print("Telegram Response:", response.text)  # DEBUG
    return response

def main():
    # TEST MESSAGE
    send_message("🔥 GitHub workflow is working bro!")

    # Fetch RSS deals
    feed = feedparser.parse(RSS_FEED)

    for entry in feed.entries[:3]:  # send first 3 deals
        title = entry.title
        link = entry.link

        # Add affiliate tag
        if "amazon" in link:
            if "?" in link:
                link += f"&tag={AFF_TAG}"
            else:
                link += f"?tag={AFF_TAG}"

        text = f"🔥 <b>{title}</b>\n\n👉 {link}"
        send_message(text)

if __name__ == "__main__":
    main()

