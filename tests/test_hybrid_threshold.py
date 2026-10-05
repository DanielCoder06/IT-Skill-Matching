from sentence_transformers import util

from src.processing.skill_embedding import encode_skill


MATCH_PAIRS = [
    ("ReactJS", "React"),
    ("Postgres", "PostgreSQL"),
    ("JS", "JavaScript"),
    ("Python3", "Python"),
    ("nodejs", "Node.js"),
    ("Vue", "Vue.js"),
    ("K8s", "Kubernetes"),
    ("ML", "Machine Learning"),
    ("TS", "TypeScript"),
    ("sklearn", "scikit-learn"),
]

NON_MATCH_PAIRS = [
    ("Python", "Java"),
    ("Docker", "Kubernetes"),
    ("Python", "PostgreSQL"),
    ("JavaScript", "Java"),
    ("React", "Docker"),
    ("Python", "Machine Learning"),
    ("SQL", "Docker"),
    ("PostgreSQL", "Kubernetes"),
]


def test_hybrid_threshold_evaluation():
    print("\n=== HYBRID THRESHOLD EVALUATION ===")

    print("\n--- EXPECTED MATCH ---")

    for skill_a, skill_b in MATCH_PAIRS:
        vector_a = encode_skill(skill_a)
        vector_b = encode_skill(skill_b)

        similarity = util.cos_sim(
            vector_a,
            vector_b,
        ).item()

        print(
            f"MATCH    | "
            f"{skill_a:20} <-> "
            f"{skill_b:25} | "
            f"{similarity:.4f}"
        )

    print("\n--- EXPECTED NON-MATCH ---")

    for skill_a, skill_b in NON_MATCH_PAIRS:
        vector_a = encode_skill(skill_a)
        vector_b = encode_skill(skill_b)

        similarity = util.cos_sim(
            vector_a,
            vector_b,
        ).item()

        print(
            f"NO MATCH | "
            f"{skill_a:20} <-> "
            f"{skill_b:25} | "
            f"{similarity:.4f}"
        )
