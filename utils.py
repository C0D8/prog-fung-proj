import numpy as np

def generate_random_weights(n, max_weight=0.2):
    weights = np.random.dirichlet(np.ones(n))
    while any(weights > max_weight):
        weights = np.random.dirichlet(np.ones(n))
    return weights

def portfolio_return(weights, returns):
    return np.dot(returns.mean(), weights) * 252

def portfolio_volatility(weights, cov_matrix):
    return np.sqrt(np.dot(weights.T, np.dot(cov_matrix * 252, weights)))

def sharpe_ratio(weights, returns, cov_matrix):
    ret = portfolio_return(weights, returns)
    vol = portfolio_volatility(weights, cov_matrix)
    return ret / vol  # taxa livre de risco = 0
