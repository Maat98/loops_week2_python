# %discount is equal to 20%
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discounted_price = 1500 - (1500 * (discount_percent / 100))
        return discounted_price
    else:
        return price

original_price = 1500
discount_percentage = 20
final_price = calculate_discount(original_price, discount_percentage)
print("Final price after discount:", final_price)

# %discount is less than 20%
def calculate_discount(price, discount_percent):
    if discount_percent >= 15:
        discounted_price = 1500 - (1500 * (discount_percent / 100))
        return discounted_price
    else:
        return price

original_price = 1500
discount_percentage = 15
final_price = calculate_discount(original_price, discount_percentage)
print("Final price after discount:", final_price)

# %discount greater than 20%(no discount)
def calculate_discount(price, discount_percent):
    if discount_percent >= 0:
        discounted_price = 1500 - (1500 * (discount_percent / 100))
        return discounted_price
    else:
        return price

original_price = 1500
discount_percentage = 0
final_price = calculate_discount(original_price, discount_percentage)
print("Final price after discount:", final_price)
