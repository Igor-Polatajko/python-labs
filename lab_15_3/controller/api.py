from lab_15_3.core.FlaskBaseController import route
from lab_15_3.exception.interceptor import exception_interceptor
from lab_15_3.service.CurrencyNumberToWrittenFormTransformService import CurrencyNumberToWrittenFormTransformService


class ApiController:
    def __init__(self):
        self.transform_service = CurrencyNumberToWrittenFormTransformService()

    @route('/api/transform/<value>')
    @exception_interceptor
    def transform(self, value):
        return self.transform_service.transform(value)
