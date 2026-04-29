# Econophysics: Power Laws in Stock Market Returns

## Overview
This project tests whether stock market returns follow a **normal distribution** (bell curve) or a **power law distribution**. The answer has major implications for risk management — normal distributions underestimate crash risk.

## Key Finding
S&P 500 daily returns (2014-2024) follow a power law with exponent **α = 2.71**, NOT a normal distribution. This means extreme crashes happen **hundreds of times more often** than Gaussian models predict.

## Why This Matters
| Distribution | Prediction for 5% crash | Reality |
|--------------|------------------------|---------|
| Normal (bell curve) | Once every 5,000+ years | |
| Power law (α = 2.71) | Once every 1-2 years | ✓ Actual market behavior |

Banks and hedge funds that use normal distribution models systematically underestimate risk.

## Methods
1. Downloaded 10+ years of S&P 500 data via `yfinance`
2. Calculated daily log returns
3. Plotted return distribution vs normal curve
4. Fitted power law to extreme negative returns (threshold: 2%)
5. Used log-log linear regression to estimate exponent α

## Results

### Visualization 1: Fat Tails
![Returns Distribution](returns_plot.png)
*Left: Regular scale. Right: Log scale reveals power law as straight line.*

### Visualization 2: Power Law Fit
![Power Law Fit](powerlaw_fit.png)
*Log-log plot of extreme negative returns. Straight red line confirms power law.*

### Statistical Output
