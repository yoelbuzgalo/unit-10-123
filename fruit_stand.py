class Fruit:
    __slot__ = ['type', 'price']
    def __init__(self, type, price):
        self.type = type
        self.price = price

GRAPE = Fruit("Grapes", 3.50)
LYCHEE = Fruit("Lychee", 0.50)
PLUM = Fruit("Plum", 1.75)

INVENTORY = {"Grapes":GRAPE,"Lychee": LYCHEE,"Plum": PLUM}

def add_to_basket(list, fruit):
    list.append(fruit)

def price_in_basket(basket):
    total_price = 0
    for item in basket:
        total_price += item.price
    return total_price

def count_fruits(basket, fruit):
    count = 0
    for item in basket:
        if item == fruit:
            count += 1
    return count

def main():
    basket = []
    while True:
        user_input = input("Enter name of fruit to add to basket: ")
        if user_input == "":
            break
        if user_input in INVENTORY:
            add_to_basket(basket, INVENTORY[user_input])
        else:
            raise ValueError("We don't sell that kind of fruit")
    print("Total price of basket: ", price_in_basket(basket))
    for fruit in INVENTORY:
        count = count_fruits(basket, INVENTORY[fruit])
        if count > 0:
            print("You have ", count, INVENTORY[fruit].type)

if __name__ == "__main__":
    main()
        
    