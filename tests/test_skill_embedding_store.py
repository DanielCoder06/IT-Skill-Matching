from src.processing.skill_embedding_store import (
    get_skill_embedding,
)


def test_skill_embedding_store():
    vector = get_skill_embedding("Python")

    assert vector.shape == (384,)

    vector_again = get_skill_embedding("Python")

    assert vector_again.shape == (384,)

    assert (vector == vector_again).all()