import json
from pathlib import Path

from database.skill_repository import create_skill

DICTIONARY_PATH = Path( "config/skills_dictionary.json")

def main():
    with DICTIONARY_PATH.open(
        "r",
        encoding="utf-8-sig",
    ) as f:
        skills_dictionary = json.load(f)

    created = 0

    for skill_name in skills_dictionary:
        skill_id = create_skill(skill_name)

        print(
            f"Skill: {skill_name} "
            f"-> ID: {skill_id}"
        )

        created += 1

    print()
    print(f"Skills processed: {created}")


if __name__ == "__main__":
    main()