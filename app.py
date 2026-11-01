from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Load the sentiment analysis model locally (runs completely free on your CPU/GPU)
print("Loading AI model locally... please wait a moment.")
classifier = pipeline("sentiment-analysis", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")
print("Model loaded successfully!")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('text', '').strip()
    
    if not text:
        return jsonify({'error': 'No text provided'}), 400
        
    try:
        # Run inference locally
        results = classifier(text)
        
        # Format results for the frontend
        formatted_results = [
            {'label': r['label'], 'score': r['score']} 
            for r in results
        ]
        return jsonify(formatted_results)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)