def madlib():
    print("=" * 50)
    print("         🧟 ZOMBIE SURVIVAL 🧟")
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
           🧟 THE ZOMBIE APOCALYPSE 🧟
==================================================

{name}, a brave {profession}, arrived at the abandoned
city of {place} to investigate a mysterious signal.

Suddenly, the sky turned {color}, and loud sirens echoed
through the streets. Hundreds of zombies emerged from the
shadows, slowly surrounding the city.

Holding only a {object_name}, {name} decided to {verb}
through the deserted buildings in search of a safe place.

During the journey, a loyal {animal} appeared and guided
{name} through hidden underground tunnels. Together, they
avoided dangerous traps and escaped countless zombies.

After several hours, they found a secure laboratory where
scientists had stored enough {food} and emergency supplies
to survive for {number} days.

Just as everything seemed safe, the zombies broke through
the entrance. Thinking quickly, {name} activated the city's
emergency defense system, sealing every exit.

The rescue helicopter finally arrived at sunrise. {name}
and the brave {animal} escaped safely while the zombies
were trapped inside the city forever.

The world celebrated the successful mission, and {name}
became known as the most {adjective} survivor in history.

🏆 MISSION SUCCESSFUL!
The city was saved, and a new adventure awaits...

==================== THE END ====================
"""

    print(story)


if __name__ == "__main__":
    madlib()