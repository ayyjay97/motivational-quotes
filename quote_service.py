from flask import Flask, jsonify
from flask_cors import CORS
import random
import json
import os

app = Flask(__name__)
CORS(app)

def load_quotes():
    """Reads quotes from the JSON file."""
    try:
        with open('quotes.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        # Fallback if the file is missing
        return [{"quote": "Stay hard.", "author": "David Goggins"}]

@app.route('/get_quote', methods=['GET'])
def get_quote():
    quotes = load_quotes()
    
    if not quotes:
        return jsonify({"error": "No quotes available."}), 404
        
    # Select a random quote
    random_quote = random.choice(quotes)
    
    # Return the quote as JSON
    return jsonify(random_quote), 200

if __name__ == '__main__':
    # Running on port 5003 to avoid conflicts with your other services
    port = int(os.environ.get('PORT', 5003))
    app.run(host='0.0.0.0', port=port, debug=True)