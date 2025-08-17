from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to connect

# Health check route (to test if backend is running)
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "Backend is running!"})

# Summarize route
@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.get_json()
    transcript = data.get("transcript", "")
    prompt = data.get("prompt", "")
    summary = f"Summary for prompt '{prompt}': {transcript[:100]}..."
    return jsonify({"summary": summary})

# Email sending route (mock version for now)
@app.route("/send-email", methods=["POST"])
def send_email():
    data = request.get_json()
    recipient = data.get("recipient")
    summary = data.get("summary")
    # Instead of sending email, we just simulate success
    return jsonify({"status": f"Email sent to {recipient} with summary!"})

if __name__ == "__main__":
    app.run(debug=True)
