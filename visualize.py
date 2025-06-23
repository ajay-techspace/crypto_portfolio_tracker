import matplotlib.pyplot as plt

def plot_portfolio(df):
    # Filter out rows with missing 'value'
    df = df.dropna(subset=['value'])

    if df.empty:
        print("⚠️ No data to plot (all rows are invalid or missing prices).")
        return

    # Plot pie chart of portfolio value distribution
    plt.figure(figsize=(6, 6))
    plt.pie(df['value'], labels=df['coin'], autopct='%1.1f%%')
    plt.title("Portfolio Allocation")
    plt.show()
