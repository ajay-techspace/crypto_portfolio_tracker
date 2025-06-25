# Crypto Portfolio Tracker

Track and analyze your cryptocurrency investments in real-time using Python. This command-line tool calculates individual and total returns, fetches live market prices, and visualizes your portfolio distribution.

## 🚀 Features

- 📈 Calculates portfolio value, cost basis, and profit/loss per asset
- 🔄 Fetches real-time prices from the CoinGecko API (or supports manual pricing)
- 📊 Visualizes asset allocation and returns using pie and bar charts
- ✅ Supports CSV input for easy data entry and updates
- 🛡 Robust error handling and input validation

## Setup

1. Clone the repo:
   ```
   git clone https://github.com/ajay-techspace/crypto_portfolio_tracker.git
   cd crypto-portfolio-tracker
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Add your portfolio to `portfolio.csv` (see sample below).

## Usage

Run the main script:
```
python main.py
```

## Sample `portfolio.csv`

| coin     | quantity | buy_price |
|----------|----------|-----------|
| bitcoin  | 0.5      | 20000     |
| ethereum | 2        | 1500      |

## Requirements

- pandas
- requests
- matplotlib

## License

This project is licensed under the [MIT License](./LICENSE).
