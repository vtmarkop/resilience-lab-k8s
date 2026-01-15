from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/products')
def get_products():
    # Chaos Experiment Target: 
    # This endpoint is designed to verify latency injection.
    return jsonify({
        "id": 101, 
        "name": "Resilient Widget", 
        "stock": 50,
        "region": "eu-central-1"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
