from flask import Flask, request, jsonify
import requests
import xmltodict
from base64 import b64decode

import database

app = Flask(__name__)

usps_userid = "156NONE02893"

usps_url_prefix = "http://production.shippingapis.com/ShippingAPI.dll?API="

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
  if not(valid_address_content(data)):
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
  if not(valid_address_content(data)):
    return "Malformed data", 400
  database.update_address(address_id, data);
  return "Address Updated", 204

@app.route('/address/<address_id>', methods=["DELETE"])
def delete_address_by_id(address_id):
  database.delete_address(address_id)
  return "Address Deleted", 204

@app.route('/city-state/<zip_code>', methods=["GET"])
def get_city_state_from_zip(zip_code):
  url = """{prefix}CityStateLookup&XML=<CityStateLookupRequest USERID="{user_id}">
      <ZipCode ID= "0">
        <Zip5>{zip_code}</Zip5>
      </ZipCode>
    </CityStateLookupRequest>"""
  tokens = {"prefix": usps_url_prefix, "user_id": usps_userid, "zip_code": zip_code}
  try:
    data = requests.get(url.format(**tokens))
    response = xmltodict.parse(data.text)
    content = response["CityStateLookupResponse"]["ZipCode"]
    return jsonify({"city": content["City"], "state": content["State"]})
  except:
    return "Results Inconclusive", 400

@app.route('/zip/<address>/<city>/<state>', methods=["GET"])
def get_zip_from_address_city_state(address, city, state):
  url = """{prefix}Verify&XML=<AddressValidateRequest USERID="{user_id}">
      <Address ID="0">
        <Address1></Address1>
        <Address2>{address}</Address2>
        <City>{city}</City>
        <State>{state}</State>
        <Zip5></Zip5>
        <Zip4></Zip4>
      </Address>
    </AddressValidateRequest>"""
  tokens = {
    "prefix": usps_url_prefix,
    "user_id": usps_userid,
    "address": b64decode(address).decode("latin1"),
    "city": city,
    "state": state
  }
  print(tokens)
  try:
    data = requests.get(url.format(**tokens))
    response = xmltodict.parse(data.text)
    print(response)
    content = response["AddressValidateResponse"]["Address"]
    return jsonify({"zip": content["Zip5"]})
  except:
    return "Results Inconclusive", 400

def valid_address_content(data):
  return isinstance(data["address"], str) and \
    len(data["address"]) > 0 and \
    isinstance(data["city"], str) and \
    len(data["city"]) > 0 and \
    isinstance(data["company"], str) and \
    isinstance(data["name"], str) and \
    len(data["name"]) > 0 and \
    isinstance(data["state"], str) and \
    len(data["state"]) > 0 and \
    isinstance(data["zip"], str) and \
    len(data["zip"]) > 0
