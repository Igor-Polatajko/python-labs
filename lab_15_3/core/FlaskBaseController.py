from flask import Flask


def route(regex, **kwds):
    def wrapper(func):
        func.route = regex
        func.args = kwds
        return func

    return wrapper


class FlaskBaseController:
    def __init__(self, debug=False, template_folder='../view'):
        self.app = Flask(__name__, template_folder=template_folder)
        self.app.debug = debug
        self.__controllers = []

    def register_controller(self, controller):
        self.__controllers.append(controller)

    def run(self, *args, **kwds):
        self.__register_routes()
        self.app.run(*args, **kwds)

    def __register_routes(self):
        for controller in self.__controllers:
            for name in dir(controller):
                controller_attr = controller.__getattribute__(name)
                if hasattr(controller_attr, 'route'):
                    self.app.route(controller_attr.route, **controller_attr.args)(controller_attr)
