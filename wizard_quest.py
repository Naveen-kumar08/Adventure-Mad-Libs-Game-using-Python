def madlib():
    print("=" * 50)
    print("         🪄 WIZARD ADVENTURE 🪄")
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
            🏰 THE MAGIC QUEST 🏰
==================================================

{name}, a young {profession}, received a mysterious letter
inviting them to the legendary Wizard Academy in {place}.

On the very first day, the Headmaster announced that a
powerful magical {object_name} had been stolen. Without it,
the entire kingdom was in danger.

Armed with a glowing {color} wand, {name} began searching
through enchanted forests, secret tunnels, and ancient
castles.

Along the journey, a loyal {animal} joined the adventure.
Together they had to {verb} across floating bridges,
solve magical riddles, and escape dangerous creatures.

After many challenges, they discovered the hidden chamber
where the legendary {object_name} was protected by an
ancient dragon.

Using courage and intelligence, {name} recovered the magical
artifact and returned it safely to the academy.

To celebrate the victory, everyone enjoyed a grand feast
filled with delicious {food}. Fireworks lit up the sky for
{number} minutes.

The Headmaster smiled and declared,

"From this day forward, {name} will always be remembered as
the most {adjective} wizard our academy has ever seen!"

🏆 MAGIC MISSION COMPLETE!
==================================================
"""

    print(story)


if __name__ == "__main__":
    madlib()