# bot.py
import feedparser
import requests
import re
import os

BOT_TOKEN = os.getenv("8204941014:AAGWCWYqWSUKLYf0Eb1tL0mQX2lXjrYvXzw")
CHAT_ID = os.getenv("@primedayofferss")
AFF_TAG = os.getenv("primedaydisco-21")

# RSS feed -> change if you prefer other feed
RSS_FEED = "https://desidime.com/deals.rss"

def extract_asin(url):
    match = re.search(r'/dp/([A-Z0-9]{10})', url)
    if match:
        return match.group(1)
    match = re.search(r'/gp/product/([A-Z0-9]{10})', url)
    if match:
        return match.group(1)
    return None

def send_message(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": msg,
        "parse_mode": "Markdown",
        "disable_web_page_preview": False
    }
    resp = requests.post(url, data=data)
    # optional: print for logs
    print("sent:", resp.status_code, resp.text)

def main():
    send_message("🔥 GitHub workflow is working bro!")
    
    feed = feedparser.parse(RSS_FEED)
    # iterate first few items to avoid spam
    for entry in feed.entries[:5]:
        title = entry.get('title', 'Deal')
        link = entry.get('link', '')
        asin = extract_asin(link)
        if asin:
            aff_link = f"https://www.amazon.in/dp/{asin}?tag={AFF_TAG}"
        else:
            # fallback: append tag param (may not work for all stores)
            aff_link = link + ("&" if "?" in link else "?") + f"tag={AFF_TAG}"

        msg = f"🔥 *{title}*\n\nBuy Now 👉 {aff_link}\n\n_Hurry — limited stock!_"
        send_message(msg)

if __name__ == "__main__":
    main()
