from sample_madlibs import treasure_hunt, wizard_quest, zombie_apocalypse, survival_challenge
import random

if __name__ == "__main__":
    m = random.choice([treasure_hunt, wizard_quest, zombie_apocalypse, survival_challenge])
    m.madlib()