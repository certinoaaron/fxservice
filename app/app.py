import logging
import requests
from flask import Flask, request, jsonify
from flask.views import MethodView
from .utils.response import response_builder
from .utils.extract import yield_data, get_url_params


app = Flask(__name__, static_folder=None)
app.logger.setLevel(logging.DEBUG)
app.config["JSON_SORT_KEYS"] = False


class HealthCheck(MethodView):
    def get(self):
        app.logger.debug("entered get method in HealthCheck")
        return {}


class FxConvertView(MethodView):
    """FxConvertView"""

    def get(self) -> dict:
        """ returns converted value

        :return: converted currency
        :rtype: dict
        """
        app.logger.debug("entered get method in FxConvert")

        params = get_url_params()
        if not params:
            app.logger.debug("required parameters are missing!! {}".format(params))
            response = response_builder(
                success=False,
                from_=params["from"],
                to=params["to"],
                amount=params["amount"],
            )
            return response.to_dict(), 422





            

        response = response = response_builder(
            success=True,
            from_=params["from"],
            to=params["to"],
            amount=params["amount"],
        )
        return response.to_dict(), 200


app.add_url_rule("/convert", view_func=FxConvertView.as_view("conversion_view"))
app.add_url_rule("/healthcheck", view_func=HealthCheck.as_view("healthcheck_view"))
-