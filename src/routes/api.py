from middlewares.authenticate import authentication
from server.instance import server
from flask import render_template

app = server.app


@app.route("/api")
@authentication(must_redirect_to_page=False)
def api(**context):
    return render_template("/api/index.html", **context)
