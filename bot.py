import requests
import time
import random

# NEW TARGET LINK (Updated by Teacher)
TARGET_URL = "https://www.facebook.com/share/r/1BSKW28Fm4/"

USER_AGENTS = [
    "Mozilla/5.0 (Linux; Android 13; SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1"
]

def start_injection():
    try:
        # Proxy Rotation for Viral Loop
        res = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all")
        proxies = res.text.splitlines()
        
        for proxy in proxies[:40]:
            headers = {'User-Agent': random.choice(USER_AGENTS), 'Referer': 'https://www.google.com/'}
            p_dict = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
            try:
                requests.get(TARGET_URL, headers=headers, proxies=p_dict, timeout=10)
                print(f"Target Hit Success: {proxy}")
                time.sleep(random.uniform(2, 4))
            except:
                continue
    except:
        pass

if __name__ == "__main__":
    while True:
        start_injection()
        time.sleep(30)
