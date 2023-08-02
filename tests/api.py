from flask import Flask, request, jsonify

application = Flask(__name__)

@application.route("/json", methods=["GET", "POST"])
def post_json():
    if request.method == "POST":
        data = request.get_json()
        if data is None:
            return jsonify({"message": "Invalid JSON data"}), 400

        # Do something with the JSON data
        print(data)

        return jsonify(data), 200

    # Handle GET requests
    return "This is a GET request. Send a POST request with JSON data to this endpoint.", 200

if __name__ == "__main__":
    application.run()
