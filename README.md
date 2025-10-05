# 📊 CryptoPriceAlert

A simple Python script that monitors the price of a cryptocurrency using the CoinGecko API and alerts when it crosses your target threshold.

---

## 🚀 Features
- Fetches live crypto prices from CoinGecko API
- Set custom alert price
- Easy to modify for any coin
- Lightweight and fast (no dependencies beyond `requests`)

---

## ⚙️ How to Use
1. Install Python 3.x  
2. Install requests:
   ```bash
   pip install requests
   ```
3. Run the script:
   ```bash
   python main.py
   ```
4. Edit the variables in `main.py` to change:
   - `COIN_ID` → coin you want (e.g., `"ethereum"`, `"solana"`)
   - `TARGET_PRICE` → your alert price
   - `CHECK_INTERVAL` → how often to check (seconds)

---

## 🧠 Example Output
```
🚀 Monitoring BITCOIN price... Target: $70000
Current BITCOIN price: $65900
Current BITCOIN price: $70150
🎉 ALERT: BITCOIN reached $70150!
```

---

## 🧩 API Source
Data provided by [CoinGecko API](https://www.coingecko.com/en/api).

---

## 📜 License
This project is licensed under the MIT License.
