from functools import wraps
import os
from flask import redirect, request, url_for
from models.DAO.users import getByID
import jwt

def authentication():
  def wrapper(func):
      @wraps(func)
      def middleware(*args, **kwargs):
          token = request.cookies['token']
          if not token:
              return redirect(url_for('login', error='Not logged in'))

          try:
            data = jwt.decode(token, os.environ['JWT_SECRET'], algorithms=['HS256'])
            user = getByID(data.get('user_id'))
            if not user:
                raise Exception('User not found')
            return func(user, *args, **kwargs)
          except jwt.ExpiredSignatureError:
              return redirect(url_for('login', error='Session expired'))
          except Exception as e:
              return redirect(url_for('login', error=str(e)))
      return middleware
  return wrapper



