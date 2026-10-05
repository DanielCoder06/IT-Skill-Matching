from src.processing.skill_matcher import (
    exact_skill_match,
    semantic_skill_match,
    hybrid_skill_match,
)

def test_exact_skill_match():
    result = exact_skill_match(
        ["Python", "PostgreSQL", "React"],
        ["Python", "PostgreSQL", "Docker"],
    )

    assert result["matched"] == [
        "PostgreSQL",
        "Python",
    ]

    assert result["missing"] == [
        "Docker",
    ]

    assert result["coverage"] == 2 / 3
    
def test_semantic_skill_match():
    result = semantic_skill_match(
        ["ReactJS", "Postgres"],
        ["React", "PostgreSQL"],
    )

    assert len(result) == 4

    assert result[0]["similarity"] >= result[-1]["similarity"]
    
def test_hybrid_skill_match():
    result = hybrid_skill_match(
        ["Python", "ReactJS", "Postgres"],
        ["Python", "React", "PostgreSQL", "Docker"],
    )

    assert "Python" in result["matched"]

    assert "Docker" in result["missing"]

    assert result["coverage"] >= 0.25

    assert len(result["semantic_matches"]) >= 1