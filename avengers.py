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
    def __init__(self, name, identity, powers=None, weapons=None):
        self.name = name
        self.identity = identity
        self.powers = [] # List of powers
        self.weapons = [] # List of weapons

        # Check whether if powers is passed or not, if it is then make a copy and append to the powers list
        if powers is not None and len(powers) > 0:
            for power in powers:
                self.powers.append(power)
        # Check whether if weapons is passed or not, if it is then make a copy and append to the weapons list
        if weapons is not None and len(weapons) > 0:
            for weapon in weapons:
                self.weapons.append(weapon)

def create_avengers_team():
    """
    This function creates an avengers team by calling and initializing class objects
    """
    thor = Superhero('Thor', 'Thor Odinson', ['Superhuman', 'Control Over Lightning', 'Longevity'], ['Mjolnir (Hammer)'])
    black_widow = Superhero('Black Widow', 'Natasha Romanoff', ['Expert Martial Artist', 'Exceptional Spy and Tactician'], ['Widow\'s Bite'])
    captain_america = Superhero('Captain America', 'Steve Rogers', ['Enhanced Strength', 'Agility', 'Endurance'], ['Vibranium Shield', 'Firearms'])
    scarlet_witch = Superhero('Scarlet Witch', 'Wanda Maximoff', ['Reality Manipulation', 'Energy Projection'])

    superheroes = [thor, black_widow, captain_america, scarlet_witch]

    avenger_team = Avengers(superheroes, captain_america)

    return avenger_team

def print_superhero_bio(a_superhero, leader=False):
    """
    Helper function to print a superhero's bio in an organized way
    """

    # If the superhero is marked as leader, print a tag before its name
    if leader:
        print("[Leader] ", a_superhero.name, "(", a_superhero.identity,")", ":", sep="")
    else: # Otherwise print normally
        print(a_superhero.name, "(", a_superhero.identity,")", ":", sep="")
    
    if len(a_superhero.powers) > 0:
        print("Abilities")
        for power in a_superhero.powers:
            print("\t",power, sep="")
    if len(a_superhero.weapons) > 0:
        print("Weapons")
        for weapon in a_superhero.weapons:
            print("\t",weapon,sep="")

def print_member(an_avenger, name):
    """
    This function calls and prints a specific member matching the name and its own bio, also determines whether if the member is a leader or not
    """
    for avenger in an_avenger.team:
        if avenger.name == an_avenger.leader.name:
            print("Leader Bio:", end="\n\n")
            print_superhero_bio(avenger) # It is on purpose that I am not putting 'True' as leader parameter since I want it to print 'Leader Bio:' before it without [Leader] tag
            break
        elif avenger.name == name:
            print("Found Avenger Bio: ", end="\n\n")
            print_superhero_bio(avenger)
            break
    print("\n")

def print_roster(an_avenger):
    """
    This function prints the roster of the avengers team and marks its leader
    """
    print("[Leader]", an_avenger.leader.name) # Prints the leader in first line
    for avenger in an_avenger.team:
        if avenger.name == an_avenger.leader.name:
            continue # Skips current iteration
        print(avenger.name)

def print_roster_with_bio(an_avenger):
    print_superhero_bio(an_avenger.leader, True)
    for avenger in an_avenger.team:
        if avenger.name == an_avenger.leader.name:
            continue # Skips current iteration
        print_superhero_bio(avenger, False)
        print()

def main():
    avengers_team = create_avengers_team()

    # Testing whether if it printed an individual member's bio correctly
    print_member(avengers_team, 'Black Widow')
    print_member(avengers_team, 'Captain America')

    # Testing whether if it printed roster without bio correctly
    print_roster(avengers_team)

    # Testing whether if it printed roster with bio correctly
    print_roster_with_bio(avengers_team)
    

if __name__ == "__main__":
    main()
