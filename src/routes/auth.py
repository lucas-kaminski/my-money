from server.instance import server
from flask import render_template, redirect, url_for, request

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
            return redirect(url_for('dashboard'))
    else:
        return render_template('/login/index.html')