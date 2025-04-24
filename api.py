from flask import Flask, request, jsonify
from flask_cors import CORS
from app.optimizers import ContentOptimizer

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

optimizer = ContentOptimizer()

@app.route('/api/generate-title', methods=['POST'])
def generate_title():
    data = request.json
    summary = data.get('summary', '')
    category = data.get('category', '')
    
    if not summary:
        return jsonify({"error": "Summary is required"}), 400
    
    try:
        title = optimizer.generate_title(f"{category} video about: {summary}")
        return jsonify({"title": title})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/generate-description', methods=['POST'])
def generate_description():
    data = request.json
    summary = data.get('summary', '')
    category = data.get('category', '')
    tone = data.get('tone', 'informative')
    include_timestamps = data.get('includeTimestamps', False)
    
    if not summary:
        return jsonify({"error": "Summary is required"}), 400
    
    try:
        description = optimizer.write_description(
            f"{category} video about: {summary}",
            tone=tone,
            include_timestamps=include_timestamps
        )
        return jsonify({"description": description})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/suggest-tags', methods=['POST'])
def suggest_tags():
    data = request.json
    summary = data.get('summary', '')
    category = data.get('category', '')
    count = data.get('count', 10)
    
    if not summary:
        return jsonify({"error": "Summary is required"}), 400
    
    try:
        tags = optimizer.suggest_tags(f"{category} video about: {summary}", count=count)
        return jsonify({"tags": tags})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/thumbnail-text', methods=['POST'])
def thumbnail_text():
    data = request.json
    summary = data.get('summary', '')
    title = data.get('title', '')
    
    if not summary or not title:
        return jsonify({"error": "Both summary and title are required"}), 400
    
    try:
        suggestions = optimizer.thumbnail_text_suggestions(title, summary)
        return jsonify({"suggestions": suggestions})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)