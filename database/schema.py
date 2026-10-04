from database.connection import get_connection


def create_tables() -> None:
    connection = get_connection()

    connection.executescript(
        """
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            source TEXT NOT NULL,
            external_id TEXT,

            title TEXT NOT NULL,
            company TEXT,
            location TEXT,

            description TEXT NOT NULL,

            job_url TEXT NOT NULL UNIQUE,

            posted_date TEXT,
            employment_type TEXT,
            experience TEXT,
            remote INTEGER,

            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        );

        CREATE INDEX IF NOT EXISTS idx_jobs_source
        ON jobs(source);

        CREATE INDEX IF NOT EXISTS idx_jobs_posted_date
        ON jobs(posted_date);
        
        CREATE TABLE IF NOT EXISTS skills (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            name TEXT NOT NULL UNIQUE,

            category TEXT,

            created_at TEXT NOT NULL
        );

        CREATE INDEX IF NOT EXISTS idx_skills_category
        ON skills(category);
        
        CREATE TABLE IF NOT EXISTS job_skills (
            job_id INTEGER NOT NULL,
            skill_id INTEGER NOT NULL,
            source TEXT NOT NULL,

            PRIMARY KEY (job_id, skill_id),

            FOREIGN KEY (job_id)
                REFERENCES jobs(id)
                ON DELETE CASCADE,

            FOREIGN KEY (skill_id)
                REFERENCES skills(id)
                ON DELETE CASCADE
        );

        CREATE INDEX IF NOT EXISTS idx_job_skills_skill
        ON job_skills(skill_id);

        CREATE INDEX IF NOT EXISTS idx_job_skills_job
        ON job_skills(job_id);
        """
    )

    connection.commit()
    connection.close()


if __name__ == "__main__":
    create_tables()
    print("Database schema created.")