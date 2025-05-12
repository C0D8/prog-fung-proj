import yfinance as yf

TICKERS = [
    "UNH", "GS", "MSFT", "HD", "V", "SHW", "MCD", "CAT", "AMGN", "AXP",
    "TRV", "CRM", "IBM", "JPM", "AAPL", "HON", "AMZN", "PG", "BA", "JNJ",
    "CVX", "MMM", "NVDA", "WMT", "DIS", "MRK", "KO", "CSCO", "NKE", "VZ"
]



def load_data(tickers, start="2024-08-01", end="2024-12-31"):
    _data = yf.download(tickers, start=start, end=end)
    data = _data['Close']
    #save in csv
    data.to_csv('./data/data.csv')
    print("Data saved to ./data/data.csv")

    return data.dropna()



if __name__ == "__main__":
    data = load_data(TICKERS)
    print(data.head())