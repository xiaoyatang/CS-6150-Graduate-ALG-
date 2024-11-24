import random

def simulate_random_walk(num_steps):
    origin_crosses = 0
    position = 0
    previous_position = 0  # Initialize previous position as zero

    for _ in range(num_steps):
        step = 1 if random.random() < 0.5 else -1
        new_position = position + step

        # Check if the particle crosses the origin: from positive to negative or vice versa
        if previous_position * new_position < 0:
            origin_crosses += 1

        previous_position = position  # Update previous position to current before the move
        position = new_position  # Update position after the move

    return origin_crosses

def average_origin_crosses(num_steps, num_trials):
    total_crosses = 0
    for trial in range(num_trials):
        # Optionally seed the random number generator for each trial
        random.seed(trial)  # Uncomment this line if deterministic randomness is needed per trial
        total_crosses += simulate_random_walk(num_steps)
    return total_crosses / num_trials

num_trials = 50
t_values = [4 * 10**4, 9 * 10**4, 16 * 10**4]
results = {t: average_origin_crosses(t, num_trials) for t in t_values}

print(results)
