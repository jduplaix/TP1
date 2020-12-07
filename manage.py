from flask_script import Manager

from app.main import create_app

app = create_app()
manager = Manager(app)


@manager.command
def run():
    app.run(host="0.0.0.0", port=int("5000"), debug=True)


if __name__ == '__main__':
    manager.run()