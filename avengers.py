class Avengers:
    __slots__ = ['team', 'leader']
    def __init__(self, superheroes, leader):
        # Initialize self variables
        self.team = [] # List of superheroes
        self.leader = leader
        # Check whether if superheroes is passed or not, if it is then make a copy and append to the team list
        if len(superheroes) > 0:
            for superhero in superheroes:
                self.team.append(superhero)

class Superhero:
    __slots__ = ['name', 'identity', 'powers', 'weapons']
    def __init__(self, name, identity, powers, weapons):
        self.name = name
        self.identity = identity
        self.powers = [] # List of powers
        self.weapons = [] # List of weapons

        # Check whether if powers is passed or not, if it is then make a copy and append to the powers list
        if len(powers) > 0:
            for power in powers:
                self.powers.append(power)
        # Check whether if weapons is passed or not, if it is then make a copy and append to the weapons list
        if len(weapons) > 0:
            for weapon in weapons:
                self.weapons.append(weapon)
