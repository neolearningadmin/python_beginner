def calculate_total(price, discount_percent, tax):
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    # Adding the tax
    final_price = final_price + tax
    return final_price

# Calling it with the new requirement
final = calculate_total(100, 20, 5.00)
print(f"Final with tax: ${final}")