from flask import Flask, request, jsonify

# Define the Flask app
app = Flask(__name__)

subscribers = {}

@app.route('/', methods=['GET'])
def root():
    return jsonify({"message": "nothing here!"}), 400

@app.route('/list-subscribers', methods=['GET'])
def list_subscribers():
  return jsonify(subscribers)

@app.route('/add-subscriber', methods=['POST'])
def add_subscriber():
  data = request.json
  name = data.get('name')
  URI = data.get('URI')
  if name is not None and URI is not None:
      subscribers[name] = URI
      return jsonify({"message": f"added subscriber: {name} with {URI}"})
  else:
      return jsonify({"message": "bad request"}), 400

@app.route("/del-subscriber", methods=["POST"])
def del_subscriber():
    data = request.json
    name = data.get("name")

    if name is None:
      return jsonify({"message": "bad request"}), 400

    if name in subscribers:
        del subscribers[name]
        return jsonify({"message": f"deleted subscriber: {name}"})
    else:
        # non-existent subscriber is not an error on delete
        return jsonify({"message": f"no subscriber named: {name}"})


@app.route("/notify", methods=["POST"])
def notify():
    data = request.json
    # lab didn't specify what to actually *do* with the notify data so I'm just gonna print it
    payload = data.get("payload")
    if payload is None:
        return jsonify({"message": "bad request"}), 400
    print(f"notify payload: {payload}")
    for k,v in subscribers:
        print(f"notifying {k}@{v}\n")

    return jsonify({"message": "notify complete"})


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
