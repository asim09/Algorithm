from spot_ledger import summarize_all_coins as spot_orders_summary
from instant_ledger import summarize_all_coins as instant_orders_summary
import json

# Assuming spot_ledger.py and instant_ledger.py internally load their own dataframes

spot_result = spot_orders_summary()      # Dict[str, dict]
instant_result = instant_orders_summary()  # Dict[str, dict]

def combined_summary():
    all_coins = set(spot_result.keys()) | set(instant_result.keys())
    
    # Helper to normalize coin names (remove trailing 'INR')
    def normalize_coin_name(coin):
        if coin.endswith("INR"):
            return coin[:-3]
        return coin

    # Aggregate data by normalized coin name
    aggregated = {}

    for coin in all_coins:
        norm_coin = normalize_coin_name(coin)

        spot_data = spot_result.get(coin, {
            "buy_summary": {"total_buy_qty": 0, "total_net_buy_amount": 0, "buy_trades_count": 0},
            "sell_summary": {"total_sell_qty": 0, "total_net_sell_amount": 0, "sell_trades_count": 0}
        })
        instant_data = instant_result.get(coin, {
            "buy_summary": {"total_buy_qty": 0, "total_net_buy_amount": 0, "buy_trades_count": 0},
            "sell_summary": {"total_sell_qty": 0, "total_net_sell_amount": 0, "sell_trades_count": 0}
        })

        combined_buy_qty = spot_data["buy_summary"]["total_buy_qty"] + instant_data["buy_summary"]["total_buy_qty"]
        combined_buy_amount = spot_data["buy_summary"]["total_net_buy_amount"] + instant_data["buy_summary"]["total_net_buy_amount"]
        combined_buy_trades = spot_data["buy_summary"].get("buy_trades_count", 0) + instant_data["buy_summary"].get("buy_trades_count", 0)

        combined_sell_qty = spot_data["sell_summary"]["total_sell_qty"] + instant_data["sell_summary"]["total_sell_qty"]
        combined_sell_amount = spot_data["sell_summary"]["total_net_sell_amount"] + instant_data["sell_summary"]["total_net_sell_amount"]
        combined_sell_trades = spot_data["sell_summary"].get("sell_trades_count", 0) + instant_data["sell_summary"].get("sell_trades_count", 0)

        if norm_coin not in aggregated:
            aggregated[norm_coin] = {
                "buy_summary": {
                    "total_buy_qty": combined_buy_qty,
                    "total_net_buy_amount": combined_buy_amount,
                    "buy_trades_count": combined_buy_trades
                },
                "sell_summary": {
                    "total_sell_qty": combined_sell_qty,
                    "total_net_sell_amount": combined_sell_amount,
                    "sell_trades_count": combined_sell_trades
                }
            }
        else:
            # Add to existing aggregated coin
            agg = aggregated[norm_coin]
            agg["buy_summary"]["total_buy_qty"] += combined_buy_qty
            agg["buy_summary"]["total_net_buy_amount"] += combined_buy_amount
            agg["buy_summary"]["buy_trades_count"] += combined_buy_trades

            agg["sell_summary"]["total_sell_qty"] += combined_sell_qty
            agg["sell_summary"]["total_net_sell_amount"] += combined_sell_amount
            agg["sell_summary"]["sell_trades_count"] += combined_sell_trades

    # Now compute avg_cost, net_position_qty, total_traded_value per aggregated coin
    combined = {}
    for coin, data in aggregated.items():
        buy_qty = data["buy_summary"]["total_buy_qty"]
        buy_amount = data["buy_summary"]["total_net_buy_amount"]
        buy_trades = data["buy_summary"]["buy_trades_count"]

        sell_qty = data["sell_summary"]["total_sell_qty"]
        sell_amount = data["sell_summary"]["total_net_sell_amount"]
        sell_trades = data["sell_summary"]["sell_trades_count"]

        avg_buy_cost = buy_amount / buy_qty if buy_qty else 0
        avg_sell_cost = sell_amount / sell_qty if sell_qty else 0
        net_position_qty = buy_qty - sell_qty
        total_traded_value = buy_amount + sell_amount

        combined[coin] = {
            "buy_summary": {
                "total_buy_qty": buy_qty,
                "total_net_buy_amount": buy_amount,
                "avg_cost": avg_buy_cost,
                "buy_trades_count": buy_trades
            },
            "sell_summary": {
                "total_sell_qty": sell_qty,
                "total_net_sell_amount": sell_amount,
                "avg_cost": avg_sell_cost,
                "sell_trades_count": sell_trades
            },
            "net_position_qty": net_position_qty,
            "total_traded_value": total_traded_value
        }

    # Aggregate totals over all normalized coins
    total_buy_qty = sum(c["buy_summary"]["total_buy_qty"] for c in combined.values())
    total_buy_amount = sum(c["buy_summary"]["total_net_buy_amount"] for c in combined.values())
    total_sell_qty = sum(c["sell_summary"]["total_sell_qty"] for c in combined.values())
    total_sell_amount = sum(c["sell_summary"]["total_net_sell_amount"] for c in combined.values())

    avg_buy_cost = total_buy_amount / total_buy_qty if total_buy_qty else 0
    avg_sell_cost = total_sell_amount / total_sell_qty if total_sell_qty else 0

    if total_sell_qty:
        realized_pl_amount = (avg_sell_cost - avg_buy_cost) * total_sell_qty
        realized_pl_percent = ((avg_sell_cost - avg_buy_cost) / avg_buy_cost) * 100 if avg_buy_cost else 0
    else:
        realized_pl_amount = 0
        realized_pl_percent = 0

    pl_summary = {
        "sold_qty": round(total_sell_qty, 4),
        "avg_sell_price": round(avg_sell_cost, 2),
        "total_sell_amount": round(total_sell_amount, 2),
        "pl_amount": round(realized_pl_amount, 2),
        "pl_percent": round(realized_pl_percent, 2)
    }

    combined_summary_result = {
        "buy_summary": {
            "total_buy_qty": round(total_buy_qty, 4),
            "total_net_buy_amount": round(total_buy_amount, 2),
            "avg_cost": round(avg_buy_cost, 2)
        },
        "sell_summary": {
            "total_sell_qty": round(total_sell_qty, 4),
            "total_net_sell_amount": round(total_sell_amount, 2),
            "avg_cost": round(avg_sell_cost, 2)
        },
        "pl_summary": pl_summary,
        "coins": combined
    }

    return combined_summary_result


