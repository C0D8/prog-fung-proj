from concurrent.futures import ProcessPoolExecutor, as_completed
import itertools
import numpy as np
from tqdm import tqdm
from data_loader import load_data_from_csv, get_daily_returns
from simulate import simulate_best_portfolio

if __name__ == "__main__":
    prices = load_data_from_csv('data/data.csv')
    daily_returns = get_daily_returns(prices)

    all_combinations = list(itertools.combinations(prices.columns, 25))
    overall_best_sharpe = -np.inf
    overall_best_result = {}

    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(simulate_best_portfolio, comb, daily_returns) for comb in all_combinations]

        for f in tqdm(as_completed(futures), total=len(futures)):
            result = f.result()
            if result['sharpe'] > overall_best_sharpe:
                overall_best_sharpe = result['sharpe']
                overall_best_result = result

    print(f"\n🏆 Best Sharpe Ratio: {overall_best_result['sharpe']:.4f}")
    print("📊 Assets and Weights:")
    for asset, weight in overall_best_result['assets']:
        print(f"{asset}: {weight:.4f}")
