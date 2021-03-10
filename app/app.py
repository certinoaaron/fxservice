import logging
import requests
from flask import Flask, request, jsonify
from flask.views import MethodView
from .utils.response import 
from .utils.extract import yield_data, get_url_params


app = Flask(__name__, static_folder=None)
app.logger.setLevel(logging.DEBUG)


class HealthCheck(MethodView):

    def get(self):
        app.logger.debug("entered get method in HealthCheck")
        return 200


class FxConvertView(MethodView):
    """FxConvertView"""

    def get(self) -> dict:
        """containing

        :return: converted currency
        :rtype: dict
        """
        app.logger.debug("entered get method in FxConvert")

        params = get_url_params()
        if not params:

            # TODO: add response builder here 
            return { "success": False }, 422

        

        

        return {"success": True}, 200


app.add_url_rule("/convert", view_func=FxConvertView.as_view("conversion_view"))
app.add_url_rule("/healthcheck", view_func=HealthCheck.as_view("healthcheck_view"))