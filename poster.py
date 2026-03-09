def generate_signal_message(coin, entry, sl, tp1, tp2, tp3, trade_type="LONG", confidence=85):
    return f"""
💹 ${coin} – {trade_type}

Entry: {entry:.8f}
SL: {sl:.8f}
TP1: {tp1:.8f}
TP2: {tp2:.7f}
TP3: {tp3:.6f}

Please like and comment your PNL
— Follow for more signal —

Why this setup?
• Confidence: {confidence}%
• Strong trend on 5m chart

DYOR 
#{coin}
"""
