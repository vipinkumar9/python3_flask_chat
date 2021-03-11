from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, leave_room

app = Flask(__name__)

soc = SocketIO(app)


@app.route("/")
def index():
    return render_template("/flask_socket_rev3.htm")


@soc.on("join")
def send_messege(data):
    room = data['channel']
    join_room(room)
    json = {'username': data['username'],'room':room}
    print(str(json['username']) + " Connected to room " + str(room))
    soc.emit("broadcast_messege",json,room=room)





if __name__ == "__main__":
    soc.run(app, debug=True, host='localhost', port=80)
