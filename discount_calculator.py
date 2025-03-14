def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price


def get_final_price():
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = int(input("Enter the discount percentage: "))
    
    final_price = calculate_discount(original_price, discount_percent)
    
    if final_price != original_price:
        print(f"The final price after discount is: ${final_price:.2f}")
    else:
        print(f"The original price is: ${original_price:.2f} (No discount applied as it's less than 20%)")



# Testing the function
get_final_price()
