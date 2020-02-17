from flask import Flask, request, jsonify
import database
import validate

app = Flask(__name__)

database.init_db()

@app.route("/", methods=["GET"])
def root():
  return jsonify({"ping": "pong"})

@app.route('/address', methods=["GET"])
def get_all_addresses():
  data = database.read_addresses()
  return jsonify(data)

@app.route('/address', methods=["POST"])
def create_address():
  data = request.get_json()
  if not(validate.address_content(data)):
    return "Malformed data", 400
  database.create_address(data);
  return "Address Created", 201

@app.route('/address/<address_id>', methods=["GET"])
def get_address_by_id(address_id):
  try:
    data = database.read_address(address_id)
    return jsonify(data)
  except ValueError:
    return "Bad Address ID", 400

@app.route('/address/<address_id>', methods=["PUT"])
def set_address_by_id(address_id):
  data = request.get_json()
  if not(validate.address_content(data)):
    return "Malformed data", 400
  database.update_address(address_id, data);
  return "Address Updated", 204

@app.route('/address/<address_id>', methods=["DELETE"])
def delete_address_by_id(address_id):
  database.delete_address(address_id)
  return "Address Deleted", 204
