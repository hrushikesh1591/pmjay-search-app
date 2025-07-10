from flask import Flask, request, render_template, jsonify
import json

app = Flask(__name__)

# Load your PMJAY JSON data
with open("PMJAY_cleaned_data.json", "r", encoding="utf-8") as f:
    db = json.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    query = request.json.get("query", "").lower()
    results = [entry for entry in db if query in entry["procedure_name"].lower()]
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
