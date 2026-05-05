# 📊 Econophysics: Power Laws in Stock Market Returns

## 📌 Project Overview
This project investigates whether stock market returns follow a **normal (Gaussian) distribution** or a **power law distribution**.  

This distinction is critical in finance:  
- A **normal distribution** assumes extreme events (crashes) are extremely rare.  
- A **power law distribution** implies **fat tails**, meaning large market moves occur far more frequently than standard models predict.

---

## 🚀 Key Finding
Analysis of **S&P 500 daily returns (2014–2024)** shows that returns follow a **power law distribution** with exponent:

\[
\alpha = 2.71
\]

This strongly contradicts the assumption of normality used in many financial risk models.

---

## ⚠️ Why This Matters
Traditional financial models underestimate risk because they assume a bell curve.

| Model | Predicted Frequency of 5% Crash | Observed Reality |
|------|-------------------------------|------------------|
| Normal Distribution | Once every 5,000+ years | ❌ Unrealistic |
| Power Law (α = 2.71) | Once every 1–2 years | ✅ Matches markets |

👉 This means **extreme market events are not "black swans" — they are expected**.

---

## 🧠 Concepts Covered
- Econophysics  
- Heavy-tailed distributions  
- Power laws  
- Log returns  
- Risk modeling  
- Fat tails in financial data  

---

## 🛠️ Methodology

### 1. Data Collection
- Historical S&P 500 data retrieved using `yfinance`
- Time period: **2014–2024**

### 2. Data Processing
- Computed **daily log returns**:

\[
r_t = \ln\left(\frac{P_t}{P_{t-1}}\right)
\]

### 3. Distribution Analysis
- Plotted return histogram
- Compared against a fitted **normal distribution**

### 4. Power Law Fitting
- Focused on extreme negative returns (threshold: **−2%**)
- Converted to log-log scale
- Applied **linear regression** to estimate slope

### 5. Estimation
- Power law form:

\[
P(x) \sim x^{-\alpha}
\]

- Estimated exponent:

\[
\alpha = 2.71
\]

---

## 📈 Results

### 1. Fat Tails
- Linear scale: resembles normal distribution  
- Log scale: reveals **heavy tails**  

📷 `returns_plot.png`  
> Right-side log plot shows deviation from Gaussian behavior.

---

### 2. Power Law Behavior
- Log-log plot produces a **straight line**
- Confirms scaling behavior of extreme returns  

📷 `powerlaw_fit.png`  
> Straight-line fit validates power law distribution.

---

## 📂 Project Structure
```
├── data/
├── notebooks/
├── returns_plot.png
├── powerlaw_fit.png
├── analysis.py
└── README.md
```

---

## 🧪 How to Run

### 1. Install Dependencies
```bash
pip install yfinance numpy pandas matplotlib scipy
```

### 2. Run Analysis
```bash
python analysis.py
```

---

## 📊 Key Insight
Financial markets are **not well described by Gaussian statistics**.

Instead:
- They exhibit **scale invariance**
- Large fluctuations are **structurally built into the system**
- Risk models must account for **fat tails**

---

## 🏦 Implications
- Underestimation of risk in banks and hedge funds  
- Mispricing of derivatives  
- Failure of Value-at-Risk (VaR) models during crises  
- Need for alternative models (e.g., stable distributions, EVT)

---

## 🔮 Future Work
- Extend analysis to other indices (NASDAQ, FTSE, crypto)
- Compare with **Extreme Value Theory (EVT)**
- Test stability of exponent α across time
- Use **maximum likelihood estimation (MLE)** instead of regression
- Study volatility clustering

---

## 📚 References
- Mandelbrot, B. – *The Misbehavior of Markets*  
- Taleb, N. N. – *The Black Swan*  
- Cont, R. – Empirical properties of asset returns  

---

## 👨‍💻 Author
**Njabulo Simelane**  
Computational Physics Student  

---

## ⭐ Final Takeaway
Markets are far riskier than traditional models suggest.  
If you assume a bell curve, you are **systematically underestimating reality**.

