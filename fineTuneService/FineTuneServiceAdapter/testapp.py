from flask import Flask
import os


app = Flask(__name__)

@app.route('/')
def hello_world():
    cwd = os.getcwd()
    return cwd

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')