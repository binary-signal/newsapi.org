#!/usr/bin/env python
# -*- coding: utf-8 -*-

class NewsApiError(Exception):
    """ basic exception for errors raised by News Api"""

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class BadRequest(NewsApiError):
    def __init__(self, *args, **kwargs):
        NewsApiError.__init__(self, *args, **kwargs)


class UnauthorizedRequest(NewsApiError):
    def __init__(self, *args, **kwargs):
        NewsApiError.__init__(self, *args, **kwargs)


class ApiRateLimit(NewsApiError):
    def __init__(self, *args, **kwargs):
        NewsApiError.__init__(self, *args, **kwargs)


class ServerError(NewsApiError):
    def __init__(self, *args, **kwargs):
        NewsApiError.__init__(self, *args, **kwargs)
