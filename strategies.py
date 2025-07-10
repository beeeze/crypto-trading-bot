from pattern_recognition import get_pattern_signal

def evaluate_coin(prices):
    signal = get_pattern_signal(prices)
    if signal['trend'] == 'Up' and signal['entropy_level'] == 'Low':
        return "Strong Buy"
    elif signal['trend'] == 'Down' and signal['entropy_level'] == 'Low':
        return "Strong Sell"
    else:
        return "Hold"
