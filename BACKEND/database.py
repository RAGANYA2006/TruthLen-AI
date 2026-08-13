import sqlite3
import os
from datetime import datetime


# ==========================================
# DATABASE PATH
# ==========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASE_PATH = os.path.join(
    BASE_DIR,
    "fake_news.db"
)


# ==========================================
# CREATE DATABASE AND TABLE
# ==========================================

def create_database():

    connection = sqlite3.connect(DATABASE_PATH)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS analyses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            news_text TEXT NOT NULL,
            prediction TEXT NOT NULL,
            confidence REAL NOT NULL,
            analyzed_at TEXT NOT NULL
        )
    """)

    connection.commit()

    connection.close()


# ==========================================
# SAVE ANALYSIS
# ==========================================

def save_analysis(
    news_text,
    prediction,
    confidence
):

    connection = sqlite3.connect(
        DATABASE_PATH
    )

    cursor = connection.cursor()

    analyzed_at = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    cursor.execute("""
        INSERT INTO analyses
        (
            news_text,
            prediction,
            confidence,
            analyzed_at
        )
        VALUES (?, ?, ?, ?)
    """, (
        news_text,
        prediction,
        confidence,
        analyzed_at
    ))

    connection.commit()

    connection.close()


# ==========================================
# GET ALL ANALYSES
# ==========================================

def get_all_analyses():

    connection = sqlite3.connect(
        DATABASE_PATH
    )

    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM analyses
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    connection.close()

    return [dict(row) for row in rows]


# ==========================================
# CREATE DATABASE AUTOMATICALLY
# ==========================================

create_database()