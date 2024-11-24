import random

def simulate_voting(sample_size, num_trials):
    votes = ['+1'] * 350000 + ['-1'] * 400000 + ['0'] * 250000
    majority_minus_one_count = 0

    for trial in range(num_trials):
        random.seed(trial)
        sample = random.sample(votes, sample_size)
        if sample.count('-1') > max(sample.count('+1'), sample.count('0')):
            majority_minus_one_count += 1

    return majority_minus_one_count / num_trials

# Sample sizes to test
sample_sizes = [10, 120, 250]
num_trials = 200

# Run experiments for each sample size
probabilities = {size: simulate_voting(size, num_trials) for size in sample_sizes}
print(probabilities)

# Finding the required sample size for which the probability that '-1' is majority is at least 0.9
required_sample_size = 10  # Start with a low number and increase
while True:
    probability = simulate_voting(required_sample_size, num_trials)
    if probability >= 0.9:
        break
    required_sample_size += 1

print(f"Required sample size for '-1' majority probability >= 0.9: {required_sample_size}")
