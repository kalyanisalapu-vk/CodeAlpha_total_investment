import os

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2700,
    "MSFT": 300,
    "AMZN": 3300,
    "NFLX": 500,
    "META": 350,
    "NVDA": 900,
    "BABA": 80,
    "INTC": 45,
    "ORCL": 120,
    "IBM": 140,
    "ADBE": 550,
    "PYPL": 70,
    "UBER": 75
}

total_investment = 0

print("📈 Stock Portfolio Tracker")
print("Available stocks:", list(stock_prices.keys()))

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").strip().upper()
    
    if stock == "DONE":
        break
    
    if stock not in stock_prices:
        print("❌ Stock not available! Try again.")
        continue
    
    try:
        quantity = int(input("Enter quantity: "))
    except:
        print("❌ Please enter a valid number!")
        continue
    
    price = stock_prices[stock]
    investment = price * quantity
    
    total_investment += investment
    
    print(f"✅ Added {stock} | Price: {price} | Quantity: {quantity} | Value: {investment}")

print("\n💰 Total Investment Value:", total_investment)

with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    file.write("------------------------\n")
    file.write("Total Investment Value: " + str(total_investment))

print("📁 Data saved to portfolio.txt")
print("📍 File saved at:", os.getcwd())