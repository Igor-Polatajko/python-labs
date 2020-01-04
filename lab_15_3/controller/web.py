from flask import render_template, redirect, request

from lab_15_3.core.FlaskBaseController import route
from lab_15_3.service.CurrencyNumberToWrittenFormTransformService import CurrencyNumberToWrittenFormTransformService


class WebController:
    def __init__(self):
        self.transform_service = CurrencyNumberToWrittenFormTransformService()

    @route('/', methods=['GET'])
    def get(self):
        value = request.args.get("value")
        result = None
        error = None
        if value:
            try:
                result = self.transform_service.transform(value)
            except ValueError as e:
                error = str(e)

        return render_template("index.html", result=result, error=error)
