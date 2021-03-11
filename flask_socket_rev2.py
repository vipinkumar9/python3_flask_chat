from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit


app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
soc = SocketIO(app)


@app.route('/')
def index():
    return render_template('/flask_socket_rev2.htm')


@soc.on("messege")
def msg(m):
    print(m)
    soc.emit("messege", m)


if __name__ == "__main__":
    soc.run(app, debug=True)
