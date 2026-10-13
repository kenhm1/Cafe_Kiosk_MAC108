# Menu Items
menu_items = [("Blueberry Muffin", 2.00), ("Any Size coffee", 3.00), ("Hot chocolate", 2.50)]


total_bill = 0.00
while True:
    print("-----Py Cafe-----") 
    for i, (item, price) in enumerate(menu_items, start=1):
        print(f"{i}. {item} - ${price:.2f}")
    print("4. Checkout")
    choice = input("Select Options (1-4)")
    if choice == "1":
        total_bill += 2.00
        print(f"Added Blueberry Muffin. Current total: ${total_bill:.2f}")
    elif choice == "2":
        total_bill += 3.00
        print(f"Added Any size Coffee. Current total: ${total_bill:.2f}")
    elif choice == "3":
        total_bill += 2.50
        print(f"Added Hot Chocolate. Current total: ${total_bill:.2f}")
    elif choice == "4":
        print(f"Final total: ${total_bill:.2f} Thank you for ordering with us!")
        break
    else:
        print("Invalid selection. Please choose a valid menu item.") 
