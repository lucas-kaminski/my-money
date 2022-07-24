from server.instance import server
from dotenv import load_dotenv
from routes import dashboard, auth, api

if __name__ == "__main__":
    load_dotenv()
    # delete route file
    with open("routes.txt", "w") as f:
        f.write("")

    with open("routes.txt", "a") as f:
        for r in server.app.url_map._rules:
            f.write(
                str(r.rule)
                + " - "
                + str(r.endpoint)
                + " - "
                + r.methods.__str__()
                + "\n"
            )

    server.run()
