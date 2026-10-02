import json
import re
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]
DICTIONARY_PATH = BASE_DIR / "config" / "skills_dictionary.json"


def load_skill_dictionary():
    with DICTIONARY_PATH.open(
        "r",
        encoding="utf-8-sig",
    ) as f:
        return json.load(f)


def extract_skills(text: str) -> list[str]:
    dictionary = load_skill_dictionary()

    text_lower = text.lower()
    found = []

    for skill, aliases in dictionary.items():
        for alias in aliases:
            pattern = rf"(?<!\w){re.escape(alias.lower())}(?!\w)"

            if re.search(pattern, text_lower):
                found.append(skill)
                break

    return found
