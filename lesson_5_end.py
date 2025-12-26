# --- THE BUDGET BATTLE ---
# A survival game where you try to make your $100 last a full week.

# 1. THE TOOLS (Our Function)
def process_day(current_balance, expense_name, cost):
    """Calculates the new balance and prints the transaction."""
    new_balance = current_balance - cost
    print(f"Spent ${cost} on {expense_name}.")
    return new_balance

# 2. THE GAME SETUP (Variables)
balance = 100
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
game_over = False

# 3. THE GAME LOOP (Bringing it all together)
print("--- WELCOME TO BUDGET BATTLE (Starting Balance: $100) ---")

for day in days:
    print(f"\nIt is {day}.")
    
    if day == "Saturday":
        print("Weekend luxury! Spend $40 on a nice dinner.")
        balance = process_day(balance, "Luxury Dinner", 40)
    else:
        print("Standard day. Spend $15 on essentials.")
        balance = process_day(balance, "Essentials", 15)

    # 4. THE LOGIC CHECK
    if balance <= 0:
        print("!!! BANKRUPT !!! You didn't make it to the end of the week.")
        game_over = True
        break 
    else:
        print(f"Remaining Balance: ${balance}")

# 5. THE FINAL RESULT
if not game_over:
    print("\nCONGRATULATIONS! You survived the week with money to spare.")

# --- THE CHALLENGE (YOU DO) ---
# 1. Add a 'Payday' feature! 
# 2. If the day is "Wednesday", add $50 to the balance before the daily expense.
# 3. Print "Payday! +$50" so the player knows.