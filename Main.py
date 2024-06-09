import tkinter as tk
from tkinter import messagebox

def martingale_strategy(first_bet, num_steps):
    # List to hold the bet amounts for each step
    bet_amounts = []

    # Calculate the bet amounts for the specified number of steps
    for i in range(num_steps):
        bet_amounts.append(first_bet * (2 ** i))

    # Calculate the total amount needed for the specified steps
    total_bet_amount = sum(bet_amounts)

    return bet_amounts, total_bet_amount

def calculate():
    try:
        # Get user inputs
        total_amount = float(total_amount_entry.get())
        num_steps = int(num_steps_entry.get())
        first_bet = float(first_bet_entry.get())

        if total_amount <= 0:
            messagebox.showerror("Error", "The total amount must be a positive number.")
            return

        if num_steps <= 0:
            messagebox.showerror("Error", "The number of steps must be a positive integer.")
            return

        if first_bet < 5:
            messagebox.showerror("Error", "The first step bet amount must be at least Ghc 5.")
            return

        # Get the bet amounts for the specified steps and the total amount needed
        bet_amounts, total_bet_amount = martingale_strategy(first_bet, num_steps)

        # Check if the total amount is sufficient
        if total_amount < total_bet_amount:
            messagebox.showerror("Error", f"The total amount in your account is not sufficient for {num_steps} Martingale steps with a first bet of Ghc {first_bet:.2f}.\nTotal amount needed: Ghc {total_bet_amount:.2f}\nAmount short: Ghc {total_bet_amount - total_amount:.2f}")
            return

        # Calculate the remaining balance
        remaining_balance = total_amount - total_bet_amount

        # Display the results
        result_text = f"Total amount needed for {num_steps} Martingale steps with a first bet of Ghc {first_bet:.2f}: Ghc {total_bet_amount:.2f}\n"
        result_text += f"Remaining balance: Ghc {remaining_balance:.2f}\n"
        result_text += "\nStep-by-step bet amounts:\n"

        for i, bet in enumerate(bet_amounts, start=1):
            result_text += f"Step {i} bet amount: Ghc {bet:.2f}\n"

        result_label.config(text=result_text)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Martingale Strategy Calculator")

# Create and place the widgets
tk.Label(root, text="Total Amount (Ghc):").grid(row=0, column=0, padx=10, pady=5)
total_amount_entry = tk.Entry(root)
total_amount_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Number of Steps:").grid(row=1, column=0, padx=10, pady=5)
num_steps_entry = tk.Entry(root)
num_steps_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="First Step Bet Amount (Ghc):").grid(row=2, column=0, padx=10, pady=5)
first_bet_entry = tk.Entry(root)
first_bet_entry.grid(row=2, column=1, padx=10, pady=5)

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, columnspan=2, pady=10)

result_label = tk.Label(root, text="", justify=tk.LEFT)
result_label.grid(row=4, columnspan=2, padx=10, pady=10)

# Start the main event loop
root.mainloop()
