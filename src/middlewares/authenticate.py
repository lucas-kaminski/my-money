from functools import wraps
import os
from flask import redirect, request, url_for
from models.DAO.users import getByID
import jwt


def authentication(must_redirect_to_page=True, redirect_to="login"):
    def wrapper(func):
        @wraps(func)
        def middleware(*args, **kwargs):
            user = None
            try:
                token = request.cookies.get("token")
                if not token:
                    raise Exception("No token")

                data = jwt.decode(token, os.environ["JWT_SECRET"], algorithms=["HS256"])
                user = getByID(data.get("user_id"))
                if not user:
                    raise Exception("User not found")
                else:
                    user.setIsAuthenticated(True)
            except jwt.ExpiredSignatureError:
                raise Exception("Session expired")
            except Exception as e:
                if must_redirect_to_page:
                    return redirect(url_for(redirect_to, error=str(e)))

            return func(*args, **{"user": user})

        return middleware

    return wrapper
