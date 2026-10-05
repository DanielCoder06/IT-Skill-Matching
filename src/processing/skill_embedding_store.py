import json
from pathlib import Path

import numpy as np

from src.processing.skill_embedding import encode_skill

BASE_DIR = Path(__file__).resolve().parents[2]
CACHE_PATH = BASE_DIR / "data" / "skill_embeddings.json"

def load_embedding_cache() -> dict:
    if not CACHE_PATH.exists():
        return {}

    with CACHE_PATH.open(
        "r",
        encoding="utf-8",
    ) as f:
        return json.load(f)

def save_embedding_cache(cache: dict) -> None:
    CACHE_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    with CACHE_PATH.open(
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(
            cache,
            f,
            ensure_ascii=False,
        )


def get_skill_embedding(skill: str) -> np.ndarray:
    cache = load_embedding_cache()

    if skill in cache:
        return np.array(
            cache[skill],
            dtype=np.float32,
        )

    vector = encode_skill(skill)

    cache[skill] = vector.tolist()

    save_embedding_cache(cache)

    return vector