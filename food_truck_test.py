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