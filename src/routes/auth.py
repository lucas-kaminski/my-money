from datetime import datetime, timedelta
import os
from server.instance import server
from flask import render_template, redirect, url_for, request, make_response
import jwt

from models.DAO.users import getByEmail

app = server.app

@app.route('/auth/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = getByEmail(email)

        if user is None:
            return render_template('/login/index.html', error='User not found')
        if not user.isValidPassword(password):
            return render_template('/login/index.html', error='Invalid password')
        else:
          response = make_response(redirect(url_for('dashboard')))
          token = jwt.encode({'user_id': user.id, "exp": datetime.now() + timedelta(days=30)}, os.environ['JWT_SECRET'], algorithm='HS256')
          response.set_cookie('token', token, samesite='Lax', secure=True, httponly=True)
          return response
    else:
        return render_template('/login/index.html')

@app.route('/auth/logout')
def logout():
    response = make_response(redirect(url_for('login')))
    response.delete_cookie('token')
    return response