import streamlit as st
import pandas as pd
from combined_summary import combined_summary, get_holdings, calculate_profit_loss

# Page setup
st.set_page_config(page_title="Ledger Dashboard", layout="wide")
st.title("📊 Ledger Dashboard")

# Refresh rate and auto-refresh
refresh_rate = 5
st.caption(f"Auto-refreshing every {refresh_rate} seconds")

# Merge coins that have INR variants (from your existing function)
# def merge_similar_coins(coins):
#     merged = {}
#     processed = set()

#     for coin in coins:
#         if coin in processed:
#             continue

#         if coin.endswith("INR"):
#             base_coin = coin[:-3]
#             if base_coin in coins:
#                 c1 = coins[base_coin]
#                 c2 = coins[coin]
#                 merged_buy_qty = c1["buy_summary"]["total_buy_qty"] + c2["buy_summary"]["total_buy_qty"]
#                 merged_buy_amt = c1["buy_summary"]["total_net_buy_amount"] + c2["buy_summary"]["total_net_buy_amount"]
#                 merged_buy_trades = c1["buy_summary"].get("buy_trades_count", 0) + c2["buy_summary"].get("buy_trades_count", 0)
#                 merged_sell_qty = c1["sell_summary"]["total_sell_qty"] + c2["sell_summary"]["total_sell_qty"]
#                 merged_sell_amt = c1["sell_summary"]["total_net_sell_amount"] + c2["sell_summary"]["total_net_sell_amount"]
#                 merged_sell_trades = c1["sell_summary"].get("sell_trades_count", 0) + c2["sell_summary"].get("sell_trades_count", 0)

#                 merged[base_coin] = {
#                     "buy_summary": {
#                         "total_buy_qty": merged_buy_qty,
#                         "total_net_buy_amount": merged_buy_amt,
#                         "avg_cost": merged_buy_amt / merged_buy_qty if merged_buy_qty else 0,
#                         "buy_trades_count": merged_buy_trades,
#                     },
#                     "sell_summary": {
#                         "total_sell_qty": merged_sell_qty,
#                         "total_net_sell_amount": merged_sell_amt,
#                         "avg_cost": merged_sell_amt / merged_sell_qty if merged_sell_qty else 0,
#                         "sell_trades_count": merged_sell_trades,
#                     },
#                     "net_position_qty": merged_buy_qty - merged_sell_qty,
#                     "total_traded_value": merged_buy_amt + merged_sell_amt
#                 }
#                 processed.add(base_coin)
#                 processed.add(coin)
#             else:
#                 merged[coin] = coins[coin]
#                 processed.add(coin)
#         else:
#             if coin not in processed:
#                 if coin + "INR" not in coins:
#                     merged[coin] = coins[coin]
#                     processed.add(coin)

#     return merged

# Fetch data
summary = combined_summary()
holdings = get_holdings()
pl_data = calculate_profit_loss()

# Merge coins with INR variants
merged_coins = merge_similar_coins(summary["coins"])

# Prepare DataFrame for coins
coins_df = pd.DataFrame.from_dict(merged_coins, orient='index')

def expand_summary(df, col_prefix):
    df_expanded = pd.json_normalize(df[f"{col_prefix}_summary"].tolist())
    df_expanded.index = df.index
    df_expanded.columns = [f"{col_prefix}_{col}" for col in df_expanded.columns]
    return df_expanded

buy_df = expand_summary(coins_df, "buy")
sell_df = expand_summary(coins_df, "sell")


coins_df = pd.concat([coins_df.drop(columns=["buy_summary", "sell_summary"]), buy_df, sell_df], axis=1)

# Replace NaNs with 0 for numeric columns (safe calculation)
coins_df.fillna(0, inplace=True)

# Calculate Realized and Unrealized Profit/Loss
ledger_rows = []
for coin, row in coins_df.iterrows():
    buy_qty = row["buy_total_buy_qty"]
    avg_buy_price = row["buy_avg_cost"]
    sold_qty = row["sell_total_sell_qty"]
    avg_sell_price = row["sell_avg_cost"]
    holding_qty = row["net_position_qty"]

    realized_profit = sold_qty * (avg_sell_price - avg_buy_price)
    # For unrealized profit, use sell avg price as current price; fallback to buy avg price if 0
    current_price = avg_sell_price if avg_sell_price > 0 else avg_buy_price
    unrealized_profit = holding_qty * (current_price - avg_buy_price)

    ledger_rows.append({
        "Coin": coin,
        "Invested Amount": buy_qty * avg_buy_price,
        "Buy Quantity": buy_qty,
        "Avg Buy Price": avg_buy_price,
        "Sold Quantity": sold_qty,
        "Avg Sell Price": avg_sell_price,
        "Realized Profit (P/L)": realized_profit,
        "Unrealized Profit (P/L on holdings)": unrealized_profit,
        "Holding Quantity": holding_qty,
    })
    

ledger_df = pd.DataFrame(ledger_rows).set_index("Coin")

# Format ledger for better readability
formatted_ledger_df = ledger_df.style.format({
    "Invested Amount": "₹{:,.2f}",
    "Buy Quantity": "{:,.4f}",
    "Avg Buy Price": "₹{:,.2f}",
    "Sold Quantity": "{:,.4f}",
    "Avg Sell Price": "₹{:,.2f}",
    "Realized Profit (P/L)": "₹{:,.2f}",
    "Unrealized Profit (P/L on holdings)": "₹{:,.2f}",
    "Holding Quantity": "{:,.4f}"
})

# Show ledger table
st.subheader("Ledger Table: Coin-wise Trading Summary")
st.dataframe(formatted_ledger_df, use_container_width=True)
