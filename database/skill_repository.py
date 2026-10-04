from datetime import datetime, timezone
from database.connection import get_connection

def _now() -> str:
    return datetime.now(timezone.utc).isoformat()

def get_skill_by_name(name: str) -> dict | None:
    connection = get_connection()

    row = connection.execute(
        """
        SELECT *
        FROM skills
        WHERE name = ?
        """,
        (name,),
    ).fetchone()
     
    connection.close()
    
    if row is None:
        return None
    return dict(row)

def create_skill(name: str, category: str | None = None) -> int:
    connection = get_connection()
    
    existing = connection.execute(
        """
        SELECT id
        FROM skills
        WHERE name = ?
        """,
        (name,),
    ).fetchone()
    
    if existing is not None:
        connection.close()
        return int(existing["id"])
    cursor = connection.execute(
        """
        INSERT INTO skills (
            name,
            category,
            created_at
        )
        VALUES (?, ?, ?)
        """,
        (
            name,
            category,
            _now(),
        ),
    )

    connection.commit()

    skill_id = cursor.lastrowid

    connection.close()

    return int(skill_id)

def get_all_skills() -> list[dict]:
    connection = get_connection()
    
    rows = connection.execute(
        """ 
        SELECT *
        FROM skills
        ORDER BY id
        """
    ).fetchall()
    
    connection.close()
    return [dict(row) for row in rows]