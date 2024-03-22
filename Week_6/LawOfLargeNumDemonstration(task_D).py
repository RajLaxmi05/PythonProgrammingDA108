import numpy as np

num_trials = [10, 100, 1000, 10000, 100000]

def coin_toss_experiment(num_trials):
    outcomes = np.random.randint(0, 2, size = num_trials)
    sample_mean = np.mean(outcomes)
    return sample_mean
for trials in num_trials:
    sample_mean = coin_toss_experiment(trials)
    print(f"Number of trials: {trials}, Sample_mean: {sample_mean}")

