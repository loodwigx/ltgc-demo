def address_content(data):
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
    len(data["zip"]) > 0 and \
    zip_in_city_state(data["city"], data["state"], data["zip"])

def zip_in_city_state(city, state, zip_code):
  # TODO validate vs USPS
  return True