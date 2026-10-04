from database.connection import get_connection
from database.job_skill_repository import add_job_skill
from src.extractor.regex_extractor import extract_skills

def main() -> None:
    connection = get_connection()
    
    jobs = connection.execute(
        """
        SELECT id, title, description
        FROM jobs
        ORDER BY id
        """        
    ).fetchall()
    
    processed_jobs = 0
    jobs_with_skills = 0
    relations_created = 0
    skills_not_found = 0
    
    for job in jobs:
        processed_jobs += 1
        
        skills = extract_skills(job["description"])

        if not skills:
            continue

        jobs_with_skills += 1
        
        for skill_name in skills:
            skill_row = connection.execute(
                """
                SELECT id
                FROM skills
                WHERE name = ?
                """,
                (skill_name,), 
            ).fetchone()
            
            if skill_row is None:
                skills_not_found += 1
                print(f"Skill not found: {skill_name}")
                continue
            
            skill_id = skill_row["id"]
            
            before = connection.execute(
                """
                SELECT 1
                FROM job_skills
                WHERE job_id = ?
                  AND skill_id = ?
                """,
                (job["id"], skill_id),               
            ).fetchone()
            
            add_job_skill(
                job_id=job["id"],
                skill_id=skill_id,
                source="regex",
            )
            
            if before is None:
                relations_created += 1
            
    connection.close()
            
    print(f"Jobs processed: {processed_jobs}")
    print(f"Jobs with skills: {jobs_with_skills}")
    print(f"Relation created: {relations_created}")
    print(f"Skills not found: {skills_not_found}")


if __name__ == "__main__":
    main()            