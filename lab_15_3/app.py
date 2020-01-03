from lab_15_3.controller.api import ApiController
from lab_15_3.controller.web import WebController
from lab_15_3.core.FlaskBaseController import FlaskBaseController

if __name__ == "__main__":
    flask_base_controller = FlaskBaseController()
    flask_base_controller.register_controller(ApiController())
    flask_base_controller.register_controller(WebController())
    flask_base_controller.run()
