import food_truck

def test_combo_class():
    # Setup
    expected_drink = 'Water'
    expected_entree = 'Burger'
    expected_side = 'Fries'

    # Invoke
    result = food_truck.Combo('Water', 'Burger', 'Fries')

    # Analysis:
    assert result.drink == expected_drink
    assert result.entree == expected_entree
    assert result.side == expected_side

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
    expected_code = 'Water'

    # Invoke
    result_code = food_truck.FOOD_CODE['wa']

    # Analysis
    assert expected_code == result_code