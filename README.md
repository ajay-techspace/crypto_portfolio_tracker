# Crypto Portfolio Tracker

A simple Python project to track your cryptocurrency portfolio, calculate returns, and visualize your holdings.

## Features

- Calculates profit/loss for each coin
- Fetches live prices (or use manual prices)
- Visualizes portfolio distribution with charts

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
