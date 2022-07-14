from flask import Flask
from .load import load_env
load_env()

from constant.interceptors import INTERCEPTORS
from exceptions.NotFoundException import NotFoundException
from exceptions.NotAuthException import NotAuthException
from interceptors.ExceptionInterceptor import ExceptionInterceptor

def config(app: Flask, CONTROLLERS):
    interceptor = ExceptionInterceptor()
    
    for k in CONTROLLERS.keys():
        eval("app.register_blueprint(CONTROLLERS.get(k)." + str(k) + "_routes, url_prefix='/api')")
    for k, v in INTERCEPTORS.items():
        eval("app.register_error_handler(" + str(v) + ", interceptor." + str(k) + ")")