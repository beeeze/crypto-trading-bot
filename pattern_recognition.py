import numpy as np
from scipy.stats import entropy

def detect_fft_pattern(prices):
    fft_result = np.fft.fft(prices)
    freq = np.fft.fftfreq(len(prices))
    dominant_freq = freq[np.argmax(np.abs(fft_result[1:len(freq)//2]))]
    return dominant_freq

def calculate_entropy(prices):
    returns = np.diff(prices)
    hist, _ = np.histogram(returns, bins=10, density=True)
    return entropy(hist)

def detect_trend(prices):
    return "Up" if prices[-1] > prices[0] else "Down"

def get_pattern_signal(prices):
    ent = calculate_entropy(prices)
    trend = detect_trend(prices)
    dom_freq = detect_fft_pattern(prices)

    return {
        "dominant_frequency": dom_freq,
        "entropy": ent,
        "entropy_level": "Low" if ent < 1.5 else "High",
        "trend": trend
    }
