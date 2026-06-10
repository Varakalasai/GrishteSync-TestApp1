# Created with GrishteSync
# https://suryasticsai.github.io/GrishteSync
# Suryasticsai | suryasticsai@gmail.com
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Welcome to GrishteSync Test App</h1><br><img src="https://i.ibb.co/RGmb4FKk/1781072041102.png"><br><p>Made with GrishteSync | Suryasticsai | suryasticsai@gmail.com</p>"

if __name__ == "__main__":
    app.run()