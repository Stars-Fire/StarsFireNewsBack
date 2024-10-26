from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/submit', methods=['POST'])
def submit():
    try:
        if not request.is_json:
            return jsonify({"error": "Request must be JSON"}), 400

        data = request.get_json()

        print("Received data:")
        print(f"Author: {data.get('author')}")
        print(f"Title: {data.get('title')}")
        print(f"Content: {data.get('content')}")
        print(f"Type: {data.get('type')}")
        print(f"Time: {data.get('time')}")

        return jsonify({"message": "Submission received"}), 200
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(port=20230, debug=True)