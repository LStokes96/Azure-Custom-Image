from flask import Flask 
import socket

app = Flask(__name__)

host = socket.gethostname()

@app.route('/')
def index():
    return "<h1>Hello World, I'm deployed automaticaly on " + str(host) + " :)</h1>"

if __name__=='__main__':
        app.run(host, port=5000, debug=True)
