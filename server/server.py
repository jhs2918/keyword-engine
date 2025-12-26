from flask import Flask, render_template, request, jsonify
import sys
import os

# 프로젝트 루트 경로 추가 (Render 필수)
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from modules.analyzer import analyze_keyword  # ⭐ 이 줄이 빠져 있었음

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    kw = request.json.get("kw", "").strip()
    if not kw:
        return jsonify([])

    result = analyze_keyword(kw)
    return jsonify(result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
