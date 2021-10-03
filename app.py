from flask import Flask, render_template, request
from flask_socketio import SocketIO
from api.workspace import workspace_api
import settings
import firebase_admin as fb_admin
from firebase_admin import auth as fb_auth, fb_exceptions


app = Flask(__name__)

app.register_blueprint(workspace_api)

socketio = SocketIO(app)
default_app = fb_admin.initialize_app()


@app.route("/")
def index():
    return render_template('./index.html',)


# ref: https://firebase.google.com/docs/auth/admin/manage-cookies
@app.route('/logged_in', methods=['POST'])
def session_login():
    try:
        id_token = request.json['idToken']
        decoded_token = fb_auth.verify_id_token(id_token)
        uid = decoded_token['uid']
        return f"logged in with id {uid}"
        # TODO: use @app.errorhandler
    except ValueError or fb_exceptions.InvalidIdTokenError:
        return "Invalid token"
    except fb_exceptions.ExpiredIdTokenError:
        return "Token expired"
    except fb_exceptions.RevokedIdTokenError:
        return "Token has been revoked"
    except fb_exceptions.CertificateFetchError:
        return "Could not fetch certificate"
    except fb_exceptions.UserDisabledError:
        return "User is disabled"



@socketio.on('send_message')
def handle_source(json_data):
    text = json_data['message']
    socketio.emit('echo', {'echo': 'Server Says: '+text})



if __name__ == "__main__":
    socketio.run(app, port=settings.PORT)