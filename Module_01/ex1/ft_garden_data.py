#!/usr/bin/python3

# --- globals ---

intro_str = "=== Garden Plant Registry ==="
outro_str = "\n=== End of Program ==="

height_suf = "cm"
age_suf = " days old"

# --- class ---


class Plant:

    """
    It's a plant
    """

    name: str
    height: int
    age: int

    def __init__(self, name="42 plant", height=42, age=42):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}, {self.height}{height_suf}, {self.age}{age_suf}")

# ---main ---


def main():

    print(intro_str)
    plant0 = Plant(
        name="Rose",
        height=25,
        age=30)
    plant1 = Plant(
        name="Sunflower",
        height=80,
        age=45)
    plant2 = Plant(
        name="Cactus",
        height=15,
        age=120)
    print(intro_str)
    plant0.show()
    plant1.show()
    plant2.show()
    print(outro_str)

# ---run ---


if __name__ == '__main__':

    main()
