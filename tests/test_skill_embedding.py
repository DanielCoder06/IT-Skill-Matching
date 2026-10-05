import json
from pathlib import Path

from sentence_transformers import util

from src.processing.skill_embedding import encode_skill


BASE_DIR = Path(__file__).resolve().parents[1]
DICTIONARY_PATH = BASE_DIR / "config" / "skills_dictionary.json"


def load_dictionary():
    with DICTIONARY_PATH.open(
        "r",
        encoding="utf-8-sig",
    ) as f:
        return json.load(f)


def test_skill_alias_similarity():
    dictionary = load_dictionary()

    print("\n=== SKILL ALIAS SIMILARITY ===")
    print(f"Canonical skills: {len(dictionary)}")

    for skill, aliases in dictionary.items():
        skill_vector = encode_skill(skill)

        print(f"\n[{skill}]")

        for alias in aliases:
            if alias.lower() == skill.lower():
                continue

            alias_vector = encode_skill(alias)

            similarity = util.cos_sim(
                skill_vector,
                alias_vector
            ).item()

            print(
                f"  {alias:30} -> "
                f"{similarity:.4f}"
            )