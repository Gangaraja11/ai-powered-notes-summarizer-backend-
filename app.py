from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)

# Start with no model loaded
summarizer = None

@app.route("/summarize", methods=["POST"])
def summarize():
    global summarizer
    data = request.get_json()
    transcript = data.get("transcript", "")
    prompt = data.get("prompt", "")

    if not transcript:
        return jsonify({"error": "Transcript is required"}), 400

    # Load summarizer only when needed (first request)
    if summarizer is None:
        print("⏳ Loading AI model, please wait...")
        summarizer = pipeline("summarization", model="t5-small") # ⚡ faster model
        print("✅ Model loaded!")

    # Generate summary
    result = summarizer(transcript, max_length=100, min_length=30, do_sample=False)
    summary_text = result[0]['summary_text']

    return jsonify({"summary": summary_text, "prompt_used": prompt})

@app.route("/send-email", methods=["POST"])
def send_email():
    data = request.get_json()
    recipient = data.get("recipient", "")
    summary = data.get("summary", "")

    # Simulated response
    return jsonify({"status": f"Email sent to {recipient} with summary."})

if __name__ == "__main__":
    app.run(debug=True)