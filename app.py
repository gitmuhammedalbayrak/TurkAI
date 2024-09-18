from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__, static_folder='static', static_url_path='')

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/api/think', methods=['POST'])
def think():
    data = request.json
    user_message = data.get('message', '')
    # Burada gerçek bir AI işlemi simüle ediliyor
    ai_response = f"Hmm..."
    return jsonify({'response': ai_response})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
