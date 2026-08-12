def calculate_total(topping_count):
    pizza = 10.00
    topping = 1.50 * topping_count
    return pizza + topping

topping_count = 0

while True:
    add_topping = input("Enter a topping: pepperoni, mushrooms, extra cheese (or type 'done' to finish): ")
    
    if add_topping == "done":
        break
    
    topping_count += 1

total_bill = calculate_total(topping_count)
print(f"Your total bill is: ${total_bill:.2f}")

