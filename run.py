from waitress import serve
from backend.app import create_app
from backend.config import Config

app = create_app(Config)

if __name__ == '__main__':
    print("Starting server on http://0.0.0.0:5000")
    print("Press Ctrl+C to stop")
    serve(app, host='0.0.0.0', port=5000, threads=4)

