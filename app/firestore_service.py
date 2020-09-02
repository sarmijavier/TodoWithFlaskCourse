import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

if not firebase_admin._apps:
    credential = credentials.Certificate('./platzi-flask-5549c-firebase-adminsdk-g8mt6-af8a978d4c.json')
    firebase_admin.initialize_app(credential)

db = firestore.client()


def get_users():
    return db.collection(u'users').get()


def get_user(user_id):
    return db.collection(u'users').document(user_id).get()


def get_todos(user_id):
    return db.collection(u'users').document(user_id).collection(u'todos').get()