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

def get_food_code():
    """
    Helper function that iterates over food price list and gets the food letter and associates the food with it.
    """
    food_dict = dict()
    for type in FOOD_PRICES:
        for food in FOOD_PRICES[type]:
            letter = food.lower()[0] + food.lower()[1]
            food_dict[letter] = food
    return food_dict

FOOD_CODE = get_food_code()



class Combo:
    def __init__(self, drink, entree, side):
        self.drink = drink
        self.entree = entree
        self.side = side
        self.price = 0

def main():
    print(FOOD_CODE)

if __name__ == "__main__":
    main()