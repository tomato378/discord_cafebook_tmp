from flask import Flask
from threading import Thread
import os

app = Flask(__name__)

@app.route('/')
def home():
    return 'Discord bot is running! 🤖'

@app.route('/health')
def health():
    return {
        'status': 'online',
        'message': 'Discord bot is alive'
    }

def run():
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

def keep_alive():
    t = Thread(target=run)
    t.daemon = True
    t.start()
    print(f'🌐 Keep-alive server running on port {os.getenv("PORT", 5000)}')
