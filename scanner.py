from binance.client import Client
import pandas as pd

# Replace these with your actual keys in config.py
api_key = 'YOUR_BINANCE_US_API_KEY'
api_secret = 'YOUR_BINANCE_US_SECRET_KEY'

client = Client(api_key, api_secret, tld='us')

def scan_lowcap_coins(min_market_cap=50_000_000):
    candidates = []
    symbols = []

    try:
        exchange_info = client.get_exchange_info()
        symbols = [s['symbol'] for s in exchange_info['symbols'] if 'USDT' in s['symbol']]
    except Exception as e:
        print("Error fetching symbols:", e)
        return []

    for symbol in symbols:
        try:
            ticker = client.get_symbol_ticker(symbol=symbol)
            price = float(ticker['price'])

            stats = client.get_ticker(symbol=symbol)
            volume_change = float(stats['priceChangePercent'])
            volume_24h = float(stats['quoteVolume'])

            market_cap = price * float(stats['weightedAvgPrice'])  # rough estimate

            if market_cap < min_market_cap and abs(volume_change) > 10:
                candidates.append({
                    'symbol': symbol,
                    'price': price,
                    'volume_change': volume_change,
                    'market_cap': market_cap
                })
        except Exception as e:
            continue

    return candidates
