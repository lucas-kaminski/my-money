from middlewares.authenticate import authentication
from server.instance import server

app = server.app

@app.route('/dashboard')
@authentication()
def dashboard(user):
    return 'dashboard'

