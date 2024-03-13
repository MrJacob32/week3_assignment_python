def calculate_discount(price, discount_percent):
    final_price = price * (1 - discount_percent / 100)
    return final_price if discount_percent >= 20 else price

original_price = float(input("Enter the original price of the item: Tzs"))
discount_percent = float(input("Enter the discount percentage: "))

final_price = calculate_discount(original_price, discount_percent)

if final_price == original_price:
    print("No discount applied. Final price:", original_price)
else:
    print("Final price after applying discount:", final_price)



