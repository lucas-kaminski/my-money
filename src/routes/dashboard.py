from middlewares.authenticate import authentication
from server.instance import server
from flask import render_template
from models.DAO.entries import getAllEntriesOfUser
app = server.app

@app.route('/dashboard')
@authentication()
def dashboard(user):
    entries = getAllEntriesOfUser(user.id)
    print(entries[0].__dict__)
    return render_template('/dashboard/index.html', entries=entries)

