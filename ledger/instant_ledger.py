import pandas as pd
import json

file_path = "asimkhan_0808202520091620250808-6-4arwtj.xlsx"
df_instant = pd.read_excel(file_path, sheet_name="Instant Orders", header=8, engine='openpyxl')
df_instant.columns = df_instant.columns.str.strip()

crypto_col_instant = [col for col in df_instant.columns if "Crypto" in col][0]

def extract_side(dataframe, side, col_crypto, col_qty, col_amount, col_date):
    filtered = dataframe[dataframe['Side (Buy/Sell)'].str.lower() == side.lower()]\
        .sort_values(by=col_date, ascending=True)
    return [
        {
            "crypto_pair": row[col_crypto],
            "qty": row[col_qty],
            "total_price": row[col_amount],
            "col_date": row[col_date] if pd.isna(row[col_date]) else row[col_date].strftime("%Y-%m-%d %H:%M:%S")
        }
        for _, row in filtered.iterrows()
    ]

def summarize_orders_for_coin(coin, price_lookup=None):
    coin_df = df_instant[df_instant[crypto_col_instant] == coin]

    buy_trades = extract_side(coin_df, "Buy", crypto_col_instant, "Quantity",
                              "Net Amount Paid/Received by the user(in INR)",
                              "Trade Completion time")
    sell_trades = extract_side(coin_df, "Sell", crypto_col_instant, "Quantity",
                               "Net Amount Paid/Received by the user(in INR)",
                               "Trade Completion time")

    total_buy_qty = sum(item["qty"] for item in buy_trades)
    total_net_buy_amount = sum(item["total_price"] for item in buy_trades)
    avg_cost_buy = total_net_buy_amount / total_buy_qty if total_buy_qty else 0

    total_sell_qty = sum(item["qty"] for item in sell_trades)
    total_net_sell_amount = sum(item["total_price"] for item in sell_trades)
    avg_cost_sell = total_net_sell_amount / total_sell_qty if total_sell_qty else 0

    net_qty = total_buy_qty - total_sell_qty
    total_traded_value = total_net_buy_amount + total_net_sell_amount

    last_trade_date = None
    if not coin_df.empty:
        dates = coin_df["Trade Completion time"].dropna()
        if not dates.empty:
            last_trade_date = dates.max().strftime("%Y-%m-%d %H:%M:%S")

    # Unrealized P/L calculation if current price provided
    unrealized_pl = None
    unrealized_pl_percent = None
    if price_lookup and coin in price_lookup and net_qty != 0:
        current_price = price_lookup[coin]
        unrealized_pl = (current_price - avg_cost_buy) * net_qty
        unrealized_pl_percent = ((current_price - avg_cost_buy) / avg_cost_buy) * 100 if avg_cost_buy else None

    return {
        "coin": coin,
        "buy_summary": {
            "total_buy_qty": total_buy_qty,
            "total_net_buy_amount": total_net_buy_amount,
            "avg_cost": avg_cost_buy,
            "buy_trades_count": len(buy_trades),
        },
        "sell_summary": {
            "total_sell_qty": total_sell_qty,
            "total_net_sell_amount": total_net_sell_amount,
            "avg_cost": avg_cost_sell,
            "sell_trades_count": len(sell_trades),
        },
        "net_position_qty": net_qty,
        "total_traded_value": total_traded_value,
        "last_trade_date": last_trade_date,
        "unrealized_pl": unrealized_pl,
        "unrealized_pl_percent": unrealized_pl_percent
    }

def summarize_all_coins(price_lookup=None):
    coins = df_instant[crypto_col_instant].dropna().unique()
    all_summary = {}
    for coin in coins:
        all_summary[coin] = summarize_orders_for_coin(coin, price_lookup=price_lookup)
    return all_summary


# print(json.dumps(summarize_all_coins(), indent=4))



