import pandas as pd
from binance.client import Client

# Load API keys from config or Streamlit secrets
try:
    from config import BINANCE_API_KEY, BINANCE_API_SECRET
except ImportError:
    import streamlit as st
    BINANCE_API_KEY = st.secrets["BINANCE_API_KEY"]
    BINANCE_API_SECRET = st.secrets["BINANCE_API_SECRET"]

client = Client(api_key=BINANCE_API_KEY, api_secret=BINANCE_API_SECRET, tld='us')

def get_ohlc(symbol, interval='1m', limit=100):
    klines = client.get_klines(symbol=symbol, interval=interval, limit=limit)
    df = pd.DataFrame(klines, columns=[
        'timestamp', 'open', 'high', 'low', 'close', 'volume',
        'close_time', 'quote_asset_volume', 'number_of_trades',
        'taker_buy_base_volume', 'taker_buy_quote_volume', 'ignore'
    ])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)
    numeric_cols = ['open', 'high', 'low', 'close', 'volume']
    df[numeric_cols] = df[numeric_cols].astype(float)
    return df

def get_all_symbols():
    exchange_info = client.get_exchange_info()
    symbols = [s['symbol'] for s in exchange_info['symbols'] if 'USDT' in s['symbol']]
    return symbols
