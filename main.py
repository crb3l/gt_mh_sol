import random
# import matplotlib.pyplot as plt # I wanted to plot the results, only thing being that matplotlib gave me troubles when exporting to an .exe so I had no choice, but to not plot the results ):



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
    input("\n When ready, please press any alphanumerical or modifier key to continue.")

if __name__ == "__main__":
    main()

