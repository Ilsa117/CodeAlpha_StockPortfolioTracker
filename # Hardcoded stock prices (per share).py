# Hardcoded stock prices (per share)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 125
}

print("=== STOCK PORTFOLIO TRACKER ===")
print("Available stocks and prices:")
for name, price in stock_prices.items():
    print(f"  {name}: ${price}")
print()

portfolio = {}        # stock name -> quantity
total_investment = 0

while True:
    stock = input("Enter stock name (or type 'done' to finish): ").upper().strip()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not found. Please choose from the available list.\n")
        continue

    qty_text = input(f"Enter quantity of {stock}: ").strip()

    if not qty_text.isdigit() or int(qty_text) <= 0:
        print("Please enter a valid whole number greater than 0.\n")
        continue

    quantity = int(qty_text)

    # If the same stock is entered again, add to the old quantity
    portfolio[stock] = portfolio.get(stock, 0) + quantity
    print(f"Added {quantity} share(s) of {stock}.\n")

# Calculate and display the results
print("\n--- Portfolio Summary ---")
if len(portfolio) == 0:
    print("No stocks entered.")
else:
    for stock, quantity in portfolio.items():
        value = stock_prices[stock] * quantity
        total_investment += value
        print(f"{stock}: {quantity} x ${stock_prices[stock]} = ${value}")
    print(f"\nTotal Investment: ${total_investment}")

    # Optional: save the result to a text file
    save = input("\nSave result to a file? (yes/no): ").lower().strip()
    if save == "yes":
        with open("portfolio_result.txt", "w") as file:
            file.write("Stock Portfolio Summary\n")
            file.write("-----------------------\n")
            for stock, quantity in portfolio.items():
                value = stock_prices[stock] * quantity
                file.write(f"{stock}: {quantity} x ${stock_prices[stock]} = ${value}\n")
            file.write(f"\nTotal Investment: ${total_investment}\n")
        print("Saved to portfolio_result.txt")