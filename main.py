import requests
import time

# === CONFIGURATION ===
COIN_ID = "bitcoin"      # CoinGecko coin ID (example: bitcoin, ethereum)
TARGET_PRICE = 70000     # Set alert threshold in USD
CHECK_INTERVAL = 30      # Seconds between checks

def get_price(coin_id):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data[coin_id]["usd"]

def main():
    print(f"🚀 Monitoring {COIN_ID.upper()} price... Target: ${TARGET_PRICE}")
    while True:
        try:
            price = get_price(COIN_ID)
            print(f"Current {COIN_ID.upper()} price: ${price}")
            
            if price >= TARGET_PRICE:
                print(f"🎉 ALERT: {COIN_ID.upper()} reached ${price}!")
                break
            
            time.sleep(CHECK_INTERVAL)
        except Exception as e:
            print("Error:", e)
            time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
