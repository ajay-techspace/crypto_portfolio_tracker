import pandas as pd
from calculate_returns import calculate_returns
from visualize import plot_portfolio

def main():
    df = pd.read_csv("portfolio.csv")

    # 🔧 Use manual prices (no API)
    manual_prices = {
        'bitcoin': 26000,
        'ethereum': 1800
    }
    df['current_price'] = df['coin'].map(manual_prices)

    # ✅ Calculate results
    df = calculate_returns(df)
    print(df)

    print("\n--- Portfolio Summary ---")
    print(df[['coin', 'quantity', 'buy_price', 'current_price', 'cost', 'value', 'profit_loss']])

    plot_portfolio(df)

if __name__ == "__main__":
    main()