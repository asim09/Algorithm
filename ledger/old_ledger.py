import pandas as pd
import json

# ---------- COMMON HELPERS ----------
def extract_side(dataframe, side, col_crypto, col_qty, col_amount):
    filtered = dataframe[dataframe['Side (Buy/Sell)'].str.lower() == side.lower()]
    return [
        {
            "crypto_pair": row[col_crypto],
            "qty": row[col_qty],
            "net_amount": row[col_amount]
        }
        for _, row in filtered.iterrows()
    ]

def summarize_orders(order_list):
    total_qty = sum(order['qty'] for order in order_list)
    total_amount = sum(order['net_amount'] for order in order_list)
    avg_price = (total_amount / total_qty) if total_qty else 0
    return {
        "total_qty": total_qty,
        "total_amount": total_amount,
        "avg_price": avg_price
    }

def combine_summaries(summary1, summary2):
    """Combine buy/sell summaries from two sources."""
    combined = {}
    for key in ['buy_summary', 'sell_summary']:
        total_qty = summary1[key]['total_qty'] + summary2[key]['total_qty']
        total_amount = summary1[key]['total_amount'] + summary2[key]['total_amount']
        avg_price = (total_amount / total_qty) if total_qty else 0
        combined[key] = {
            "total_qty": total_qty,
            "total_amount": total_amount,
            "avg_price": avg_price
        }
    return combined

# ---------- SPOT ORDERS ----------
file_path = "asimkhan_0808202520091620250808-6-4arwtj.xlsx"
df_spot = pd.read_excel(file_path, sheet_name="Spot Orders", header=8, engine='openpyxl')
df_spot.columns = df_spot.columns.str.strip()

crypto_col_spot = [col for col in df_spot.columns if "Crypto Pair" in col][0]
sol_df_spot = df_spot[df_spot[crypto_col_spot] == 'SOLINR']

spot_result = {
    "buy": extract_side(sol_df_spot, "Buy", "Crypto Pair", "Quantity",
                        "Net Amount Paid/Received by the user(in base currency)"),
    "sell": extract_side(sol_df_spot, "Sell", "Crypto Pair", "Quantity",
                         "Net Amount Paid/Received by the user(in base currency)")
}
spot_summary = {
    "buy_summary": summarize_orders(spot_result["buy"]),
    "sell_summary": summarize_orders(spot_result["sell"])
}

print(json.dumps(spot_summary, indent=4))

# ---------- INSTANT ORDERS ----------
df_instant = pd.read_excel(file_path, sheet_name="Instant Orders", header=8, engine='openpyxl')
df_instant.columns = df_instant.columns.str.strip()

crypto_col_instant = [col for col in df_instant.columns if "Crypto" in col][0]
sol_df_instant = df_instant[df_instant[crypto_col_instant] == 'SOL']

instant_result = {
    "buy": extract_side(sol_df_instant, "Buy", "Crypto", "Quantity",
                        "Net Amount Paid/Received by the user(in INR)"),
    "sell": extract_side(sol_df_instant, "Sell", "Crypto", "Quantity",
                         "Net Amount Paid/Received by the user(in INR)")
}
instant_summary = {
    "buy_summary": summarize_orders(instant_result["buy"]),
    "sell_summary": summarize_orders(instant_result["sell"])
}

print(json.dumps(instant_summary, indent=4))

# ---------- FINAL COMBINED SUMMARY ----------
final_summary = combine_summaries(spot_summary, instant_summary)

print(json.dumps(final_summary, indent=4))

def calculate_profit_loss(summary):
    buy_amount = summary['buy_summary']['total_amount']
    sell_amount = summary['sell_summary']['total_amount']
    profit_loss = sell_amount - buy_amount
    net_qty = summary['sell_summary']['total_qty'] - summary['buy_summary']['total_qty']
    return {
        "profit_loss": profit_loss,
        "net_quantity": net_qty
    }

profit_loss_summary = calculate_profit_loss(final_summary)

print("\nProfit/Loss Summary:")
print(json.dumps(profit_loss_summary, indent=4))
