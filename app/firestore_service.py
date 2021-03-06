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


def user_put(user_data):
    user_ref = db.collection(u'users').document(user_data.username)
    user_ref.set({'password': user_data.password})


def put_todo(user_id, description):
    todos_collection_ref = db.collection(u'users').document(user_id).collection('todos')
    todos_collection_ref.add({'description': description, 'done': False})

def delete_todo(user_id, todo_id):
    #print(f'{user_id}  {todo_id}--------------------------------------------------')
    #todo_ref = db.collection(f'users/{user_id}/todos/{todo_id}')
    todo_ref = _get_todo_ref(user_id, todo_id)
    todo_ref.delete()


def update_todo(user_id, todo_id, done):
    todo_done = not bool(done)
    todo_ref = _get_todo_ref(user_id, todo_id)
    todo_ref.update({'done': todo_done})

def _get_todo_ref(user_id, todo_id):
    return  db.collection(u'users').document(user_id).collection('todos').document(todo_id)

    