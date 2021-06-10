from flask import Flask
import sys

print(sys.path)

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "<h1>Testing!</h1>"


if "__main__" == __name__:
    app.run(host="0.0.0.0", port=5000, debug=True) 