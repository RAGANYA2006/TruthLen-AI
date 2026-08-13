from flask import Flask, request, jsonify
from flask_cors import CORS

import joblib
import os

from database import (
    save_analysis,
    get_all_analyses
)

from export_excel import (
    export_to_excel
)


# ==========================================
# FLASK APP
# ==========================================

app = Flask(__name__)

CORS(app)


# ==========================================
# BASE DIRECTORY
# ==========================================

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)


# ==========================================
# MODEL PATHS
# ==========================================

MODEL_PATH = os.path.join(
    BASE_DIR,
    "fake_news_model.pkl"
)

VECTORIZER_PATH = os.path.join(
    BASE_DIR,
    "tfidf_vectorizer.pkl"
)


# ==========================================
# LOAD TRAINED MODEL
# ==========================================

print("Loading trained model...")

model = joblib.load(
    MODEL_PATH
)

vectorizer = joblib.load(
    VECTORIZER_PATH
)

print(
    "Model loaded successfully!"
)

print(
    "Vectorizer loaded successfully!"
)


# ==========================================
# HOME ROUTE
# ==========================================

@app.route("/", methods=["GET"])
def home():

    return jsonify({

        "message":
            "Fake News Detection Backend is running!",

        "model":
            "Logistic Regression",

        "database":
            "SQLite",

        "excel":
            "Enabled",

        "status":
            "ready"

    })


# ==========================================
# PREDICT NEWS
# ==========================================

@app.route(
    "/predict",
    methods=["POST"]
)
def predict():

    try:

        # ----------------------------------
        # GET JSON DATA
        # ----------------------------------

        data = request.get_json()

        if not data:

            return jsonify({

                "error":
                    "No data received"

            }), 400


        # ----------------------------------
        # GET NEWS TEXT
        # ----------------------------------

        news_text = data.get(
            "text",
            ""
        ).strip()


        if not news_text:

            return jsonify({

                "error":
                    "News text is required"

            }), 400


        # ----------------------------------
        # CONVERT TEXT TO TF-IDF
        # ----------------------------------

        text_vector = vectorizer.transform(
            [news_text]
        )


        # ----------------------------------
        # PREDICTION
        # ----------------------------------

        prediction = model.predict(
            text_vector
        )[0]


        # ----------------------------------
        # CONFIDENCE
        # ----------------------------------

        probabilities = model.predict_proba(
            text_vector
        )[0]

        confidence = (
            max(probabilities) * 100
        )


        # ----------------------------------
        # CONVERT LABEL
        # ----------------------------------

        if prediction == 0:

            result = "FAKE"

        else:

            result = "REAL"


        confidence = round(
            confidence,
            2
        )


        # ----------------------------------
        # SAVE TO SQLITE DATABASE
        # ----------------------------------

        save_analysis(

            news_text,

            result,

            confidence

        )


        # ----------------------------------
        # UPDATE EXCEL REPORT
        # ----------------------------------

        excel_status = export_to_excel()


        # ----------------------------------
        # RETURN RESULT TO FRONTEND
        # ----------------------------------

        return jsonify({

            "prediction":
                result,

            "confidence":
                confidence,

            "message":
                "News analyzed successfully",

            "database_saved":
                True,

            "excel_updated":
                excel_status

        })


    except Exception as e:

        print(
            "Prediction error:",
            e
        )

        return jsonify({

            "error":
                str(e)

        }), 500


# ==========================================
# ANALYSIS HISTORY
# ==========================================

@app.route(
    "/history",
    methods=["GET"]
)
def history():

    try:

        analyses = get_all_analyses()


        return jsonify({

            "success":
                True,

            "count":
                len(analyses),

            "analyses":
                analyses

        })


    except Exception as e:

        print(
            "History error:",
            e
        )

        return jsonify({

            "error":
                str(e)

        }), 500


# ==========================================
# EXPORT EXCEL MANUALLY
# ==========================================

@app.route(
    "/export",
    methods=["GET"]
)
def export():

    try:

        success = export_to_excel()


        if success:

            return jsonify({

                "success":
                    True,

                "message":
                    "Excel report created successfully!",

                "file":
                    "analysis_reports.xlsx"

            })


        return jsonify({

            "success":
                False,

            "message":
                "Excel export failed"

        }), 500


    except Exception as e:

        return jsonify({

            "success":
                False,

            "error":
                str(e)

        }), 500


# ==========================================
# RUN SERVER
# ==========================================

if __name__ == "__main__":

    app.run(

        debug=True,

        port=5000

    )