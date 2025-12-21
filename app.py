from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    error = ""
    error_line = ""
    error_col = ""
    input_json = ""
    action = ""

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

if __name__ == "__main__":
    app.run()
