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
        print("Basket: ")
        for item in basket:
            print(item.type)

if __name__ == "__main__":
    main()
        
    