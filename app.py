from flask import  Flask, request, render_template,jsonify, make_response
import firebase_admin
from firebase_admin import credentials, firestore
from k8s import credfirestore
import requests


cred_data = credfirestore.firebase_cred()
cred = credentials.Certificate(cred_data)
firebase_admin.initialize_app(cred)
db = firestore.client()

app = Flask(__name__)

@app.route('/')
def index():
    # return render_template('index.html')
    return "Welcome to citySights API"

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

@app.route( '/login', methods=['POST'] )
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
    except Exception as e:
        response = jsonify({'error':(e)})
        response.status_code = 500
        return response
    
@app.route('/logout', methods = [ 'POST' ])
def  logout():
    data = request.json
    id_token=data['id_Token']

    auth = firebase_admin.auth()
    try:
        auth.revoke_refresh_tokens(id_token)

        # Return a 200 OK response
        response = make_response()
        response.status_code = 200
        return response
    
    except Exception as e:
        response = jsonify({'error': str(e)})
        response.status_code = 500
        return response

@app.route('/get-madrid-museum-data', methods=['GET'])
def get_madrid_museums_data():
    url = 'https://datos.madrid.es/egob/catalogo/201132-0-museos.json'
    response = requests.get(url=url, headers={'Accept': 'application/json'})
    data = response.json()
    museums_data = []
 
    for item in data['@graph'][:4]:
        title = item.get('title', '')
        street_address = item.get('address', {}).get('street-address', '')
        museum_data = {'title': title, 'street_address': street_address}
        museums_data.append(museum_data)
 
    return jsonify(museums_data)

@app.route("/monuments",methods=["GET"])
def monuments():
    url = 'https://datos.madrid.es/egob/catalogo/300356-0-monumentos-ciudad-madrid.json'
    response = requests.get(url=url, headers={'Accept': 'application/json'})
    data = response.json()
    monuments = [{'title': item['title'], 'street-address': item['address']['street-address']} for item in data['@graph']]
    return jsonify(monuments)

# if __name__ == '__main__':
#     app.run(debug=True)





