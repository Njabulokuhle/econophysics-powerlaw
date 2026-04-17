import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

print("Step 1: Downloading data...")

# Download S&P 500 data
ticker = "^GSPC"
data = yf.download(ticker, start="2014-01-01", end="2024-01-01")

print(f"Step 2: Downloaded {len(data)} days of data")

# Get closing prices and convert to 1D array
close_prices = data['Close'].values.flatten()  # .flatten() ensures 1D array

print(f"Step 3: Closing prices shape: {close_prices.shape}")

# Calculate daily returns as percentage
# Using a simple loop approach to avoid shape issues
returns_array = []
for i in range(1, len(close_prices)):
    daily_return = (close_prices[i] - close_prices[i-1]) / close_prices[i-1] * 100
    returns_array.append(daily_return)

returns_array = np.array(returns_array)

print(f"Step 4: Calculated {len(returns_array)} daily returns")

# Calculate statistics
mean_return = np.mean(returns_array)
std_return = np.std(returns_array)
print(f"Step 5: Mean return = {mean_return:.2f}%, Std dev = {std_return:.2f}%")

# Plot histogram
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.hist(returns_array, bins=100, density=True, alpha=0.7, color="steelblue", edgecolor="black")
plt.xlabel("Daily Return (%)")
plt.ylabel("Density")
plt.title("S&P 500 Daily Returns (2014-2024)")
plt.grid(True, alpha=0.3)

# Add normal distribution for comparison
x = np.linspace(np.min(returns_array), np.max(returns_array), 100)
normal_pdf = stats.norm.pdf(x, mean_return, std_return)
plt.plot(x, normal_pdf, "r-", linewidth=2, label="Normal Distribution")
plt.legend()

plt.subplot(1, 2, 2)
plt.hist(returns_array, bins=100, density=True, alpha=0.7, color="steelblue", edgecolor="black", log=True)
plt.yscale("log")
plt.xlabel("Daily Return (%)")
plt.ylabel("Density (log scale)")
plt.title("Same Data on Log Scale")
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("\nStep 6: Close the plot window to continue...")
input("Press Enter after closing the plot window...")

# Power law fit
print("\nStep 7: Fitting power law to extreme returns...")

# Focus on negative returns (crashes) and make them positive
negative_returns = -returns_array[returns_array < 0]

if len(negative_returns) == 0:
    print("No negative returns found. Something went wrong.")
    exit()

threshold = 2.0  # 2% drop
tail = negative_returns[negative_returns > threshold]

print(f"Found {len(tail)} extreme negative returns beyond {threshold}%")

if len(tail) > 10:
    # Sort the tail
    sorted_tail = np.sort(tail)
    n = len(sorted_tail)
    
    # Empirical survival function: P(X > x)
    survival = np.array([(n - i) / n for i in range(n)])
    
    # Take logs (avoid log(0) by filtering out zeros)
    log_x = np.log(sorted_tail)
    log_survival = np.log(survival)
    
    # Fit line: log_survival = -alpha * log_x + constant
    slope, intercept = np.polyfit(log_x, log_survival, 1)
    alpha = -slope
    
    print(f"\n--- RESULTS ---")
    print(f"Power law exponent (alpha): {alpha:.2f}")
    
    if alpha < 3:
        print("→ Alpha < 3: Extremely fat tails")
    elif alpha > 4:
        print("→ Alpha > 4: Thinner tails than typical markets")
    else:
        print("→ Alpha between 3-4: Matches econophysics literature")
    
    # Plot the power law fit
    plt.figure(figsize=(8, 6))
    plt.loglog(sorted_tail, survival, "bo", markersize=4, alpha=0.5, label="Actual Data")
    plt.loglog(sorted_tail, np.exp(intercept) * (sorted_tail ** (-alpha)), "r-", linewidth=2, label=f"Power Law: α = {alpha:.2f}")
    plt.xlabel("Negative Return Magnitude (%)")
    plt.ylabel("P(X > x)")
    plt.title("Power Law Fit to Extreme Negative Returns")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()
    
    print("\n✅ Project complete! You have successfully demonstrated fat tails in stock returns.")
    
else:
    print(f"Only found {len(tail)} extreme returns. Try lowering the threshold.")
    print("You can modify the 'threshold' variable to a lower value like 1.5")

print("\nDone!")