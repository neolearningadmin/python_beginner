# --- THE CLEAN CODE REFACTOR ---
# Demonstrating PEP 8 Best Practices

# BAD CODE (Don't do this!)
def total(a,b):
 return a+b
x=10
y=5
print(total(x,y))

# GOOD CODE (PEP 8 Compliant)
def calculate_total_price(base_price, tax_amount):
    """Returns the sum of price and tax."""
    return base_price + tax_amount


# Set our initial values
item_price = 10.00
sales_tax = 0.50

# Calculate and display
final_total = calculate_total_price(item_price, sales_tax)
print(f"The final total is: ${final_total}")