from collections import Counter

from database.connection import get_connection
from src.extractor.regex_extractor import extract_skills

def main():
    connection =  get_connection()
    
    rows = connection.execute(
    """SELECT id, title, company, description
    FROM jobs
    ORDER BY id
    """
    ).fetchall()
    
    connection.close()
    
    skill_counter = Counter()
    
    for row in rows:
        skills = extract_skills(row["description"])
        for skill in skills:
            skill_counter[skill] += 1
            
    print(f"Jobs analyzed: {len(rows)}")
    print(f"Unique skills found: {len(skill_counter)}")

    print("\n=== SKILL FREQUENCY ===")

    for skill, count in skill_counter.most_common():
        print(f"{skill}: {count}")


if __name__ == "__main__":
    main()