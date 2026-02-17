import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from bot.db import list_students

rows = list_students()
if rows:
    for row in rows:
        print(f"id={row[0]}, name={row[1]}, age={row[2]}, grade={row[3]}")
else:
    print("Таблица students пуста.")
