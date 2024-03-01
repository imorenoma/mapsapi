# Map Api

### Index
1. [First Steps](#howto)
2. [Api project path](#api)
3. [API Functions](#functions)

----

## First Steps <a name= 'howto'></a>

The first stept is cloning the repository from:

```bash
    git clone https://github.com/imorenoma/mapsapi
```

Them go inside the project:
```bash
   cd ~/.../mapsapi
```

Now install the virtual env and un it and install all dependencies:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
For windows:

```bash
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```

Now you need to  create a .env file in the root of your repo, the data inside of this .env will be like:

```
FIREBASE_TYPE=type
FIREBASE_PROJECT_ID=project_id
FIREBASE_PRIVATE_KEY_ID=private_key_id
FIREBASE_PRIVATE_KEY=private_key
FIREBASE_CLIENT_EMAIL='client_email
FIREBASE_CLIENT_ID=client_id
FIREBASE_AUTH_URI=auth_uri
FIREBASE_TOKEN_URI=token_uri
FIREBASE_AUTH_PROVIDER_X509_CERT_URL=auth_provider_X509_cert_url
FIREBASE_CLIENT_X509_CERT_URL=client_X509_cert_url
FIREBASE_UNIVERSE_DOMAIN=universe_domain
```

The parameter on the right side of the equal comes from the JSON file that Firestore generates to connect to your database.

---
## Api project path <a name= 'api'></a>
```bash
.
├── app.py                 # Main application file
├── app.yaml
├── k8s
│   └── credfirestore.py
├── .venv
├── .env
├── requirements.txt
├── README.md
├── dockerfile
└── 
```
---

## Api Funtions  <a name = 'functions'></a>

### Send data from comunidad de madrid open data  Function: 

In this code we can se how do we take data from  the Comunidad de Madrid Open Data, in order to send it to the front and print this data, in this case we send name of the museum and the addres, and monuments

```python
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
```

```python
@app.route("/monuments",methods=["GET"])
def monuments():
    url = 'https://datos.madrid.es/egob/catalogo/300356-0-monumentos-ciudad-madrid.json'
    response = requests.get(url=url, headers={'Accept': 'application/json'})
    data = response.json()
    monuments = [{'title': item['title'], 'street-address': item['address']['street-address']} for item in data['@graph']]
    return jsonify(monuments)
```

### Login Function

The loging function  is used for authenticate the user in the app,
this function check if the user are in the database of firestore, in 
other case they send error messages

```python
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
```
### Logout Function
```python
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
```
### Register Function 
This function takes data that comes from a from of vue and save the data in a
Firestore database, the parameters that we save are name, pass, and some options
```python
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
```










    


