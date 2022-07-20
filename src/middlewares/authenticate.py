from functools import wraps
import os
from flask import redirect, request, url_for
from models.DAO.users import getById
import jwt

def authentication():
  def wrapper(func):
      @wraps(func)
      def middleware(*args, **kwargs):
          token = request.cookies['token']
          if not token:
              return redirect(url_for('login', error='You must be logged in'))

          try:
            data = jwt.decode(token, os.environ['JWT_SECRET'], algorithms=['HS256'])
            user = getById(data.get('user_id'))
            if not user:
                raise
            return func(user, *args, **kwargs)
          except:
            return redirect(url_for('login', error='You must be logged in'))
      return middleware
  return wrapper



