import json
from pathlib import Path

from sentence_transformers import util

from src.processing.skill_embedding import encode_skill


BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = BASE_DIR / "tests" / "data" / "skill_similarity_eval.json"


def load_evaluation_data():
    with DATA_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)


def test_skill_similarity_evaluation():
    data = load_evaluation_data()

    print("\n=== SKILL SIMILARITY EVALUATION ===")

    for item in data:
        cv_skill = item["cv_skill"]
        job_skill = item["job_skill"]
        label = item["label"]

        cv_vector = encode_skill(cv_skill)
        job_vector = encode_skill(job_skill)

        similarity = util.cos_sim(
            cv_vector,
            job_vector,
        ).item()

        expected = "MATCH" if label == 1 else "NO MATCH"

        print(
            f"{expected:8} | "
            f"{cv_skill:20} <-> "
            f"{job_skill:25} | "
            f"{similarity:.4f}"
        )