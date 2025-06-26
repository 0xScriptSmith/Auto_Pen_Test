# 📁 report/pdf_report.py
from weasyprint import HTML
import os

def generate_pdf_report(html_content, output_path="results/report.pdf"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    HTML(string=html_content).write_pdf(output_path)
    print(f"[+] PDF report saved to {output_path}")
