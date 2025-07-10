import streamlit as st
import pandas as pd
from binance_api import get_ohlc
from scanner import scan_lowcap_coins
from pattern_recognition import get_pattern_signal

st.set_page_config(page_title="🧠 Crypto Pattern Detection Bot", layout="wide")

st.title("🧠 Quantitative Crypto Trading Bot")
st.markdown("Uses advanced math to detect early price movements and low-cap coins with potential.")

# BTC Signal
btc_df = get_ohlc('BTCUSDT')
btc_signal = get_pattern_signal(btc_df['close'].values)

st.subheader("📈 BTC/USDT Signal")
col1, col2, col3 = st.columns(3)
col1.metric("Trend", btc_signal['trend'])
col2.metric("Entropy Level", btc_signal['entropy_level'])
col3.metric("Dominant Frequency", f"{btc_signal['dominant_frequency']:.2f}")

# Low-cap Coin Scanner
st.subheader("🚀 Low-Cap Coin Candidates")
lowcap_coins = scan_lowcap_coins()
if lowcap_coins:
    st.table(pd.DataFrame(lowcap_coins))
else:
    st.info("No low-cap coins found with strong volume spikes yet.")
