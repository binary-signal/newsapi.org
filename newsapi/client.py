#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .objects import Source, Article
from .exceptions import *
import requests
import json
import logging

module_logger = logging.getLogger('news-api')


class Client:
    api = 'https://newsapi.org/v2/'

    def __init__(self, api_key):
        self.logger = logging.getLogger("news-api")
        if not isinstance(api_key, str):
            self.logger.error("Api key must be string type")
            raise TypeError("Api key must be string type")
        self.api_key = api_key

    def api_call(self, endpoint, payload={}):
        """ low level api call to newsapi.org """

        url = self.api + endpoint
        payload['apiKey'] = self.api_key
        try:
            resp = requests.get(url, params=payload)
        except requests.exceptions as e:
            logging.error(e)
            print(e)
            return
        response = json.loads(resp.text)

        """ on error """
        if resp.status_code != 200:
            self.logger.error("{} {} {}".format(response['message'], response['status'], response['code'], ))
            if resp.status_code == 400:
                raise BadRequest(response['message'])
            elif resp.status_code == 401:
                raise UnauthorizedRequest(response['message'])
            elif resp.status_code == 429:
                raise ApiRateLimit(response['message'])
            elif resp.status_code == 500:
                raise ServerError(response['message'])
            else:
                """ capture a generic error return code"""
                raise NewsApiError(response['message'])

        """ on success """
        return response

    def top_headlines(self, source=None, country=None, category=None, q=None, pageSize=20, page=None):
        """

        :param source:
        :param country:
        :param category:
        :param q:
        :param pageSize:
        :param page:
        :return:
        """
        response = self.api_call(endpoint='top-headlines', payload={'sources': source,
                                                                    'country': country,
                                                                    'category': category,
                                                                    'q': q,
                                                                    'pageSize': pageSize,
                                                                    'page': page})
        return [Article(**s) for s in response['articles']], response['totalResults']

    def everything(self, q=None, sources=None, domains=None, from_=None, to=None,
                   language=None, sortBy=None, pageSize=None, page=None):
        """

        :param q:
        :param sources:
        :param domains:
        :param from_:
        :param to:
        :param language:
        :param sortBy:
        :param pageSize:
        :param page:
        :return:
        """

        response = self.api_call(endpoint='everything', payload={'q': q,
                                                                 'sources': sources,
                                                                 'domains': domains,
                                                                 'from': from_,
                                                                 'to': to,
                                                                 'language': language,
                                                                 'sortBy': sortBy,
                                                                 'pageSize': pageSize,
                                                                 'page': page})
        return [Article(**s) for s in response['articles']]

    def sources(self, category=None, language=None, country=None):
        """
        Provides a list of the news sources and blogs available on News API.
        You will need this to programmatically locate the identifier for the
        source you want articles from when querying the /articles endpoint.

        :param category:
        :param language: optional) - The category you would like to get sources for.
        :param country: (optional) The 2-letter ISO 3166-1 code of the country
        :return:
        """

        data = self.api_call(endpoint='sources', payload={'category': category,
                                                          'language': language,
                                                          'country': country})

        return [Source(**s) for s in data['sources']]
