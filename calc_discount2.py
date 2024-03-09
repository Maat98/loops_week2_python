def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = 500 - (500 * (discount_percent / 100))
        return discounted_price
    else:
        return price

# original price and discount percentage
original_price = 500
discount_percentage = 20

# final price after applying the discount
final_price = calculate_discount(original_price, discount_percentage)

# Print the final price after applying the discount
if final_price != original_price:
    print("Final price after applying the discount:", final_price)
else:
    print("No discount applied. Final price remains the same:", final_price)
