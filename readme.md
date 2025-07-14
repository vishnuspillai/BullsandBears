# 📈 Bulls & Bears: Indian Stock Market Analysis Engine

> A modular Python project for visualizing, analyzing, and predicting stock price movements on the Indian stock market (NSE) using historical OHLC data, technical indicators, and simple machine learning models.

---

## 🚀 Features

- 🔽 **Download historical OHLC data** using `yfinance`
- 📉 **Plot candlestick charts** using `plotly`
- 🧭 **Identify support and resistance levels** using local extrema
- 🔮 **Predict future stock prices** using linear regression on moving averages
- 🧠 **Compute key technical indicators** (SMA, EMA, RSI, MACD)
- ⚙️ Built for modularity and GitHub collaboration

---

## 🧱 Project Structure

```
BullsandBears/
├── notebooks/
│   ├── 01_plot_sr.ipynb         
│   ├── 02_predict_prices.ipynb  
├── src/
│   ├── data_loader.py           
│   ├── support_resistance.py    
│   ├── predictor.py             
│   ├── indicator.py             
│   └── classifier.py            
├── data/
│   ├── raw/                     
│   └── processed/               
├── README.md
└── requirements.txt             
```

---

## 📦 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/BullsandBears.git
   cd BullsandBears
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch Jupyter Notebook**
   ```bash
   jupyter notebook
   ```

---

## 📊 Example Output

- ✅ Candlestick chart with SR points  
- ✅ Forecasted future price line  
- ✅ RSI and MACD overlays  
- ✅ CSVs saved to `data/processed/`  
- 🔜 Classifier prediction ("Up or Down tomorrow?")

---

## 📌 Dependencies

- `yfinance`  
- `pandas`  
- `numpy`  
- `plotly`  
- `scikit-learn`  
- `scipy`

```bash
pip install yfinance pandas numpy plotly scikit-learn scipy
```

---

## 📈 Sample Usage

```python
from src.data_loader import download_stock_data
from src.support_resistance import find_support_resistance
from src.predictor import predict_next_prices
from src.indicator import compute_rsi
```

---

## 📍 TODO (Next Modules)

- [x] Visualize OHLC and SR points
- [x] Forecast price using Linear Regression
- [x] Compute SMA, EMA, RSI, MACD
- [ ] Predict next-day trend using ML classifier
- [ ] Live dashboard (Streamlit or Dash)

---

## 👨‍💻 Author

**Vishnu S. Pillai**  
Bioinformatician | Data Engineer | Market Enthusiast  
GitHub: [@vishnuspillai](https://github.com/vishnuspillai)

---

> ⭐️ Star this repo if you find it useful. Contributions & issues welcome!
