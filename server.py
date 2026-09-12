from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "online", "service": "Ricam Downloader Pro Backend"})

@app.route('/api/download', methods=['POST'])
def process_download():
    data = request.json or {}
    url = data.get('url')
    format_type = data.get('format', 'mp4')
    
    if not url:
        return jsonify({"error": "No URL provided"}), 400
        
    return jsonify({
        "status": "success",
        "message": f"Successfully queued download for {url}",
        "format": format_type
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
