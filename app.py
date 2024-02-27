from flask import  Flask, request, render_template,jsonify, make_response
import firebase_admin
from firebase_admin import credentials, firestore
from k8s import credfirestore

cred = credfirestore.firebase_cred()

firebase_admin.initialize_app(cred)

db = firestore.client()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.json()
    mail = data['mail']
    passwd = data['psswd']
    radius = data['radius']

    auth=firebase_admin.auth()
    try:
        user = auth.create_user(mail=mail, passwd=passwd)
        user_id = user['uid']

        user_ref = db.collection('users').document(user_id)
        user_ref.set({
            'mail':mail,
            'radius':int(radius)
            })
        
        response = jsonify({'message': 'User created successfully!'})
        response.status_code = 200
        return response
    
    except Exception as e:
        response = jsonify({'error': str(e)})
        response.status_code = 400
        return response

@app.route( '/login', methods=[ 'POST' ] )
def login():
    data = request.json
    mail = data['mail']
    passwd = data['psswd']

    auth = firebase_admin.auth()
    try:
        user = auth.get_user_by_email(mail)
        if user:
            if auth.verify_password(passwd, user.password_hash):
                response = make_response()
                response.status_code = 200
                return response
            else:
                response = jsonify({'error': 'Invalid password'})
                response.status_code = 401
                return response
        else:
            response = jsonify({'error': 'User not found'})
            response.status_code = 404
            return response
    except:
        response = jsonify({'error':(e)})
        response.status_code = 500
        return response


if __name__ == '__main__':
    app.run(debug=True)









