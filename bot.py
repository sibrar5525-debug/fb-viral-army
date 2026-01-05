import requests
import time
import random

# YOUR AD PREVIEW LINK
TARGET_URL = "https://www.facebook.com/61567833521980/posts/122174479976594450/?mibextid=rS40aB7S9Ucbxw6v"

# 1. Distributed Army (Multi-Device User Agents)
USER_AGENTS = [
    "Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; HD1903) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.111 Mobile Safari/537.36"
]

def get_fresh_proxies():
    # Smart Proxy Rotation Logic
    try:
        response = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all")
        return response.text.splitlines()
    except:
        return []

def start_viral_engine():
    proxies = get_fresh_proxies()
    print(f"[*] Engine Initialized. Loaded {len(proxies)} Proxy Nodes.")

    for proxy in proxies:
        try:
            # 2. Human Behavior Bypass (Random Delays)
            wait_time = random.uniform(2, 5) 
            agent = random.choice(USER_AGENTS)
            
            headers = {
                'User-Agent': agent,
                'Referer': 'https://www.google.com/', # Organic Traffic Signal
                'Accept-Language': 'en-US,en;q=0.9'
            }

            proxy_dict = {"http": f"http://{proxy}", "https": f"http://{proxy}"}
            
            # 3. Organic + Technical Combo
            # Step A: Visit Referral Source
            session = requests.Session()
            session.get("https://www.google.com", headers=headers, proxies=proxy_dict, timeout=10)
            
            # Step B: Inject View into Ad Link
            response = session.get(TARGET_URL, headers=headers, proxies=proxy_dict, timeout=15)
            
            if response.status_code == 200:
                print(f"[SUCCESS] View Injected via IP: {proxy} | Device: {agent[:30]}...")
            
            time.sleep(wait_time) # Human-like pause

        except Exception as e:
            continue

if __name__ == "__main__":
    # Multi-Device Power Loop
    while True:
        start_viral_engine()
        print("[*] Cooling down for 60 seconds to avoid detection...")
        time.sleep(60)


