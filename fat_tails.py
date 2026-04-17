import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Download S&P 500 data (20 years for good statistics)
ticker = "^GSPC"  # S&P 500
data = yf.download(ticker, start="2004-01-01", end="2024-01-01")

# Calculate daily returns as percentage
returns = data["Close"].pct_change().dropna() * 100

# Plot histogram
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.hist(returns, bins=100, density=True, alpha=0.7, color="steelblue", edgecolor="black")
plt.xlabel("Daily Return (%)")
plt.ylabel("Density")
plt.title("S&P 500 Daily Returns (2004-2024)")
plt.grid(True, alpha=0.3)

# Add a normal distribution for comparison
x = np.linspace(returns.min(), returns.max(), 100)
normal_pdf = stats.norm.pdf(x, returns.mean(), returns.std())
plt.plot(x, normal_pdf, "r-", linewidth=2, label="Normal Distribution")

plt.legend()
plt.subplot(1, 2, 2)

# Log scale plot to see the tails better
counts, bins, _ = plt.hist(returns, bins=100, density=True, alpha=0.7, color="steelblue", edgecolor="black", log=True)
plt.yscale("log")
plt.xlabel("Daily Return (%)")
plt.ylabel("Density (log scale)")
plt.title("Same Data on Log Scale (Reveals Power Law)")
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()