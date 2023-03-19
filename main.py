from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config["SECRET_KEY"] = "asdasdeqd34134dsd12343dd"
socketio = SocketIO(app)


@app.get("/")
def index():
    return render_template("index.html")


@socketio.on("save_file")
def create_file(data):
    socketio.emit("stream", data)
    
