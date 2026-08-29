def madlib():
    print("=" * 50)
    print("      🏹 SURVIVAL CHALLENGE 🏹")
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
           🏹 THE ULTIMATE SURVIVAL 🏹
==================================================

{name}, a skilled {profession}, entered the legendary
Survival Arena located deep inside {place}. Only the
bravest adventurers had ever completed the challenge.

As the countdown reached {number}, a loud horn echoed
across the arena. Gates opened, revealing dense forests,
towering mountains, hidden caves, and dangerous rivers.

{name} quickly picked up a {color} {object_name} and
began to {verb} toward the nearest safe zone.

Along the journey, a fearless {animal} appeared and
became an unexpected companion. Together they crossed
broken bridges, climbed steep cliffs, and escaped
hidden traps.

After hours of exploring, they discovered a secret camp
filled with fresh {food}, clean water, and a mysterious
map leading to the final challenge.

The last obstacle was a giant stone gate protected by
ancient guardians. Using intelligence, courage, and
teamwork, {name} unlocked the gate and claimed the
Champion's Crystal.

As the crowd cheered, the arena lights illuminated the
sky. Everyone celebrated the incredible victory and
honored {name} as the most {adjective} champion in
the history of the Survival Arena.

🏆 CONGRATULATIONS!
You completed the Ultimate Survival Challenge!

==================== THE END ====================
"""

    print(story)


if __name__ == "__main__":
    madlib()