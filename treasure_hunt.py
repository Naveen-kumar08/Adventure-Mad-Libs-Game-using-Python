def madlib():
    print("=" * 50)
    print("        🏴‍☠️ TREASURE HUNT ADVENTURE 🏴‍☠️")
    print("=" * 50)

    name = input("Name: ")
    place = input("Place: ")
    animal = input("Animal: ")
    food = input("Food: ")
    color = input("Color: ")
    adjective = input("Adjective: ")
    object_name = input("Object: ")
    profession = input("Profession: ")
    verb = input("Verb: ")
    number = input("Number: ")

    story = f"""
==================================================
               THE LOST TREASURE 
==================================================

{name}, a brave {profession}, received an old treasure map
leading to the mysterious land of {place}. Legends said that
a priceless treasure had been hidden there for over {number}
years.

Carrying only a {color} {object_name}, {name} entered the
ancient jungle. Suddenly, a giant {animal} appeared from the
bushes. Instead of attacking, it quietly guided {name}
toward a forgotten cave.

Inside the cave were strange symbols, glowing crystals,
and several hidden traps. Using quick thinking, {name}
managed to {verb} past every obstacle.

Deep inside the cave, a huge treasure chest waited beneath
a waterfall. When it was finally opened, it was filled with
gold, sparkling jewels, and delicious {food} prepared by
the island's ancient guardians.

As {name} stepped outside, the sun lit up the entire island,
revealing a breathtaking view. Everyone celebrated the
successful adventure, calling {name} the most {adjective}
explorer of all time.

The mysterious map disappeared forever, leaving behind only
the unforgettable memories of the greatest treasure hunt
ever discovered.

   ADVENTURE COMPLETE!
==================================================
"""

    print(story)


if __name__ == "__main__":
    madlib()