from server.instance import server

app = server.app

@app.route('/dashboard')
def dashboard():
    return 'dashboard'

