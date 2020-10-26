from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "Hello, World! This is the next test"

    return app

if __name__ == "__main__":
    app = create_app()
    # app.run(port=5000, debug=True)
    app.run()
