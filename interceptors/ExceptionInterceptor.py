from exceptions.NotAuthException import NotAuthException
from exceptions.NotFoundException import NotFoundException
from utils.ExceptionBuilder import ExceptionBuilder
from utils.ResponseBuilder import ResponseBuilder


class ExceptionInterceptor:
    def error(self, error: Exception):
        return ResponseBuilder.failed(ExceptionBuilder.build(error))

    def notFound(self, error: NotFoundException):
        return ResponseBuilder.failedNotFound(ExceptionBuilder.build(error))

    def notAuth(self, error: NotAuthException):
        return ResponseBuilder.responseConfig(error, statusBody = {"message": "No authority in route", "status": 403})