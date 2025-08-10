from ledger.bak_combined_summary import combined_summary, get_holdings, calculate_profit_loss
import json

# print(json.dumps(combined_summary(), indent=4))
# print("===========================")
# print(json.dumps(get_holdings(), indent=4))
# print("===========================")
# print(json.dumps(calculate_profit_loss(), indent=4))

# save this as app.py
# app.py
# app.py
# app.py
import streamlit as st
from streamlit_autorefresh import st_autorefresh
import plotly.express as px
import pandas as pd

from ledger.bak_combined_summary import combined_summary, get_holdings, calculate_profit_loss

# Page setup
st.set_page_config(page_title="Ledger Dashboard", layout="wide")
st.title("📊 Ledger Dashboard (Live)")

# Auto-refresh every X seconds (5000 ms = 5 seconds)
refresh_rate = 5
st_autorefresh(interval=refresh_rate * 1000, key="ledgerrefresh")
st.caption(f"Auto-refreshing every {refresh_rate} seconds")

# Get latest data
summary = combined_summary()
holdings = get_holdings()
pl_data = calculate_profit_loss()

# -------- BUY/SELL/P&L Summary Chart --------
buy_amount = summary["buy_summary"]["total_net_buy_amount"]
sell_amount = summary["sell_summary"]["total_net_sell_amount"]
pl_amount = summary["pl_summary"]["pl_amount"]

df_amounts = pd.DataFrame({
    "Category": ["Buy Amount", "Sell Amount", "P/L Amount"],
    "Value": [buy_amount, sell_amount, pl_amount]
})

fig_amounts = px.bar(
    df_amounts,
    x="Category",
    y="Value",
    color="Category",
    text="Value",
    title="Buy vs Sell vs P/L Amounts"
)
fig_amounts.update_traces(texttemplate='%{text:,.2f}', textposition='outside')

# -------- HOLDINGS TABLE --------
if isinstance(holdings, dict):
    # If dict is coin → quantity
    if all(isinstance(v, (int, float, str)) for v in holdings.values()):
        df_holdings = pd.DataFrame(list(holdings.items()), columns=["Coin", "Quantity"])
    else:
        df_holdings = pd.DataFrame([holdings])
elif isinstance(holdings, list):
    df_holdings = pd.DataFrame(holdings)
else:
    df_holdings = pd.DataFrame()

# -------- Layout --------
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Amounts Summary")
    st.plotly_chart(fig_amounts, use_container_width=True)

with col2:
    st.subheader("Holdings")
    if not df_holdings.empty:
        st.dataframe(df_holdings, use_container_width=True)
    else:
        st.write("No holdings data available")

# -------- P/L Summary --------
st.subheader("Profit/Loss Summary")
st.json(pl_data)

