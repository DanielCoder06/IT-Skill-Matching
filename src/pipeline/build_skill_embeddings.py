import json

from src.processing.skill_embedding_store import (
    get_skill_embedding,
)


def load_skill_dictionary() -> dict:
    with open(
        "config/skills_dictionary.json",
        "r",
        encoding="utf-8-sig",
    ) as f:
        return json.load(f)


def main():
    dictionary = load_skill_dictionary()

    print("=== BUILD SKILL EMBEDDINGS ===")
    print(f"Canonical skills: {len(dictionary)}")

    for skill in dictionary:
        vector = get_skill_embedding(skill)

        print(
            f"{skill:25} -> "
            f"{len(vector)} dimensions"
        )

    print("\nEmbedding build completed.")


if __name__ == "__main__":
    main()