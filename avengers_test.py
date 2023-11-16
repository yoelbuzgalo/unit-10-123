import avengers

def test_superhero_batman():
    # Setup
    expected_name = "Batman"
    expected_identity = "Bruce Wayne"
    expected_powers = ['Grappling', 'Punching']
    expected_weapons = ['Grappling gun', 'Batarangs']

    # Invoke
    result = avengers.Superhero("Batman", "Bruce Wayne", ['Grappling', 'Punching'], ['Grappling gun', 'Batarangs'])

    # Analysis
    assert result.name == expected_name
    assert result.identity == expected_identity
    assert result.powers[1] == expected_powers[1]
    assert result.weapons[1] == expected_weapons[1]
