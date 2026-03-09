# Simple Shopping Cart Program

item1 = input("Enter the first item: ")
price1 = float(input("Enter the price of the first item: "))

item2 = input("Enter the second item: ")
price2 = float(input("Enter the price of the second item: "))

item3 = input("Enter the third item: ")
price3 = float(input("Enter the price of the third item: "))

total = price1 + price2 + price3

print("\n--- Shopping Cart ---")
print(item1, "-", price1)
print(item2, "-", price2)
print(item3, "-", price3)

print("Total price:", total)