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
        'Cornbread': 1.00,
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
            # I decided to have double letters here to avoid situations where there are two items with same first letter being selected (Pizza or Pasta for example). This would be a safer approach.
            letter = food.lower()[0] + food.lower()[1]
            food_dict[food] = letter
    return food_dict

# Constant to associate food code letter for every food item
FOOD_LETTER = get_food_letter()

class Combo:
    __slots__ = ['drink', 'entree', 'side', 'price']
    def __init__(self, drink, entree, side):
        self.drink = drink
        self.entree = entree
        self.side = side
        self.price = 0

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

def print_menu(menu_obj):
    """
    This function prints all items of a menu, seperated by categories
    """
    
    print("MENU", "All meals are a combo!",sep="\n", end="\n\n")
    
    print("Drinks")
    for i in range(len(menu_obj.drink_list)):
        menu_item = menu_obj.drink_list[i]
        print(menu_item.name,"(",menu_item.letter,")",": ", "$"+str(menu_item.price),sep="", end="\t")
    
    print("\n") # Empty line

    print("Entrees")
    for i in range(len(menu_obj.entree_list)):
        menu_item = menu_obj.entree_list[i]
        print(menu_item.name,"(",menu_item.letter,")",": ", "$"+str(menu_item.price),sep="", end="\t")

    print("\n") # Empty line

    print("Sides")
    for i in range(len(menu_obj.side_list)):
        menu_item = menu_obj.side_list[i]
        print(menu_item.name,"(",menu_item.letter,")",": ", "$"+str(menu_item.price),sep="", end="\t")


def main():
    my_menu = Menu()
    print_menu(my_menu)


if __name__ == "__main__":
    main()