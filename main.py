import random
import matplotlib.pyplot as plt


def monty_hall_simulation(n_doors, k_repetitions):
    if n_doors < 3:
        raise ValueError("Number of doors must be at least 3")

    strategy1_wins = 0
    strategy2_wins = 0

    for _ in range(k_repetitions):
        gift_door = random.randint(1, n_doors)

        first_choice = random.randint(1, n_doors)

        remaining_doors = list(range(1, n_doors + 1))
        remaining_doors.remove(first_choice)
        if gift_door != first_choice:
            remaining_doors.remove(gift_door)

        doors_to_open = random.sample(remaining_doors, n_doors - 2)

        unopened_doors = list(range(1, n_doors + 1))
        unopened_doors.remove(first_choice)
        for door in doors_to_open:
            unopened_doors.remove(door)
        other_unopened = unopened_doors[0]

        if first_choice == gift_door:
            strategy1_wins += 1

        if other_unopened == gift_door:
            strategy2_wins += 1

    prob_strategy1 = strategy1_wins / k_repetitions
    prob_strategy2 = strategy2_wins / k_repetitions

    return prob_strategy1, prob_strategy2


def run_simulations_for_n(n_values, k_values):
    results = {}

    for n in n_values:
        results[n] = {}
        print(f"\nResults for N = {n} doors:")
        print("-" * 50)
        print(f"{'K repetitions':<15} {'Strategy 1 (Stay)':<20} {'Strategy 2 (Switch)':<20}")
        print("-" * 50)

        for k in k_values:
            prob1, prob2 = monty_hall_simulation(n, k)
            results[n][k] = (prob1, prob2)
            print(f"{k:<15} {prob1:<20.6f} {prob2:<20.6f}")

    return results


def plot_results(results, n_values, k_values):

    fig, axes = plt.subplots(len(n_values), 1, figsize=(10, 4 * len(n_values)))
    if len(n_values) == 1:
        axes = [axes]

    for i, n in enumerate(n_values):
        ax = axes[i]
        k_values_log = [k for k in k_values]
        strategy1_probs = [results[n][k][0] for k in k_values]
        strategy2_probs = [results[n][k][1] for k in k_values]

        ax.plot(k_values_log, strategy1_probs, 'o-', label='Strategy 1 (Stay)')
        ax.plot(k_values_log, strategy2_probs, 's-', label='Strategy 2 (Switch)')
        ax.axhline(y=1 / n, color='r', linestyle='--', label=f'Expected Strategy 1 (1/{n})')
        ax.axhline(y=(n - 1) / n, color='g', linestyle='--', label=f'Expected Strategy 2 ({n - 1}/{n})')

        ax.set_xscale('log')
        ax.set_xlabel('Number of Repetitions (K)')
        ax.set_ylabel('Probability of Winning')
        ax.set_title(f'Monty Hall Simulation Results for N = {n} Doors')
        ax.grid(True)
        ax.legend()

    plt.tight_layout()
    plt.savefig('problem2(montyhall)_results.png')
    plt.close()


def main():
    n_values = [3, 4, 5, 10, 20]
    k_values = [10, 100, 1000, 10000]

    # probabilities in theory
    print("Theoretical Probabilities:")
    print("-" * 50)
    print(f"{'N doors':<10} {'Strategy 1 (Stay)':<20} {'Strategy 2 (Switch)':<20}")
    print("-" * 50)
    for n in n_values:
        print(f"{n:<10} {1 / n:<20.6f} {(n - 1) / n:<20.6f}")
    print("-" * 50)

    # run the sim
    results = run_simulations_for_n(n_values, k_values)

    # plot the results
    try:
        plot_results(results, n_values, k_values)
        print("\nResults have been plotted and saved as 'problem2(montyhall)_results.png' in .exe dir.")
    except ImportError:
        print("\nMatplotlib is not available. Results have not been plotted.")


if __name__ == "__main__":
    main()