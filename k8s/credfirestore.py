from dotenv import load_dotenv
import os
import json

load_dotenv()

def firebase_cred():    

    FIRESTORE_PROJECT_ID = os.getenv('FIRESTORE_PROJECT_ID')
    FIRESTORE_PRIVATE_KEY_ID = os.getenv('FIRESTORE_PRIVATE_KEY_ID')
    FIRESTORE_PRIVATE_KEY = os.getenv('FIRESTORE_PRIVATE_KEY').replace('\\n','\n')
    FIRESTORE_CLIENT_EMAIL = os.getenv('FIRESTORE_CLIENT_EMAIL')
    FIRESTORE_CLIENT_ID = os.getenv('FIRESTORE_CLIENT_ID')
    FIRESTORE_AUTH_URI = os.getenv('FIRESTORE_AUTH_URI')
    FIRESTORE_TOKEN_URI = os.getenv('FIRESTORE_TOKEN_URI')
    FIRESTORE_AUTH_PROVIDER_X509_CERT_URL = os.getenv('FIRESTORE_AUTH_PROVIDER_X509_CERT_URL')
    FIRESTORE_CLIENT_X509_CERT_URL = os.getenv('FIRESTORE_CLIENT_X509_CERT_URL')

    cred = {
        'firestore_project_id': FIRESTORE_PROJECT_ID,
        'firestore_private_key_id': FIRESTORE_PRIVATE_KEY_ID,
        'firestore_private_key': FIRESTORE_PRIVATE_KEY,
        'firestore_client_email': FIRESTORE_CLIENT_EMAIL,
        'firestore_client_id': FIRESTORE_CLIENT_ID,
        'firestore_auth_uri': FIRESTORE_AUTH_URI,
        'firestore_token_uri': FIRESTORE_TOKEN_URI,
        'firestore_auth_provider_X509_cert_url':FIRESTORE_AUTH_PROVIDER_X509_CERT_URL,
        'firestore_client_X509_cert_url': FIRESTORE_CLIENT_X509_CERT_URL
    }

    cred = json.dumps(cred, indent=4)

    return cred