import random

def roll_dice(num_dice=1):
    """Roll one or more dice and return the results"""
    results = []
    for _ in range(num_dice):
        results.append(random.randint(1, 6))
    return results

def main():
    print("🎲 Welcome to the Dice Roller Simulator! 🎲")
    print("-" * 40)

    while True:
        num_dice = input("\nHow many dice do you want to roll? (Enter 'q' to quit): ")

        if num_dice.lower() == 'q':
            print("Thanks for playing! Goodbye! 👋")
            break

        if not num_dice.isdigit():
            print("Please enter a valid number!")
            continue

        num_dice = int(num_dice)

        if num_dice <= 0:
            print("Please enter a number greater than 0.")
            continue

        if num_dice > 10:
            print("Maximum 10 dice allowed!")
            continue

        results = roll_dice(num_dice)

        print(f"\n🎲 Rolling {num_dice} dice...")
        print("Results:", ' + '.join(f"[{r}]" for r in results))

        if num_dice > 1:
            total = sum(results)
            print(f"Total: {total}")

        if num_dice == 1:
            if results[0] == 6:
                print("🔥 Maximum roll! Lucky you!")
            elif results[0] == 1:
                print("😅 Oops! Better luck next time!")
        else:
            total = sum(results)
            if total == num_dice * 6:
                print("🔥 PERFECT SCORE! All sixes!")
            elif total == num_dice:
                print("😅 All ones! What are the odds?")

if __name__ == "__main__":
    main()
