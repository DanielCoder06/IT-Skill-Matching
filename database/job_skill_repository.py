from database.connection import get_connection

def add_job_skill(
    job_id: int, 
    skill_id: int, 
    source: str = "regex",
) -> None:
    connection = get_connection()
    connection.execute(
        """
        INSERT OR IGNORE INTO job_skills (
            job_id, skill_id, source
        )
        VALUES (?, ?, ?)
        """,
        (
            job_id,
            skill_id,
            source,
        ),
    )
    connection.commit()
    connection.close()
    
def get_skills_by_job(job_id: int,) -> list[dict]:
    connection = get_connection()
    
    rows = connection.execute(
        """ 
        SELECT
            s.id,
            s.name,
            js.source
        FROM job_skills js
        JOIN skills s
            ON s.id = js.skill_id
        WHERE js.job_id = ?
        ORDER BY s.name
        """,
         (job_id,),
    ).fetchall()
    connection.close()
    return [dict(row) for row in rows]

def get_jobs_by_skill(skill_id: int,) -> list[dict]:
    connection = get_connection()
      
    rows = connection.execute(
        """ 
        SELECT
            j.id,
            j.title,
            j.company,
            js.source
        FROM job_skills js
        JOIN jobs j
            ON j.id = js.job_id
        WHERE js.skill_id = ?
        ORDER BY j.id
        """,
        (skill_id,),
    ).fetchall()
    connection.close()
    return [dict(row) for row in rows]