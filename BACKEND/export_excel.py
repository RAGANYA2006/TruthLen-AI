import sqlite3
import pandas as pd
import os


# ==========================================
# PATHS
# ==========================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

DATABASE_PATH = os.path.join(
    BASE_DIR,
    "fake_news.db"
)

EXCEL_PATH = os.path.join(
    BASE_DIR,
    "analysis_reports.xlsx"
)


# ==========================================
# EXPORT DATABASE TO EXCEL
# ==========================================

def export_to_excel():

    try:

        connection = sqlite3.connect(
            DATABASE_PATH
        )

        df = pd.read_sql_query(
            """
            SELECT
                id,
                news_text,
                prediction,
                confidence,
                analyzed_at
            FROM analyses
            ORDER BY id DESC
            """,
            connection
        )

        connection.close()

        df.to_excel(
            EXCEL_PATH,
            index=False
        )

        print(
            "Excel report updated successfully!"
        )

        return True

    except Exception as e:

        print(
            "Excel export error:",
            e
        )

        return False