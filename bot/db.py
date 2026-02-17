import sqlite3
from pathlib import Path


def _db_path() -> Path:
    return Path(__file__).resolve().parent.parent / "school_data.db"


def init_db() -> None:
    path = _db_path()
    conn = sqlite3.connect(path)
    try:
        conn.execute(
            "CREATE TABLE IF NOT EXISTS students "
            "(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, "
            "age INTEGER NOT NULL, grade TEXT NOT NULL)"
        )
        conn.commit()
    finally:
        conn.close()


def insert_student(name: str, age: int, grade: str) -> int:
    path = _db_path()
    conn = sqlite3.connect(path)
    try:
        cur = conn.execute(
            "INSERT INTO students (name, age, grade) VALUES (?, ?, ?)",
            (name, age, grade),
        )
        conn.commit()
        return cur.lastrowid
    finally:
        conn.close()


def list_students(limit: int = 20) -> list[tuple]:
    path = _db_path()
    conn = sqlite3.connect(path)
    try:
        cur = conn.execute(
            "SELECT * FROM students ORDER BY id DESC LIMIT ?", (limit,)
        )
        return cur.fetchall()
    finally:
        conn.close()
