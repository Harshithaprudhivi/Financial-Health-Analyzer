from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from report_generator import create_pdf_report
from fastapi.responses import FileResponse
import pandas as pd
from metrics import calculate_metrics_from_df
from risk_analyzer import analyze_risk
import io
import traceback

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        df = pd.read_csv(io.BytesIO(contents))

        print("=== RAW COLUMNS ===")
        print(df.columns)

        df.columns = df.columns.str.strip().str.lower()

        print("=== CLEANED COLUMNS ===")
        print(df.columns)

        summary = calculate_metrics_from_df(df)
        risk = analyze_risk(summary)

        return {
            "summary": summary,
            "risk_analysis": risk
        }

    except Exception as e:
        print("🔥 ERROR OCCURRED 🔥")
        traceback.print_exc()
        return {"error": str(e)}

@app.post("/generate-report")
async def generate_report(file: UploadFile = File(...)):
    contents = await file.read()
    df = pd.read_csv(io.BytesIO(contents))
    df.columns = df.columns.str.strip().str.lower()

    summary = calculate_metrics_from_df(df)
    risk = analyze_risk(summary)

    create_pdf_report(summary, risk, "financial_report.pdf")

    return FileResponse("financial_report.pdf", media_type="application/pdf", filename="financial_report.pdf")
