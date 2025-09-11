# python
"""
backend/seed.py
Purpose:
    Create database tables from SQLAlchemy models, insert demo rows, and print them
    so you can demonstrate a working backend and retrieve sample data from the
    terminal.


"""

# Runtime flow (high-level, outside the docstring):
# 1) Load environment variables from `.env`.
# 2) Verify `DATABASE_URL` exists; exit with a message if missing.
# 3) Import SQLAlchemy engine, session factory and Base from `backend.database`.
# 4) Import `Word` model from `backend.models`.
# 5) Create database tables using `Base.metadata.create_all`.
# 6) Open a session, delete any existing demo rows (to avoid duplicates), insert demo rows, commit.
# 7) Query and print all `Word` rows for verification, then close the session.

import os
import sys
from dotenv import load_dotenv

load_dotenv()

if not os.getenv("DATABASE_URL"):
    print("DATABASE_URL not found.")
    sys.exit(1)

from backend.database import engine, SessionLocal, Base
from backend.models import Word

def init_db_and_seed():
    # Ensure tables exist
    Base.metadata.create_all(bind=engine)

    session = SessionLocal()
    try:
        # Remove existing demo rows with same 'word' values to make reruns safe
        session.query(Word).filter(Word.word.in_(["hello", "world", "test"])).delete(synchronize_session=False)

        demo_rows = [
            Word(word="hello", language="English", origin="Old English", history="Common greeting"),
            Word(word="world", language="English", origin="Old English", history="The earth or realm of human existence"),
            Word(word="test", language="English", origin="Latin", history="An examination or trial"),
        ]

        session.add_all(demo_rows)
        session.commit()

        # Print rows to demonstrate retrieval in terminal
        words = session.query(Word).all()
        for w in words:
            print(f"id={w.id} word={w.word} language={w.language} origin={w.origin} history={w.history}")
    finally:
        session.close()

if __name__ == "__main__":
    init_db_and_seed()