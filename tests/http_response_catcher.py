# -*- coding: utf-8 -*-

"""
    tests.http_response_catcher

    This file was automatically generated for Tango Card, Inc. by APIMATIC v2.0 ( https://apimatic.io ).
"""

from raas.http.http_call_back import HttpCallBack

class HttpResponseCatcher(HttpCallBack):

    """A class used for catching the HttpResponse object from controllers.
    
    This class inherits HttpCallBack and implements the on_after_response
    method to catch the HttpResponse object as returned by the HttpClient
    after a request is executed.

    """
    def on_before_request(self, request):
        pass;

    def on_after_response(self, context):
        self.response = context.response



