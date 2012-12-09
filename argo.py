#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '1.0'
__author__ = 'mopodo (hjiale@gmail.com)'

'''
Python client SDK for Argo BBS
'''
import json
import urllib, urllib2, cookielib
import logging

class APIError(StandardError):
    '''
    raise APIError if got failed json message.
    '''
    def __init__(self, error, error_code):
        self.error = error
        self.error_code = error_code
        StandardError.__init__(self, error)

    def __str__(self):
        return 'APIError: {}: {}'.format(self.error_code, self.error)

class APIClient(object):
    '''
    API client using synchronized invocation.
    '''
    def __init__(self, domain='argolab.org'):
        self.api_url = 'http://{}/'.format(domain)
        self.cookie = cookielib.CookieJar() 
        self._HTTP_GET = 0
        self._HTTP_POST = 1
        # self.get = HttpObject(self, _HTTP_GET)
        # self.post = HttpObject(self, _HTTP_POST)
        # self.upload = HttpObject(self, _HTTP_UPLOAD)
    
    def __getattr__(self, attr):
        postfix = attr.split('_')
        method = self._HTTP_GET if postfix[0] == 'get' else self._HTTP_POST
        
        def wrap(**kw):
            return self._http_call('{}{}'.format(self.api_url, '/'.join(postfix[1:])), method, **kw)
        return wrap


    def _http_call(self, url, method, **kw):
        '''
        http request handling with cookie
        '''
        logging.info('{}: {}'.format('GET' if not method else 'POST', url))
        params = urllib.urlencode(kw)
        http_url = '{}?{}'.format(url, params) if method == self._HTTP_GET else url
        http_body = None if method == self._HTTP_GET else params
        req = urllib2.Request(http_url, data = http_body)
        ckproc = urllib2.HTTPCookieProcessor(self.cookie)
        opener = urllib2.build_opener(ckproc)
        try:
            resp = opener.open(req)
            body = resp.read()
            # r = json.loads(body, object_hook=_obj_hook)
            r = json.loads(body)
            if r['success'] == '':
                raise APIError(r.get('error', ''), r.get('code', ''))
            resp.close()
            return r
        except urllib2.HTTPError, e:
            # r = json.loads(e.read(), object_hook=_obj_hook)
            r = json.loads(e.read())
            if r['success'] == '':
                raise APIError(r.get('error', ''), r.get('code', ''))
            raise
