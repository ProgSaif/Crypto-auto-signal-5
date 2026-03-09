def generate_signal_message(coin, entry, sl, tp1, tp2, tp3, trade_type="LONG", confidence=85):
    return f"""
💹 ${coin} – {trade_type}

Entry: {entry:.8f}
SL: {sl:.8f}
TP1: {tp1:.8f}
TP2: {tp2:.7f}
TP3: {tp3:.6f}

Please like and comment
— Follow for more signal —

Why this setup?
• Confidence: {confidence}%
• Strong trend on 1h tf
• ${coin} is actively traded with sufficient liquidity

DYOR 
#{coin}
"""
