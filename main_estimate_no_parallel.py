import itertools
from tqdm import tqdm
import time
from datetime import timedelta
from data_loader import load_data_from_csv, get_daily_returns
from simulate import simulate_best_portfolio

if __name__ == "__main__":
    prices = load_data_from_csv('data/data.csv')
    daily_returns = get_daily_returns(prices)

    all_combinations = list(itertools.combinations(prices.columns, 25))
    
    sample_size = 100
    sample_combinations = all_combinations[:sample_size]

    print(f"🔎 Estimando tempo com {sample_size} combinações...")
    start_sample = time.time()
    for comb in tqdm(sample_combinations, desc="Rodando amostra"):
        simulate_best_portfolio(comb, daily_returns)
    end_sample = time.time()

    sample_duration = end_sample - start_sample
    estimated_total = sample_duration / sample_size * len(all_combinations)

    print(f"\n🕒 Tempo estimado total (sem paralelismo): {timedelta(seconds=estimated_total)} ({estimated_total / 60:.2f} minutos)")
