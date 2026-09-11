import os
from flask import Flask, render_template, request, jsonify
from ai_engine import generate_ai
app=Flask(__name__)
SYSTEM_INSTRUCTION=os.getenv("SYSTEM_INSTRUCTION","You are a helpful professional AI assistant.")
@app.route("/")
def home(): return render_template("index.html", title=os.getenv("PROJECT_TITLE","AI Project"))
@app.post("/api/generate")
def generate():
    data=request.get_json() or {}
    text=data.get("input","").strip()
    if not text:return jsonify(error="Enter some input"),400
    try:return jsonify(result=generate_ai(text,SYSTEM_INSTRUCTION))
    except Exception as e:return jsonify(error=str(e)),503
if __name__=="__main__": app.run(debug=True)
