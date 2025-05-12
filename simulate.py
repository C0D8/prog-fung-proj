from utils import generate_random_weights, sharpe_ratio
import numpy as np

def simulate_best_portfolio(combination, full_returns, n_simulations=1000):
    returns = full_returns[list(combination)]
    cov_matrix = returns.cov()
    best_sr = -np.inf
    best_weights = None
    for _ in range(n_simulations):
        weights = generate_random_weights(len(combination))
        sr = sharpe_ratio(weights, returns, cov_matrix)
        if sr > best_sr:
            best_sr = sr
            best_weights = weights

    return {
        "sharpe": best_sr,
        "assets": list(zip(combination, best_weights))
    }


def evaluate_portfolio_performance(prices_df, asset_weights, risk_free_rate=0.02):
    returns = prices_df.pct_change().dropna()
    weights = np.array([weight for _, weight in asset_weights])
    mean_return = np.dot(returns.mean(), weights) * 252
    volatility = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 252, weights)))
    sharpe = (mean_return - risk_free_rate) / volatility
    return mean_return, volatility, sharpe