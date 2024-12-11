import random


def roll_dice(num_dice=10, kicker_threshold=7):

    if num_dice < 1:
        raise ValueError("You must roll at least one die.")

    # Roll the dice
    rolls = [random.randint(0, 9) for _ in range(num_dice)]
    total_value = sum(rolls)
    kicker = len(rolls) > kicker_threshold

    # Combine rolls at indices 6 and 7 into a tuple, then remove index 7
    if kicker:
        rolls[6] = (rolls[6], rolls[7])
        rolls.pop(7)

    # Adjust results if fewer dice are rolled

    kicker = rolls[6] if kicker else None

    return {
        "result": rolls,
        "kicker": kicker,
        "total": total_value
    }


# Example Usage
# Initial roll with exactly 10 dice
print("-" * 40)
initial_roll = roll_dice()
print("Initial Roll:", initial_roll)

# Roll with fewer dice, e.g., 8 dice
print("-" * 40)
print("-" * 40)

reduced_roll = roll_dice(num_dice=8)
print("Reduced Roll:", reduced_roll)
print("-" * 40)
print("-" * 40)

# Roll with fewer dice, kicker is removed when dice < 7
further_reduced_roll = roll_dice(num_dice=6)
print("Further Reduced Roll:", further_reduced_roll)
print("-" * 40)
