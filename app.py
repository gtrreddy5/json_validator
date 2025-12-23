from flask import Flask, render_template, request, Response
import json
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    error = ""
    error_line = ""
    error_col = ""
    input_json = ""

    if request.method == "POST":
        input_json = request.form.get("json_input", "")
        action = request.form.get("action")

        try:
            parsed = json.loads(input_json)

            if action == "validate":
                message = "✅ Valid JSON"

            elif action == "beautify":
                input_json = json.dumps(parsed, indent=4)
                message = "✅ JSON Beautified"

            elif action == "minify":
                input_json = json.dumps(parsed, separators=(",", ":"))
                message = "✅ JSON Minified"

        except json.JSONDecodeError as e:
            error = "❌ Invalid JSON"
            error_line = e.lineno
            error_col = e.colno

    return render_template(
        "index.html",
        input_json=input_json,
        message=message,
        error=error,
        error_line=error_line,
        error_col=error_col
    )

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

@app.route("/terms")
def terms():
    return render_template("terms.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/sitemap.xml")
def sitemap():
    pages = [
        "https://json-tools-online.com/",
        "https://json-tools-online.com/about",
        "https://json-tools-online.com/privacy",
        "https://json-tools-online.com/terms",
        "https://json-tools-online.com/contact",
    ]

    xml = ['<?xml version="1.0" encoding="UTF-8"?>']
    xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    for page in pages:
        xml.append(f"""
        <url>
            <loc>{page}</loc>
            <changefreq>weekly</changefreq>
            <priority>0.8</priority>
        </url>
        """)

    xml.append('</urlset>')
    return Response("\n".join(xml), mimetype="application/xml")
@app.route("/robots.txt")
def robots():
    content = """User-agent: *
Allow: /

Sitemap: https://json-tools-online.com/sitemap.xml
"""
    return Response(content, mimetype="text/plain")
@app.route("/json-to-csv", methods=["GET", "POST"])
def json_to_csv():
    return render_template("json_to_csv.html")

@app.route("/json-viewer")
def json_viewer():
    return render_template("json_viewer.html")

@app.route("/json-to-xml")
def json_to_xml():
    return render_template("json_to_xml.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
# if __name__ == "__main__":
#     app.run(debug=True)
