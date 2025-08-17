def calculate_profit(buy_price, sell_price, quantity):
    """
    Calculate profit and profit percentage based on:
    - 0.5% fee + 18% GST on buy and sell side
    """
    fee_percent = 0.17 / 100
    gst_percent = 18 / 100

    # Buy side
    total_buy = buy_price * quantity
    buy_fee = total_buy * fee_percent
    buy_gst = buy_fee * gst_percent
    total_buy_cost = total_buy + buy_fee + buy_gst

    # Sell side
    total_sell = sell_price * quantity
    sell_fee = total_sell * fee_percent
    sell_gst = sell_fee * gst_percent
    net_sell_amount = total_sell - sell_fee - sell_gst

    # Profit calculation
    profit = net_sell_amount - total_buy_cost
    profit_percent = (profit / total_buy_cost) * 100 if total_buy_cost != 0 else 0

    # Results
    print("\n--- Trade Summary ---")
    print(f"Buy Price per Coin (₹): {buy_price}")
    print(f"Sell Price per Coin (₹): {sell_price}")
    print(f"Quantity: {round(quantity, 6)}")
    print(f"Total Buy Cost (₹): {round(total_buy_cost, 2)}")
    print(f"Net Sell Amount (₹): {round(net_sell_amount, 2)}")
    print(f"💹 Profit (₹): {round(profit, 2)}")
    print(f"Profit Percentage: {round(profit_percent, 2)} %")

    # Fee & Tax Breakdown
    print("\n--- Fee & Tax Breakdown ---")
    print(f"Buy Fee (0.17% of Buy): ₹{round(buy_fee, 2)}")
    print(f"Buy GST (18% of Buy Fee): ₹{round(buy_gst, 2)}")
    print(f"Sell Fee (0.17% of Sell): ₹{round(sell_fee, 2)}")
    print(f"Sell GST (18% of Sell Fee): ₹{round(sell_gst, 2)}")


if __name__ == "__main__":
    while True:
        try:
            print("\n===============================")
            print("💹 Crypto Trade Profit Calculator")
            print("===============================\n")

            buy_input = input("Enter Buy Price per Coin (₹): ").strip()
            if buy_input.lower() in ["q", "exit"]:
                break
            buy_price = float(buy_input)

            sell_input = input("Enter Sell Price per Coin (₹): ").strip()
            if sell_input.lower() in ["q", "exit"]:
                break
            sell_price = float(sell_input)

            total_amount_input = input(
                "Optional - Enter Total Buy Amount (₹), or leave blank to enter quantity: "
            ).strip()
            if total_amount_input.lower() in ["q", "exit"]:
                break

            if total_amount_input:
                total_amount = float(total_amount_input)
                quantity = total_amount / buy_price
                print(
                    f"✅ Coins Purchased: {round(quantity, 6)} for ₹{round(total_amount, 2)}"
                )
            else:
                quantity_input = input("Enter Quantity of Coins: ").strip()
                if quantity_input.lower() in ["q", "exit"]:
                    break
                quantity = float(quantity_input)

            calculate_profit(buy_price, sell_price, quantity)

        except ValueError:
            print("❌ Please enter valid numeric inputs.")
