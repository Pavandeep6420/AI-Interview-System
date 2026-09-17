import sqlite3

DATABASE = "interview.db"


def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():

    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS interviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            role TEXT NOT NULL,
            difficulty TEXT NOT NULL,
            score REAL DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS answers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            interview_id INTEGER,
            question TEXT,
            answer TEXT,
            score REAL,
            feedback TEXT,
            analysis TEXT,
            FOREIGN KEY(interview_id) REFERENCES interviews(id)
        )
    """)

    # Add analysis column if old database already exists
    columns = conn.execute(
        "PRAGMA table_info(answers)"
    ).fetchall()

    column_names = [
        column["name"]
        for column in columns
    ]

    if "analysis" not in column_names:

        conn.execute(
            "ALTER TABLE answers ADD COLUMN analysis TEXT"
        )

    conn.commit()
    conn.close()