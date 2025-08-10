from ledger.bak_spot_ledger import summarize_orders as spot_orders_summary
from ledger.bak_instant_ledger import summarize_orders as instant_orders_summary
import json

spot_result = spot_orders_summary()
instant_result = instant_orders_summary()


def combined_summary():

    # Combine buy summary
    combined_buy_qty = spot_result["buy_summary"]["total_buy_qty"] + instant_result["buy_summary"]["total_buy_qty"]
    combined_buy_amount = spot_result["buy_summary"]["total_net_buy_amount"] + instant_result["buy_summary"]["total_net_buy_amount"]

    combined_buy = {
        "total_buy_qty": round(combined_buy_qty, 4),
        "total_net_buy_amount": round(combined_buy_amount, 2),
        "avg_cost": round(combined_buy_amount / combined_buy_qty, 2) if combined_buy_qty else 0
    }

    # Combine sell summary
    combined_sell_qty = spot_result["sell_summary"]["total_sell_qty"] + instant_result["sell_summary"]["total_sell_qty"]
    combined_sell_amount = spot_result["sell_summary"]["total_net_sell_amount"] + instant_result["sell_summary"]["total_net_sell_amount"]

    combined_sell = {
        "total_sell_qty": round(combined_sell_qty, 4),
        "total_net_sell_amount": round(combined_sell_amount, 2),
        "avg_cost": round(combined_sell_amount / combined_sell_qty, 2) if combined_sell_qty else 0
    }

    # Final combined result
    if combined_sell_qty:
        realized_pl_amount = (combined_sell["avg_cost"] - combined_buy["avg_cost"]) * combined_sell_qty
        realized_pl_percent = ((combined_sell["avg_cost"] - combined_buy["avg_cost"]) / combined_buy["avg_cost"]) * 100
    else:
        realized_pl_amount = 0
        realized_pl_percent = 0

    pl_summary = {
        "sold_qty": round(combined_sell_qty, 4),
        "avg_sell_price": combined_sell["avg_cost"],
        "total_sell_amount": round(combined_sell_amount, 2),
        "pl_amount": round(realized_pl_amount, 2),
        "pl_percent": round(realized_pl_percent, 2)
    }

    # Final combined result
    combined_result = {
        "buy_summary": combined_buy,
        "sell_summary": combined_sell,
        "pl_summary": pl_summary
    }
    return combined_result


def get_holdings():
    data = combined_summary()

    buy_qty = data["buy_summary"]["total_buy_qty"]
    buy_avg = data["buy_summary"]["avg_cost"]
    sell_qty = data["sell_summary"]["total_sell_qty"]

    holding_qty = buy_qty - sell_qty
    holding_amount = holding_qty * buy_avg
    holding_avg = buy_avg if holding_qty > 0 else 0

    return {
        "holding_qty": round(holding_qty, 4),
        "holding_amount": round(holding_amount, 2),
        "holding_avg": round(holding_avg, 2)
    }

def calculate_profit_loss():
    combined_result = combined_summary()

    # Extract buy details
    buy_qty = combined_result["buy_summary"]["total_buy_qty"]
    buy_amount = combined_result["buy_summary"]["total_net_buy_amount"]
    buy_avg = combined_result["buy_summary"]["avg_cost"]

    # Extract sell details
    sell_qty = combined_result["sell_summary"]["total_sell_qty"]
    sell_amount = combined_result["sell_summary"]["total_net_sell_amount"]
    sell_avg = combined_result["sell_summary"]["avg_cost"]

    # Calculate holdings
    holding_qty = buy_qty - sell_qty
    holding_amount = holding_qty * buy_avg
    holding_avg = buy_avg if holding_qty > 0 else 0

    # Realized profit/loss (sold quantity)
    realized_pl_amount = sell_amount - (sell_qty * buy_avg)
    realized_pl_percent = (realized_pl_amount / (sell_qty * buy_avg) * 100) if sell_qty > 0 else 0

    # Unrealized profit/loss (current holdings, valued at sell_avg)
    unrealized_pl_amount = (sell_avg - buy_avg) * holding_qty if holding_qty > 0 else 0
    unrealized_pl_percent = (unrealized_pl_amount / holding_amount * 100) if holding_amount > 0 else 0

    # Total profit/loss
    total_pl_amount = realized_pl_amount + unrealized_pl_amount
    total_pl_percent = ((total_pl_amount) / (buy_amount) * 100) if buy_amount > 0 else 0

    return {
        "holding_qty": round(holding_qty, 4),
        "holding_amount": round(holding_amount, 2),
        "holding_avg": round(holding_avg, 2),

        "realized_pl_amount": round(realized_pl_amount, 2),
        "realized_pl_percent": round(realized_pl_percent, 2),

        "unrealized_pl_amount": round(unrealized_pl_amount, 2),
        "unrealized_pl_percent": round(unrealized_pl_percent, 2),

        "total_pl_amount": round(total_pl_amount, 2),
        "total_pl_percent": round(total_pl_percent, 2)
    }
