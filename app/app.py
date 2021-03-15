import logging
import datetime
import requests
from flask import Flask, request, jsonify
from flask.views import MethodView
from .utils.response import response_builder
from .utils.convert import calculate_fx
from .utils.extract import yield_data, get_url_params
from .utils.errors import UnprocessableEntity, ServiceUnavailable


app = Flask(__name__, static_folder=None)
app.logger.setLevel(logging.DEBUG)
app.config["JSON_SORT_KEYS"] = False


FX_DATA_URL = "http://fxdata:5200/getRates"


@app.errorhandler(UnprocessableEntity)
def handle_unprocessable_entity(error):
    app.logger.debug("required parameters are missing!!")
    payload = dict(error.payload or ())
    payload['success'] = False
    payload['code'] = error.status
    payload['message'] = error.message
    return jsonify(payload), 422



@app.errorhandler(ServiceUnavailable)
def handle_service_unavailable(error):
    app.logger.debug(error.message)
    payload = dict(error.payload or ())
    payload['success'] = False
    payload['code'] = error.status
    payload['message'] = error.message
    return jsonify(payload), 503


class HealthCheck(MethodView):
    def get(self):
        app.logger.debug("entered get method in HealthCheck")
        return {}


class FxConvertView(MethodView):
    """FxConvertView"""

    def get(self) -> dict:
        app.logger.debug("entered get method in FxConvert")

        params, err = get_url_params()
        if params["date"] == None:
            date = datetime.datetime.now().date().strftime("%Y-%m-%d")
        else:
            date = params["date"]

        if err:
            raise UnprocessableEntity("Missing required parameters")

        req = requests.get(
            FX_DATA_URL
            + "?from={}&to={}&date={}".format(
                params["from"], params["to"], date
            )
        )

        if req.status_code != 200:
            raise ServiceUnavailable("failure from fxdata with status {}".format(req.status_code))

        data = req.json()
        app.logger.info("result from fxdata: {}".format(data))

        try:
            result = calculate_fx(str(params["amount"]), str(data['detail']['rate']))
        except Exception as e:
            app.logger.error(e)
            raise ServiceUnavailable("failure: {}".format(e))

        response = response = response_builder(
            success=True,
            from_=params["from"],
            to=params["to"],
            amount=params["amount"],
            date=date,
            result=str(result)
        )

        return response.to_dict(), 200


app.add_url_rule("/convert", view_func=FxConvertView.as_view("conversion_view"))
app.add_url_rule("/healthcheck", view_func=HealthCheck.as_view("healthcheck_view"))
