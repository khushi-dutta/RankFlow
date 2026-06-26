import os
from jinja2 import Template

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>SEO & AEO Pipeline Report</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background-color: #f9f9f9; }
        .container { background-color: #fff; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }
        h1, h2 { color: #333; }
        .score-board { display: flex; gap: 20px; margin-bottom: 30px; }
        .score-card { padding: 20px; border-radius: 8px; text-align: center; flex: 1; color: white; font-size: 24px; font-weight: bold; }
        .seo { background-color: #007bff; }
        .aeo { background-color: #28a745; }
        .geo { background-color: #6f42c1; }
        .section { margin-bottom: 20px; }
        ul { list-style-type: none; padding: 0; }
        li { padding: 5px 0; border-bottom: 1px solid #eee; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Pipeline Audit Report</h1>
        
        <div class="score-board">
            <div class="score-card seo">SEO SCORE<br/>{{ scores['SEO'] }}</div>
            <div class="score-card aeo">AEO SCORE<br/>{{ scores['AEO'] }}</div>
            <div class="score-card geo">GEO SCORE<br/>{{ scores['GEO'] }}</div>
        </div>
        
        <div class="section">
            <h2>Metadata Analysis</h2>
            <ul>
            {% for item in metadata %}
                <li>{{ item }}</li>
            {% endfor %}
            </ul>
        </div>
        
        <div class="section">
            <h2>Headings Analysis</h2>
            <ul>
            {% for item in headings %}
                <li>{{ item }}</li>
            {% endfor %}
            </ul>
        </div>
        
        <div class="section">
            <h2>Readability Analysis</h2>
            <ul>
            {% for item in readability %}
                <li>{{ item }}</li>
            {% endfor %}
            </ul>
        </div>
        
        <div class="section">
            <h2>Schema Status</h2>
            <ul>
            {% for item in schema %}
                <li>{{ item }}</li>
            {% endfor %}
            </ul>
        </div>
        
        <div class="section">
            <h2>Internal Link Suggestions</h2>
            <ul>
            {% for page, links in internal_links.items() %}
                <li><strong>{{ page }}</strong> links to: {{ links | join(', ') }}</li>
            {% endfor %}
            </ul>
        </div>
        
    </div>
</body>
</html>
"""

def generate_html_report(data_dict, output_path="report.html"):
    template = Template(HTML_TEMPLATE)
    html_output = template.render(
        scores=data_dict["scores"],
        metadata=data_dict["metadata"],
        headings=data_dict["headings"],
        readability=data_dict["readability"],
        schema=data_dict["schema"],
        internal_links=data_dict.get("internal_links", {})
    )
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_output)
    print(f"Report generated at {output_path}")
