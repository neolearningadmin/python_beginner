# --- THE PRICE HERO CALCULATOR ---
# This script builds a reusable tool to calculate final shopping prices.

# 1. THE TOOL (Defining the Function)
def calculate_total(price, discount_percent):
    """
    Calculates the final price after a discount.
    """
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    
    return final_price

# 2. USING THE TOOL (The 'I Do')
print("--- SHOPPING CART ---")

# We can use our tool over and over with different numbers!
item_a = calculate_total(100, 20)
item_b = calculate_total(50, 10)
item_c = calculate_total(25, 0)

print(f"Item A: ${item_a}")
print(f"Item B: ${item_b}")
print(f"Item C: ${item_c}")

# 3. GLOBAL LOGIC
total_bill = item_a + item_b + item_c
print(f"\nGRAND TOTAL: ${total_bill}")

# --- THE CHALLENGE (YOU DO) ---
# 1. Update the function definition to include a third parameter: 'tax'.
# 2. Inside the function, add the tax to the 'final_price' before returning it.
#    (Hint: final_price = final_price + tax)
# 3. Call the function again with a tax of 5.00 and see the result.