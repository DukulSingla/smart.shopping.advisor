from flask import Flask, request, jsonify
import requests
import datetime

app = Flask(__name__)

# Configuration for lyzr API
LYZR_API_BASE_URL = "https://agent-prod.studio.lyzr.ai"
LYZR_API_KEY = "YOUT_API_KEY"

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"datestamp": datetime.datetime.now().isoformat()})

@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Get request data
        data = request.get_json()
        
        # Make request to lyzr API
        response = requests.post(
            f"{LYZR_API_BASE_URL}/v3/inference/chat/",
            headers={
                'Content-Type': 'application/json',
                'x-api-key': LYZR_API_KEY
            },
            json={
                "user_id": data.get('user_id', "iamspathan@gmail.com"),
                "agent_id": data.get('agent_id', "685796a717bfa0b3af0f39e6"),
                "session_id": data.get('session_id', "685796a717bfa0b3af0f39e6-pr2hxsckm4e"),
                "message": data.get('message', "")
            }
        )
        response.raise_for_status()
        return jsonify(response.json())
    except requests.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)