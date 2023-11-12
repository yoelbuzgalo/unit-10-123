import food_truck

def test_food_price_dict():
    # Setup
    expected_water_price = 2.00
    expected_pasta_price = 4.00
    expected_salad_price = 2.25

    # Invoke
    result_water = food_truck.FOOD_PRICES['Drink']['Water']
    result_pasta = food_truck.FOOD_PRICES['Entree']['Pasta']
    result_salad = food_truck.FOOD_PRICES['Side']['Salad']

    # Analysis
    assert result_water == expected_water_price
    assert result_pasta == expected_pasta_price
    assert result_salad == expected_salad_price

def test_food_code():
    # Setup
    expected_code = 'wa'

    # Invoke
    result_code = food_truck.FOOD_LETTER['Water']

    # Analysis
    assert expected_code == result_code

def test_menu_item_water():
    """
    Verify that menu item is implemented correctly (test once to see if class object is constructed correctly)
    """
    # Setup
    expected_letter = 'wa'
    expected_name = 'Water'
    expected_price = 2.00

    # Invoke
    result = food_truck.Menu_Item('wa', 'Water', 2.00)

    # Analysis
    assert result.letter == expected_letter
    assert result.name == expected_name
    assert result.price == expected_price

def test_menu_list_item_drink():
    """
    Verify that menu list is working as expected (drink category)
    """
    # Setup
    expected_item = food_truck.Menu_Item('wa', 'Water', 2.00)

    # Invoke
    result = food_truck.Menu().drink_list

    # Analysis
    assert result[0].letter == expected_item.letter
    assert result[0].name == expected_item.name
    assert result[0].price == expected_item.price

def test_menu_list_item_entree():
    """
    Verify that menu list is working as expected (entree category)
    """
    # Setup
    expected_item = food_truck.Menu_Item('pi', 'Pizza', 2.85)

    # Invoke
    result = food_truck.Menu().entree_list

    # Analysis
    assert result[1].letter == expected_item.letter
    assert result[1].name == expected_item.name
    assert result[1].price == expected_item.price

def test_menu_list_item_side():
    """
    Verify that menu list is working as expected (side category)
    """
    # Setup
    expected_item = food_truck.Menu_Item('co', 'Cornbread', 1.00)

    # Invoke
    result = food_truck.Menu().side_list

    # Analysis
    assert result[2].letter == expected_item.letter
    assert result[2].name == expected_item.name
    assert result[2].price == expected_item.price

def test_order_combo():
    """
    Verify that order combo function is working as expected
    """
    # Setup
    menu = food_truck.Menu()
    expected_drink = menu.drink_list[0]
    expected_entree = menu.entree_list[0]
    expected_side = menu.side_list[0]
    expected_price = (2+3.5+1.20)

    # Invoke
    result = food_truck.order_combo(menu, 'wa','bu','fr')

    assert expected_drink == result.drink
    assert expected_entree == result.entree
    assert expected_side == result.side
    assert expected_price == result.price