class Fruit:
    type = ''
    price = 1000000

GRAPE = Fruit()
GRAPE.type = "Grapes"
GRAPE.price = 3.50

LYCHEE = Fruit()
LYCHEE.type = "Lychee"
LYCHEE.price = 0.50

PLUM = Fruit()
PLUM.type = "Plum"
PLUM.price = 1.75

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
        elif user_input == "Grapes":
            add_to_basket(basket, GRAPE)
        elif user_input == "Lychee":
            add_to_basket(basket, LYCHEE)
        elif user_input == "Plum":
            add_to_basket(basket, PLUM)
        else:
            raise ValueError("No fruit matched to add for basket")
    
    grape_count = count_fruits(basket, GRAPE)
    lychee_count = count_fruits(basket, LYCHEE)
    plum_count = count_fruits(basket, PLUM)
    
    print("Total price of basket: ", price_in_basket(basket))
    print("You have", grape_count, "bundles of", GRAPE.type)
    print("You have", plum_count, "bundles of", PLUM.type)
    print("You have", lychee_count, "bundles of", LYCHEE.type)

if __name__ == "__main__":
    main()
        
    