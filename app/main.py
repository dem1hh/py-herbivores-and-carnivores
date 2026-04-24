class Animal:
    alive = []

    def __init__(self, name: str, health=100, hidden=False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return ("{" + f"Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}" + "}")


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, her_obj):
        if isinstance(her_obj,Herbivore) and not her_obj.hidden:
            her_obj.health -= 50
        if her_obj.health <= 0:
            Animal.alive.remove(her_obj)
