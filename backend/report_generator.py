from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf_report(summary, risk, file_path="financial_report.pdf"):
    doc = SimpleDocTemplate(file_path)
    styles = getSampleStyleSheet()
    elements = []

    title = "SME Financial Health Report"
    elements.append(Paragraph(title, styles['Title']))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("<b>Financial Summary</b>", styles['Heading2']))
    for key, value in summary.items():
        line = f"{key.replace('_',' ').title()}: {round(value,2)}"
        elements.append(Paragraph(line, styles['Normal']))

    elements.append(Spacer(1, 12))
    elements.append(Paragraph("<b>Credit Assessment</b>", styles['Heading2']))
    elements.append(Paragraph(f"Credit Score: {risk['credit_score']}", styles['Normal']))
    elements.append(Paragraph(risk['credit_status'], styles['Normal']))

    elements.append(Spacer(1, 12))
    elements.append(Paragraph("<b>Risks Identified</b>", styles['Heading2']))
    for r in risk['risks']:
        elements.append(Paragraph(f"- {r}", styles['Normal']))

    elements.append(Spacer(1, 12))
    elements.append(Paragraph("<b>Recommendations</b>", styles['Heading2']))
    for rec in risk['recommendations']:
        elements.append(Paragraph(f"- {rec}", styles['Normal']))

    doc.build(elements)
