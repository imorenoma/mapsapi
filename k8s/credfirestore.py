from dotenv import load_dotenv
import os


load_dotenv()

def firebase_cred():

    FIRESTORE_TYPE = os.getenv('FIREBASE_TYPE')
    FIRESTORE_PROJECT_ID = os.getenv('FIREBASE_PROJECT_ID')
    FIRESTORE_PRIVATE_KEY_ID = os.getenv('FIREBASE_PRIVATE_KEY_ID')

    FIRESTORE_PRIVATE_KEY = os.getenv('FIREBASE_PRIVATE_KEY')
    if FIRESTORE_PRIVATE_KEY is None:
        raise Exception('FIREBASE_PRIVATE_KEY environment variable is not set')
        
    FIRESTORE_PRIVATE_KEY = FIRESTORE_PRIVATE_KEY.replace('\\n', '\n')
    
    FIRESTORE_CLIENT_EMAIL = os.getenv('FIREBASE_CLIENT_EMAIL')
    FIRESTORE_CLIENT_ID = os.getenv('FIREBASE_CLIENT_ID')
    FIRESTORE_AUTH_URI = os.getenv('FIREBASE_AUTH_URI')
    FIRESTORE_TOKEN_URI = os.getenv('FIREBASE_TOKEN_URI')
    FIRESTORE_AUTH_PROVIDER_X509_CERT_URL = os.getenv('FIREBASE_AUTH_PROVIDER_X509_CERT_URL')
    FIRESTORE_CLIENT_X509_CERT_URL = os.getenv('FIREBASE_CLIENT_X509_CERT_URL')
    FIRESTORE_UNIVERSE_DOMAIN = os.getenv('FIREBASE_UNIVERSE_DOMAIN')

    cred = {
        'type': FIRESTORE_TYPE,
        'project_id': FIRESTORE_PROJECT_ID,
        'private_key_id': FIRESTORE_PRIVATE_KEY_ID,
        'private_key': FIRESTORE_PRIVATE_KEY,
        'client_email': FIRESTORE_CLIENT_EMAIL,
        'client_id': FIRESTORE_CLIENT_ID,
        'auth_uri': FIRESTORE_AUTH_URI,
        'token_uri': FIRESTORE_TOKEN_URI,
        'auth_provider_X509_cert_url':FIRESTORE_AUTH_PROVIDER_X509_CERT_URL,
        'client_X509_cert_url': FIRESTORE_CLIENT_X509_CERT_URL,
        'universe_domain': FIRESTORE_UNIVERSE_DOMAIN
    }
    
    return cred
