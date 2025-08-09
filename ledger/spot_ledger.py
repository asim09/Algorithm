import pandas as pd
import json

file_path = "asimkhan_0808202520091620250808-6-4arwtj.xlsx"
df_spot = pd.read_excel(file_path, sheet_name="Spot Orders", header=8, engine='openpyxl')
df_spot.columns = df_spot.columns.str.strip()
crypto_col_spot = [col for col in df_spot.columns if "Crypto Pair" in col][0]


sol_df_spot = df_spot[df_spot[crypto_col_spot] == 'SOLINR']
def extract_side(dataframe, side, col_crypto, col_qty, col_amount, col_date):
    filtered = dataframe[dataframe['Side (Buy/Sell)'].str.lower() == side.lower()]\
        .sort_values(by=col_date, ascending=True)
    return [
        {
            "crypto_pair": row[col_crypto],
            "qty": row[col_qty],
            "total_price": row[col_amount],
            "col_date": row[col_date]if pd.isna(row[col_date]) else row[col_date].strftime("%Y-%m-%d %H:%M:%S")
        }
        for _, row in filtered.iterrows()
    ]

def summarize_orders():

    spot_result = {
        "buy": extract_side(sol_df_spot, "Buy", "Crypto Pair", "Quantity",
                            "Net Amount Paid/Received by the user(in base currency)",
                            "Trade Completion time"),
        "sell": extract_side(sol_df_spot, "Sell", "Crypto Pair", "Quantity",
                            "Net Amount Paid/Received by the user(in base currency)",
                            "Trade Completion time")
    }


    total_buy_qty = sum(item["qty"] for item in spot_result['buy'])
    total_net_buy_amount = sum(item["total_price"] for item in spot_result['buy'])
    avg_cost = total_net_buy_amount / total_buy_qty
    result = {
        "buy_summary": {
        "total_buy_qty": total_buy_qty,
        "total_net_buy_amount": total_net_buy_amount,
        "avg_cost": avg_cost
    },
    "sell_summary": { 
        "total_sell_qty": sum(item["qty"] for item in spot_result['sell']),
        "total_net_sell_amount": sum(item["total_price"] for item in spot_result['sell']),
        "avg_cost": sum(item["total_price"] for item in spot_result['sell']) / sum(item["qty"] for item in spot_result['sell'])
    }
    }
    return result


# print(result)

# print(json.dumps(summarize_orders(), indent=4))
# print(json.dumps(result, indent=4))