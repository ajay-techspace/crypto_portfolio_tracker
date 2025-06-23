import requests

def fetch_price(coin_id):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
    try:
        response = requests.get(url)
        data = response.json()
        return data[coin_id]['usd']
    except Exception as e:
        print(f"Error fetching price for {coin_id}: {e}")
        return None
