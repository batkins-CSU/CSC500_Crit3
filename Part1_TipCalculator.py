
def calculateTip(items=[], tipPercentage = 0.18, salesTax = 0.07):
    total = 0
    for item in items:
        total += item
    tip = total * tipPercentage
    salesTax = total * salesTax
    return round(total, 2), round(tip, 2), round(salesTax, 2)

def main():
    print("Welcome to the tip calculator.")
    priceHolder = []
    finished = False

    while not (finished):
        try:
            # get the price of the item rounded to two decimal places as currency
            userInput = input("What was the Item Price? Type x when complete: ")
            if userInput.lower().strip() == "x":
                finished = True
                break
            else:
                price = round(float(userInput), 2)
                priceHolder.append(price)
        except ValueError:
            print("Please enter a valid price.")

    total, tip, salesTax = calculateTip(priceHolder)
    for itemPrice in priceHolder:
        print(f"Item Price: ${itemPrice:.2f}")

    print(f"Total before tax and tip: $ {total:.2f}")
    print(f"Sales Tax: ${salesTax:.2f}")
    print(f"Tip: ${tip:.2f}")
    print(f"Total: $ {round(total + salesTax + tip,2):.2f}")

if __name__ == "__main__":
    main()


