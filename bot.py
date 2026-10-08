
# Gold-Ai-bot
# First version: safe practice mode

def analyze_market(price, previous_price):
    if price > previous_price:
        return "UPTREND"
    elif price < previous_price:
        return "DOWNTREND"
    else:
        return "SIDEWAYS"


def main():
    print("=== Gold-Ai-bot ===")
    print("Practice mode only")

    previous_price = 4000.00
    current_price = 4005.00

    trend = analyze_market(current_price, previous_price)

    print(f"Previous price: {previous_price}")
    print(f"Current price: {current_price}")
    print(f"Market trend: {trend}")
    print("No real trades will be placed.")


if __name__ == "__main__":
    main()
