from flask import Flask, request, jsonify
import uuid

from utils import calculate_points

app = Flask(__name__)

# In-memory storage for receipts
receipts_storage = {}

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/receipts/process', methods=['POST'])
def process_receipt():
    data = request.json
    
    # Generate a uuid for the receipt
    receipt_id = str(uuid.uuid4())
    receipts_storage[receipt_id] = data
    
    return jsonify({"id": receipt_id}), 200

@app.route('/receipts/<receipt_id>/points', methods=['GET'])
def get_points(receipt_id):
    receipt = receipts_storage.get(receipt_id)
    if receipt:
        points = calculate_points(receipt)
        return jsonify({"id": receipt_id, "points": points}), 200
    else:
        return jsonify({"error": "Receipt not found"}), 404

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host="0.0.0.0", debug=True, port=80)
