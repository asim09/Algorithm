from combined_summary import combined_summary, get_holdings, calculate_profit_loss
import json

print(json.dumps(combined_summary(), indent=4))
print("===========================")
print(json.dumps(get_holdings(), indent=4))
print("===========================")
print(json.dumps(calculate_profit_loss(), indent=4))
