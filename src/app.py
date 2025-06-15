from flask import Flask, request, jsonify, render_template_string
from model import GenerativeAIModel
import logging
import os

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# Initialize model
model = GenerativeAIModel()

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Generative AI Model</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 50px; }
        .container { max-width: 800px; margin: 0 auto; }
        textarea { width: 100%; height: 100px; }
        button { background-color: #4CAF50; color: white; padding: 10px 20px; border: none; cursor: pointer; }
        .result { background-color: #f9f9f9; padding: 20px; margin-top: 20px; border-radius: 5px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🤖 Generative AI Model</h1>
        <form id="genForm">
            <label for="prompt">Enter your prompt:</label><br><br>
            <textarea id="prompt" name="prompt" placeholder="Enter your text prompt here..."></textarea><br><br>
            <label for="max_length">Max Length:</label>
            <input type="number" id="max_length" name="max_length" value="100" min="50" max="500"><br><br>
            <button type="submit">Generate Text</button>
        </form>
        <div id="result" class="result" style="display:none;">
            <h3>Generated Text:</h3>
            <p id="generated-text"></p>
        </div>
    </div>
    
    <script>
        document.getElementById('genForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            const prompt = document.getElementById('prompt').value;
            const maxLength = document.getElementById('max_length').value;
            
            try {
                const response = await fetch('/generate', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ prompt: prompt, max_length: parseInt(maxLength) })
                });
                const data = await response.json();
                document.getElementById('generated-text').innerText = data.generated_text;
                document.getElementById('result').style.display = 'block';
            } catch (error) {
                alert('Error: ' + error.message);
            }
        });
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/health')
def health():
    try:
        status = model.health_check()
        return jsonify({'status': 'healthy', 'message': status}), 200
    except Exception as e:
        return jsonify({'status': 'unhealthy', 'error': str(e)}), 500

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.get_json()
        prompt = data.get('prompt', '')
        max_length = data.get('max_length', 100)
        
        if not prompt:
            return jsonify({'error': 'Prompt is required'}), 400
        
        generated_text = model.generate_text(prompt, max_length)
        return jsonify({'generated_text': generated_text})
    
    except Exception as e:
        app.logger.error(f"Error in generate endpoint: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)