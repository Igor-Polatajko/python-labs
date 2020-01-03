from lab_15_3.core.FlaskBaseController import route


class ApiController:
    @route('/api')
    def hello1(self):
        return "Hello World !"

    def m(self):
        pass
