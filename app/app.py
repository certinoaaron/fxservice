import logging
import requests
from flask import Flask, request
from flask.views import MethodView
from utils.extract import yield_data


app = Flask(__name__, static_folder=None)
app.logger.setLevel(logging.DEBUG)


class FxConvertView(MethodView):
    """ FxConvertView
    """

    def get(self) -> dict:
        """ get some conversion rate

        :return: conversion rate
        :rtype: dict
        """
        app.logger.debug("entered get method in FxConvertView")

        return {"data" : data, "meta": {}}
    
    def post(self) -> dict:
        """ post data 
        """
        app.logger.debug("entered get method in FxConvertView")


        return {"data" : data, "meta": {}}


app.add_url_rule('/convert', view_func=DataView.as_view('conversion_view'))