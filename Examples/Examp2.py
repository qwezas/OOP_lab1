from typing import Optional


class Ship:
    def __init__(self, name: str, capacity: float) -> None:
        self.name: str = name
        self.capacity: float = capacity
        self.cargo: float = 0
        self.captain: Optional[str] = None  # Может быть None пока не назначен

    def name_captain(self, cap: str) -> None:
        self.captain = cap
        print("{} is the captain of the {}".format(self.captain, self.name))

    def load_cargo(self, weight: float) -> None:
        if self.cargo + weight <= self.capacity:
            self.cargo += weight
            print("Loaded {} tons".format(weight))
        else:
            print("Cannot load that much")

    def unload_cargo(self, weight: float) -> None:
        if self.cargo - weight >= 0:
            self.cargo -= weight
            print("Unloaded {} tons".format(weight))
        else:
            print("cannot unload that much")
