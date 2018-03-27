from flask import Flask, jsonify, request, session #from flask import classes
import re #re is a module that assists in regular expression(checks if certain formats are met)
from app.hb_users import hello_book_users 

app=Flask(__name__)

@app.route('/api/auth/register/', methods=['POST']) #This a url path using method POST when registering new user

def register()
    '''
    This method is used to validate user registration
    '''
    user = hello_book_users()
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    password_confirmation = ['password_confirmation']

    if not username or len(username.strip()) == 0:
        return jsonify({'message': 'You did not input anything, Please enter username'}), 401
    elif not email or len(email.strip()) == 0:
        return jsonify({'message': 'You did not input anything, Please enter email'}), 401
    elif not password or len(password.strip()) == 0:
        return jsonify({'message': 'You did not input anything, password should be atleast 8 characters'}), 401
    elif password != password_confirmation:
        return jsonify({'message': 'Password does not match previous entry'}), 401
    elif re.match is not (r'(^[a-zA-Z0-9_.+-] + @[a-zA-Z0-9-] + \.[a-zA-Z.] + $)', email):
        return jsonify({'message': 'Invalid entry, please enter valid email address'}), 401
    elif [user for user in hello_book_users if user['email'] == email]:
        return jsonify({'message': 'Registration succesful'}), 201


app.route('/api/auth/login/', methods=['POST'])

#Still working on login endpoint
#def login():
 #   user = hello_book_users()
  #  username = request.json['username']
   # password = request.json['password']


    