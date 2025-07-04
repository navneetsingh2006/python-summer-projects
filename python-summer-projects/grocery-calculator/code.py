def show_menu():
    print("\nGROCERY CALCULATOR")
    print("1. View Products")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")

    #comment

def get_products():
    return {
        "apple": 40.00,
        "banana": 10.00,
        "milk": 55.00,
        "bread": 35.00,
        "eggs": 60.00,
        "rice": 80.00,
        "cheese": 50.00,
        "pasta": 45.00,
        "tomato": 20.00,
        "potato": 25.00,
        "onion": 30.00,
        "maggi": 15.00,
        "biscuit": 10.00,
        "cold drink": 40.00,
        "tea": 20.00,
        "sugar": 45.00,
        "atta": 35.00,
        "oil": 120.00,
        "salt": 18.00
    }


def show_products():
    print("\nAvailable Products:")
    print("-" * 25)
    for item, price in get_products().items():
        print(f"{item.title()}: ₹{price:.2f}")

def get_valid_product():
    products = get_products()
    while True:
        item = input("\nEnter product name: ").lower()
        if item in products:
            return item
        print("Product not found! Try again.")

def get_valid_quantity():
    while True:
        try:
            qty = int(input("Enter quantity: "))
            if qty > 0:
                return qty
            print("Quantity must be positive!")
        except ValueError:
            print("Please enter a valid number!")

def add_item(cart):
    show_products()
    item = get_valid_product()
    qty = get_valid_quantity()
    cart[item] = cart.get(item, 0) + qty
    print(f"Added {qty} {item}(s) to cart")

def show_cart(cart):
    if not cart:
        print("\nYour cart is empty!")
        return 0

    print("\nYour Cart:")
    print("-" * 30)

    products = get_products()
    total = 0
    for item, qty in cart.items():
        price = products[item]
        item_total = price * qty
        total += item_total
        print(f"{item.title()}: {qty} x ₹{price:.2f} = ₹{item_total:.2f}")

    print("-" * 30)
    print(f"Subtotal: ₹{total:.2f}")
    return total

def checkout(cart):
    subtotal = show_cart(cart)
    if subtotal == 0:
        return

    gst = subtotal * 0.18
    total = subtotal + gst

    print(f"GST (18%): ₹{gst:.2f}")
    print(f"Total amount to pay: ₹{total:.2f}")

    while True:
        try:
            payment = float(input("Enter payment (₹): "))
            if payment >= total:
                break
            print(f"Not enough! Need ₹{total - payment:.2f} more.")
        except ValueError:
            print("Please enter a valid amount!")

    if payment > total:
        print(f"Your change: ₹{payment - total:.2f}")

    cart.clear()
    print("Thank you for shopping!")

def main():
    cart = {}
    print("Welcome to the Grocery Store!")

    while True:
        show_menu()
        choice = input("\nChoose option (1-5): ")

        if choice == '1':
            show_products()
        elif choice == '2':
            add_item(cart)
        elif choice == '3':
            show_cart(cart)
        elif choice == '4':
            checkout(cart)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Pick 1-5.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
