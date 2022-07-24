from middlewares.authenticate import authentication
from server.instance import server
from flask import render_template
from models.DAO.entries import getAllEntriesOfUser

app = server.app


@app.route("/dashboard")
@authentication()
def dashboard(**context):
    return render_template("/dashboard/index.html", **context)


@app.route("/dashboard/banks")
@authentication()
def banks(**context):
    return render_template("/dashboard/banks/index.html", **context)


@app.route("/dashboard/entries")
@authentication()
def entries(**context):
    user = context.get("user")
    entries = getAllEntriesOfUser(user.id)
    context = {"entries": entries, **context}
    print(context)
    return render_template("/dashboard/entries/index.html", **context)
