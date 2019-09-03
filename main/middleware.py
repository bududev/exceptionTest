# coding: utf-8

import re
import json
from HTMLParser import HTMLParser

from django.conf import settings
from exceptioinTest.celery import save_exception
import traceback


GRID_LINE = '+' + (78 * '-') + '+'


def break_string(string, every=76):
    lines = []
    for i in xrange(0, len(string), every):
        lines.append(string[i:i+every])
    return lines


def print_string(string):
    lines = break_string(string)
    for line in lines:
        print u'| {}'.format(line) + ((76 - len(line)) * ' ') + ' |'


class ExceptionMiddleware(object):

    def __init__(self, get_response):
        self.headers = {
            'User-Agent': 'github.com/vitorfs/seot'
        }
        self.get_response = get_response

    def process_exception(self, request, exception):
        if settings.DEBUG:
            representation = repr(exception)
            save_exception.delay(type(exception).__name__, str(exception), representation, exception.args, traceback.format_exc())

        return None

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response