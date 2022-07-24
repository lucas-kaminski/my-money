from flask import Flask


class Server:
    def __init__(self) -> None:
        self.app = Flask(
            __name__, template_folder="../templates", static_folder="../static"
        )

    def run(self) -> None:
        self.app.run(host="0.0.0.0", port=5000, debug=True)


server = Server()
