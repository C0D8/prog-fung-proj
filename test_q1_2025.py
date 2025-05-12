from simulate import evaluate_portfolio_performance
import yfinance as yf

# Substitua isso com sua melhor carteira:
best_assets_and_weights = [
    ('AAPL', 0.0422), ('AXP', 0.0363), ('CAT', 0.0046), ('CRM', 0.1601),
    ('CSCO', 0.0052), ('CVX', 0.0156), ('DIS', 0.0665), ('GS', 0.0127),
    ('HD', 0.0175), ('IBM', 0.0195), ('JNJ', 0.0099), ('JPM', 0.0255),
    ('KO', 0.0777), ('MCD', 0.0291), ('MRK', 0.0050), ('MSFT', 0.0052),
    ('NKE', 0.0031), ('NVDA', 0.0442), ('PG', 0.0205), ('SHW', 0.0074),
    ('TRV', 0.0218), ('UNH', 0.0015), ('V', 0.1618), ('VZ', 0.0131), ('WMT', 0.1942)
]

tickers = [t[0] for t in best_assets_and_weights]
weights = [t[1] for t in best_assets_and_weights]

# Baixar preços de Jan a Mar 2025
data = yf.download(tickers, start="2025-01-01", end="2025-03-31")['Close'].dropna()

# Avaliar desempenho
ret, vol, sharpe = evaluate_portfolio_performance(data, best_assets_and_weights)

print("\n📈 Desempenho no 1º trimestre de 2025:")
print(f"🔹 Retorno anualizado: {ret:.4f}")
print(f"🔹 Volatilidade anualizada: {vol:.4f}")
print(f"🔹 Sharpe Ratio: {sharpe:.4f}")
