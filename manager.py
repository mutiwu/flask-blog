from flask_script import Manager, Server
import main

manager = Manager(main.app)

manager.add_command("server", Server())


@manager.shell
def make_shell_context():
    """Create a python cli

    :return: Default import object
    """
    return dict(app=main.app)


if __name__ == '__main__':
    manager.run()