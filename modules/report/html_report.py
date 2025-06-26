# 📁 report/html_report.py
from jinja2 import Environment, FileSystemLoader
import os

def generate_html_report(data, template_name="report_template.html", output_path="results/report.html"):
    env = Environment(loader=FileSystemLoader("report/templates"))
    template = env.get_template(template_name)
    html_content = template.render(data)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        f.write(html_content)

    print(f"[+] HTML report saved to {output_path}")
    return html_content
