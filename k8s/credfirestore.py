from dotenv import load_dotenv
import os
import json

load_dotenv()

def firebase_cred():    
    FIREBASE_TYPE = os.getenv('FIREBASE_TYPE')
    FIRESTORE_PROJECT_ID = os.getenv('FIRESTORE_PROJECT_ID')
    FIRESTORE_PRIVATE_KEY_ID = os.getenv('FIRESTORE_PRIVATE_KEY_ID')
    FIRESTORE_PRIVATE_KEY = os.getenv('FIRESTORE_PRIVATE_KEY').replace('\\n','\n')
    FIRESTORE_CLIENT_EMAIL = os.getenv('FIRESTORE_CLIENT_EMAIL')
    FIRESTORE_CLIENT_ID = os.getenv('FIRESTORE_CLIENT_ID')
    FIRESTORE_AUTH_URI = os.getenv('FIRESTORE_AUTH_URI')
    FIRESTORE_TOKEN_URI = os.getenv('FIRESTORE_TOKEN_URI')
    FIRESTORE_AUTH_PROVIDER_X509_CERT_URL = os.getenv('FIRESTORE_AUTH_PROVIDER_X509_CERT_URL')
    FIRESTORE_CLIENT_X509_CERT_URL = os.getenv('FIRESTORE_CLIENT_X509_CERT_URL')
    FIREBASE_UNIVERSE_DOMAIN = os.getenv('FIREBASE_UNIVERSE_DOMAIN')

    cred = {
        "type": FIREBASE_TYPE,
        'project_id': FIRESTORE_PROJECT_ID,
        'private_key_id': FIRESTORE_PRIVATE_KEY_ID,
        'private_key': FIRESTORE_PRIVATE_KEY,
        'client_email': FIRESTORE_CLIENT_EMAIL,
        'client_id': FIRESTORE_CLIENT_ID,
        'auth_uri': FIRESTORE_AUTH_URI,
        'token_uri': FIRESTORE_TOKEN_URI,
        'auth_provider_X509_cert_url':FIRESTORE_AUTH_PROVIDER_X509_CERT_URL,
        'client_X509_cert_url': FIRESTORE_CLIENT_X509_CERT_URL,
        'universe_domain': FIREBASE_UNIVERSE_DOMAIN
    }

    cred = json.dumps(cred, indent=4)

    return cred