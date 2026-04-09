from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "CI/CD Pipeline is alive! v2", "status": "ok"})

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/about")
def about():
    return jsonify({
        "author": "Mahmoud Zangri",
        "project": "CI/CD Pipeline",
        "stack": ["Python", "Flask", "Docker", "GitHub Actions"]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)