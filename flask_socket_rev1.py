from flask import Flask, render_template
from flask_socketio import SocketIO


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
io = SocketIO(app)
active_users = [0]


@app.route('/')
def sessions():
    return render_template('flask_socket_rev1.htm')

@io.on("connect")
def conn():  
    a = active_users.pop()
    a += 1
    active_users.append(a)
    print("Active users:" + str(a))
    io.emit("messege",{"data": str(a)})


@io.on("disconnect")
def d_conn():
    a = active_users.pop()
    a -= 1
    active_users.append(a)
    print("Active users:" + str(a))
    io.emit("messege",{"data": str(a)})



    
    



if __name__ == '__main__':
    io.run(app, debug=True)