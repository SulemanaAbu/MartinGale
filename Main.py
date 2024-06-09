def martingale_strategy(total_amount):
    # Initial bet amount (first gale)
    initial_bet = total_amount * 0.01  # assuming 1% of total amount as the initial bet

    # List to hold the bet amounts for each step
    bet_amounts = []

    # Calculate the bet amounts for 6 steps
    for i in range(6):
        bet_amounts.append(initial_bet)
        initial_bet *= 2  # Double the bet for the next step

    return bet_amounts

def main():
    try:
        # Ask the user to enter the total amount in the account
        total_amount = float(input("Enter the total amount in your account: $"))

        if total_amount <= 0:
            print("The total amount must be a positive number.")
            return

        # Get the bet amounts for the 6 steps
        bet_amounts = martingale_strategy(total_amount)

        # Display the bet amounts
        for i, bet in enumerate(bet_amounts, start=1):
            print(f"Step {i} bet amount: ${bet:.2f}")

    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
