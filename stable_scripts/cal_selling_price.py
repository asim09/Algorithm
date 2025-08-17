def required_sell_price_for_target_profit(buy_price, quantity, target_profit):
    """
    Calculate the required sell price per coin to earn a desired profit (₹), after:
    - 0.17% fee on buy/sell
    - 18% GST on fees
    """

    fee_percent = 0.17 / 100
    gst_percent = 18 / 100

    # --- Buy Side ---
    total_buy = buy_price * quantity
    buy_fee = total_buy * fee_percent
    buy_gst = buy_fee * gst_percent
    total_buy_cost = total_buy + buy_fee + buy_gst

    # --- Required Net Sell Amount to Achieve Target Profit ---
    required_net_sell = total_buy_cost + target_profit

    # Reverse calculate sell price from required net sell amount
    # net_sell = (sell_price * quantity) - sell_fee - sell_gst
    # net_sell = (sell_price * quantity) - (sell_price * quantity * fee%) - (sell_price * quantity * fee% * gst%)

    # So:
    # net_sell = (sell_price * quantity) * (1 - fee% - fee%*gst%)
    effective_multiplier = 1 - fee_percent * (1 + gst_percent)
    required_total_sell = required_net_sell / effective_multiplier
    required_sell_price = required_total_sell / quantity

    # --- Fee Breakdown for Verification ---
    sell_fee = required_sell_price * quantity * fee_percent
    sell_gst = sell_fee * gst_percent
    net_sell = required_sell_price * quantity - sell_fee - sell_gst
    actual_profit = net_sell - total_buy_cost

    # Output
    print("\n--- Reverse Profit Calculator ---")
    print(f"Buy Price per Coin (₹): {buy_price}")
    print(f"Quantity: {round(quantity, 6)}")
    print(f"Total Buy Cost (₹): {round(total_buy_cost, 2)}")
    print(f"Target Profit (₹): {round(target_profit, 2)}")
    print(f"✅ Required Sell Price per Coin: ₹{round(required_sell_price, 2)}")

    print("\n--- Verification ---")
    print(f"Estimated Net Sell Amount: ₹{round(net_sell, 2)}")
    print(f"Actual Profit (₹): {round(actual_profit, 2)}")

    print("\n--- Fee Breakdown ---")
    print(f"Buy Fee + GST: ₹{round(buy_fee + buy_gst, 2)}")
    print(f"Sell Fee + GST: ₹{round(sell_fee + sell_gst, 2)}")


if __name__ == "__main__":
    while True:
        try:
            print("\n===============================")
            print("💹 Required Sell Price Calculator")
            print("===============================\n")

            buy_input = input("Enter Buy Price per Coin (₹): ").strip()
            if buy_input.lower() in ["q", "exit"]:
                break
            buy_price = float(buy_input)

            qty_input = input("Enter Quantity of Coins: ").strip()
            if qty_input.lower() in ["q", "exit"]:
                break
            quantity = float(qty_input)

            profit_input = input("Enter Desired Profit (₹): ").strip()
            if profit_input.lower() in ["q", "exit"]:
                break
            target_profit = float(profit_input)

            required_sell_price_for_target_profit(buy_price, quantity, target_profit)

        except ValueError:
            print("❌ Please enter valid numeric inputs.")
