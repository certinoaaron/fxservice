import logging
import datetime
import requests
from flask import Flask, request, jsonify
from flask.views import MethodView
from .utils.response import response_builder
from .utils.convert import calculate_fx
from .utils.extract import yield_data, get_url_params


app = Flask(__name__, static_folder=None)
app.logger.setLevel(logging.DEBUG)
app.config["JSON_SORT_KEYS"] = False


FX_DATA_URL = "http://fxdata:5200/getRates"


class HealthCheck(MethodView):
    def get(self):
        app.logger.debug("entered get method in HealthCheck")
        return {}


class FxConvertView(MethodView):
    """FxConvertView"""

    def get(self) -> dict:
        app.logger.debug("entered get method in FxConvert")

        params, err = get_url_params()
        if err:
            app.logger.debug("required parameters are missing!! {}".format(params))
            app.logger.info(
                "sending 422 Unprocessable Entity status to client -> {}".format(
                    request.remote_addr
                )
            )
            response = response_builder(
                success=False,
                from_=params["from"],
                to=params["to"],
                amount=params["amount"],
            )
            return response.to_dict(), 422

        # TODO: improve this service call

        if params["date"] == None:
            date = datetime.datetime.now().date()
        else:
            date = params["date"]

        req = requests.get(
            FX_DATA_URL
            + "?from={}&to={}&date={}".format(
                params["from"], params["to"], date
            )
        )

        if req.status_code != 200:
            app.logger.error(
                "failure from fxdata with status {}".format(req.status_code)
            )
            app.logger.info(
                "forwarding fxdata status code on to client -> {}".format(
                    request.remote_addr
                )
            )
            response = response_builder(
                success=False,
                from_=params["from"],
                to=params["to"],
                amount=params["amount"],
                date=date
            )
            return response.to_dict(), req.status_code

        data = req.json()

        try:
            result = calculate_fx(str(params["amount"]), str(data['rate']))
        except requests.exceptions.ConnectionError as e:
            app.logger.error(e)
            app.logger.error("Unable to connect to fxdata, returning a 503 :(")
            response = response_builder(
                success=False,
                from_=params["from"],
                to=params["to"],
                amount=params["amount"],
                date=date
            )
            return response.to_dict(), 503

        except Exception as e:
            app.logger.error(e)
            app.logger.error("This is a catch all error")
            response = response_builder(
                success=False,
                from_=params["from"],
                to=params["to"],
                amount=params["amount"],
                date=date
            )
            return response.to_dict(), 503


        response = response = response_builder(
            success=True,
            from_=params["from"],
            to=params["to"],
            amount=params["amount"],
            date=date,
            result=result
        )
        return response.to_dict(), 200


app.add_url_rule("/convert", view_func=FxConvertView.as_view("conversion_view"))
app.add_url_rule("/healthcheck", view_func=HealthCheck.as_view("healthcheck_view"))
