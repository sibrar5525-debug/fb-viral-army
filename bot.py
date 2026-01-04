import requests
import time
import random

# Aapki Medicine Wali Video ka ID
VIDEO_URL = "https://m.facebook.com/1327170131980838"

def get_proxies():
    # 1. Distributed Army: Free and Fast Proxies
    try:
        r = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all")
        if r.status_code == 200:
            return r.text.splitlines()
    except:
        return []

def start_viral_loop():
    print("--- CLOUD MISSION STARTED ---")
    proxies = get_proxies()
    
    # 2. Human Behavior Bypass & Organic Combo
    for ip in proxies[:100]: # Batch of 100 per run
        try:
            proxy_dict = {"http": f"http://{ip}", "https": f"http://{ip}"}
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Referer': 'https://www.google.com.pk/'
            }
            
            # Request sending
            s = requests.Session()
            s.get(VIDEO_URL, headers=headers, proxies=proxy_dict, timeout=12)
            
            # 3. Viral Loop: Random Watch Time
            watch = random.randint(35, 70)
            print(f"Target Hit: {ip} | Watching: {watch}s")
            time.sleep(watch)
            
        except:
            continue

if __name__ == "__main__":
    start_viral_loop()
