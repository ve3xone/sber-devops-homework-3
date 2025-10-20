from flask import Flask, send_file

app = Flask(__name__)

@app.route('/file')
def get_file():
    try:
        return send_file('/app/data/sample.txt', mimetype='text/plain')
    except FileNotFoundError:
        return "File not found", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
