"""Some docstring"""


class Fighter:
    """
    Creates fighters.
    """
    def __init__(self, name, health, damage_per_attack):
        """
        Initializes field.
        """
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack

    def attack(self, opponent):
        """
        Attacks.
        """
        opponent.health -= self.damage_per_attack


class Fight:
    """
    Fight.
    """
    def __init__(self, fighter_1, fighter_2):
        """
        Initializes field.
        """
        self.fighter_1 = fighter_1
        self.fighter_2 = fighter_2
        self.winner = None

    def get_winner(self):
        """
        Gets winner.
        """
        while self.fighter_1.health > 0 and self.fighter_2.health > 0:
            self.fighter_1.attack(self.fighter_2)
            if self.fighter_2.health <= 0:
                self.winner = self.fighter_1.name
                break

            self.fighter_2.attack(self.fighter_1)
            if self.fighter_1.health <= 0:
                self.winner = self.fighter_2.name
                break

        return self.winner


fighter_tyler = Fighter("Tyler Derden", 100, 13)
fighter_narrator = Fighter("Narrator", 100, 13)

fight = Fight(fighter_tyler, fighter_narrator)
winner = fight.get_winner()

if winner:
    print(f"{winner} won the fight!")
