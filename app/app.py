from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def root():
  return jsonify({"hello": "world"})

@app.route("/app", methods=["GET"])
def app_path():
  return jsonify({"hello": "app"})
