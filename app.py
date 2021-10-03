from flask import Flask, render_template
from flask_socketio import SocketIO
from api.workspace import workspace_api
import settings

app = Flask(__name__)

app.register_blueprint(workspace_api)

socketio = SocketIO(app)


@app.route("/")
def index():
    return render_template('./index.html',)


@socketio.on('send_message')
def handle_source(json_data):
    text = json_data['message']
    socketio.emit('echo', {'echo': 'Server Says: '+text})


if __name__ == "__main__":
    socketio.run(app, port=settings.PORT)