def get_holdings():
    combined_data = combined_summary()
    data = combined_data["buy_summary"]
    sell_data = combined_data["sell_summary"]

    buy_qty = data["total_buy_qty"]
    buy_avg = data["avg_cost"]
    sell_qty = sell_data["total_sell_qty"]

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

    buy_qty = combined_result["buy_summary"]["total_buy_qty"]
    buy_amount = combined_result["buy_summary"]["total_net_buy_amount"]
    buy_avg = combined_result["buy_summary"]["avg_cost"]

    sell_qty = combined_result["sell_summary"]["total_sell_qty"]
    sell_amount = combined_result["sell_summary"]["total_net_sell_amount"]
    sell_avg = combined_result["sell_summary"]["avg_cost"]

    holding_qty = buy_qty - sell_qty
    holding_amount = holding_qty * buy_avg
    holding_avg = buy_avg if holding_qty > 0 else 0

    realized_pl_amount = sell_amount - (sell_qty * buy_avg)
    realized_pl_percent = (realized_pl_amount / (sell_qty * buy_avg) * 100) if sell_qty > 0 else 0

    unrealized_pl_amount = (sell_avg - buy_avg) * holding_qty if holding_qty > 0 else 0
    unrealized_pl_percent = (unrealized_pl_amount / holding_amount * 100) if holding_amount > 0 else 0

    total_pl_amount = realized_pl_amount + unrealized_pl_amount
    total_pl_percent = (total_pl_amount / buy_amount * 100) if buy_amount > 0 else 0

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


def per_coin_summary():
    combined_data = combined_summary()
    coins_data = combined_data.get("coins", {})

    per_coin_results = {}

    for coin, data in coins_data.items():
        buy = data["buy_summary"]
        sell = data["sell_summary"]

        buy_qty = buy.get("total_buy_qty", 0)
        buy_amount = buy.get("total_net_buy_amount", 0)
        buy_avg = buy.get("avg_cost", 0)

        sell_qty = sell.get("total_sell_qty", 0)
        sell_amount = sell.get("total_net_sell_amount", 0)
        sell_avg = sell.get("avg_cost", 0)

        holding_qty = buy_qty - sell_qty
        holding_amount = holding_qty * buy_avg
        holding_avg = buy_avg if holding_qty > 0 else 0

        realized_pl_amount = sell_amount - (sell_qty * buy_avg)
        realized_pl_percent = (realized_pl_amount / (sell_qty * buy_avg) * 100) if sell_qty > 0 else 0

        unrealized_pl_amount = (sell_avg - buy_avg) * holding_qty if holding_qty > 0 else 0
        unrealized_pl_percent = (unrealized_pl_amount / holding_amount * 100) if holding_amount > 0 else 0

        total_pl_amount = realized_pl_amount + unrealized_pl_amount
        total_pl_percent = (total_pl_amount / buy_amount * 100) if buy_amount > 0 else 0

        per_coin_results[coin] = {
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

    return per_coin_results

