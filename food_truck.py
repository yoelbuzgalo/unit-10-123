# Constant prices for food items
FOOD_PRICES = {
    'Drink':
    {
        'Water': 2.00,
        'Coke': 3.25,
        'Beer': 5.00
    },
    'Entree': 
    {
        'Burger': 3.50,
        'Pizza' : 2.85,
        'Pasta' : 4.00
    },
    'Side' : 
    {
        'Fries': 1.20,
        'Salad': 2.25,
        'Cornbread': 1.00
    },
}

def get_food_letter():
    """
    Helper function that iterates over food price list and gets the food letter and associates the food with it.
    Returns a dict item to a global constant.
    """
    food_dict = dict()
    for type in FOOD_PRICES:
        for food in FOOD_PRICES[type]:
            # I decided to have double letters here (like in some examples 'cb' for cheese burger) to avoid situations where there are two items with same first letter being selected (Pizza or Pasta for example). This would be a safer approach.
            letter = food.lower()[0] + food.lower()[1]
            food_dict[food] = letter
    return food_dict

# Constant to associate food code letter for every food item
FOOD_LETTER = get_food_letter()

class Menu_Item:
    __slots__ = ['letter', 'name', 'price']
    def __init__(self, letter, name, price):
        self.letter = letter
        self.name = name
        self.price = price

class Menu:
    __slots__ = ['drink_list', 'entree_list', 'side_list']
    def __init__(self):
        # Initialize lists by category, each list item has relevant information associated with it (letter, name, price)
        self.drink_list = [Menu_Item(FOOD_LETTER[food_name], food_name, FOOD_PRICES['Drink'][food_name]) for food_name in FOOD_PRICES['Drink']]
        self.entree_list = [Menu_Item(FOOD_LETTER[food_name], food_name, FOOD_PRICES['Entree'][food_name]) for food_name in FOOD_PRICES['Entree']]
        self.side_list = [Menu_Item(FOOD_LETTER[food_name], food_name, FOOD_PRICES['Side'][food_name]) for food_name in FOOD_PRICES['Side']]

class Combo:
    __slots__ = ['drink', 'entree', 'side', 'price']
    def __init__(self, drink, entree, side):
        self.drink = drink
        self.entree = entree
        self.side = side
        self.price = (drink.price + entree.price + side.price)

def print_menu(menu):
    """
    This function prints all items of a menu, seperated by categories
    """
    
    print("MENU", "All meals are a combo!",sep="\n", end="\n\n")
    
    print("Drinks")
    for i in range(len(menu.drink_list)):
        menu_item = menu.drink_list[i]
        print(menu_item.name,"(",menu_item.letter,")",": ", "$"+str(menu_item.price),sep="", end="\t\t")
    
    print("\n") # Empty line

    print("Entrees")
    for i in range(len(menu.entree_list)):
        menu_item = menu.entree_list[i]
        print(menu_item.name,"(",menu_item.letter,")",": ", "$"+str(menu_item.price),sep="", end="\t\t")

    print("\n") # Empty line

    print("Sides")
    for i in range(len(menu.side_list)):
        menu_item = menu.side_list[i]
        print(menu_item.name,"(",menu_item.letter,")",": ", "$"+str(menu_item.price),sep="", end="\t\t")

    print("\n") # Empty line

def get_food_from_input(list, target):
    """
    Helper function to get the menu item information
    """
    for menu_item in list:
        if menu_item.letter == target:
            return menu_item
    

def order_combo(menu, drink_letter_input, entree_input_letter, side_input_letter):
    """
    This function returns a combo object, depending on client's order
    """
    drink = get_food_from_input(menu.drink_list, drink_letter_input)
    entree = get_food_from_input(menu.entree_list, entree_input_letter)
    side = get_food_from_input(menu.side_list, side_input_letter)

    if drink != None and entree != None and side != None:
        return Combo(drink, entree, side)
    else:
        raise ValueError("No matched items in menu was found")


def inquire_order():
    """
    This helper function takes in user input and returns input values
    """
    input_drink = str(input("What would you like to drink: "))
    input_entree = str(input("What would you like for your entree: "))
    input_side = str(input("What would you like for your side: "))
    
    return input_drink, input_entree, input_side

def take_order(menu):
    """
    This function takes an order and adds combos to cart. Returns a list of ordered combos.
    """
    cart = []
    while True:
        drink, entree, side = inquire_order()
        cart.append(order_combo(menu, drink, entree, side))
        inquire_add_combo = input("Would you like to add another combo (y/n):")
        if inquire_add_combo.lower() == 'y':
            continue
        else:
            break
    return cart

def main():
    """
    Main entry of this program
    """
    menu = Menu()
    print_menu(menu)
    cart = take_order(menu)
    print("Your order is:")
    total = 0
    for order in cart:
        print("Drink:", order.drink.name, "Entree:", order.entree.name, "Side:", order.side.name, "Price:", "$"+str(order.price))
        total += order.price
    print("Total:", "$"+str(total))


if __name__ == "__main__":
    main()