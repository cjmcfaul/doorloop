import json
import requests
import logging
from urllib.parse import urlencode

logger = logging.getLogger('__name__')


class DoorLoopBase:
    endpoint_base = ''

    def __init__(self, connector, validator):
        self.connector = connector
        self.validator = validator

    def pagination(self, func, **kwargs):
        page = 1
        total_pages = 2
        while page < total_pages:
            kwargs['page'] = page
            result = func(**kwargs)
            if result:
                total_pages = result[0].get('total_pages') + 1
            page += 1
            yield result

    def sorting(self, func, **kwargs):
        pass

    def filter(self, func, **kwargs):
        pass


class DoorLoopConnector:

    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = f"https://app.doorloop.com/api"

    def get_url(self, endpoint, query_params):
        return f"{self.base_url}{endpoint}{self.get_url_query_params(query_params)}"

    def get_url_query_params(self, params):
        if isinstance(params, dict):
            # url encode query parameters
            return f"?{urlencode(params)}"
        return ''

    def __getattr__(self, name):
        def f(endpoint, data=None, **kwargs):
            # validate function called is a valid request method
            upper_name = name.upper()
            if upper_name not in ('GET', 'POST', 'PUT', 'PATCH', 'HEAD',
                                  'DELETE', 'OPTIONS', 'CONNECT'):
                return name
            # Add Header Data to Request
            if kwargs.get('headers'):
                # if headers passed to function
                if not kwargs['headers'].get('Accept'):
                    kwargs['headers']['Accept'] = 'application/json'
                if not kwargs['headers'].get('Authorization'):
                    kwargs['headers']['Authorization'] = f"Bearer {self.api_key}"
                if not kwargs['headers'].get('User-Agent'):
                    kwargs['headers']['User-Agent'] = "PostmanRuntime/7.26.8"
            else:
                # set default headers if not passed
                kwargs['headers'] = {
                    'Accept': 'application/json',
                    'Authorization': f"Bearer {self.api_key}",
                    'Content-Type': 'application/json',
                    'User-Agent': "PostmanRuntime/7.26.8",
                }

            if upper_name in ('POST', 'PUT') and not kwargs['headers'].get('Content-Type'):
                # Add Content-Type header when required by DoorLoop API
                kwargs['headers']['Content-Type'] = 'application/json'

            query_params = None
            if kwargs.get('query_params'):
                query_params = kwargs['query_params']
                del kwargs['query_params']

            if data:
                if kwargs['headers'].get('Content-Type') == 'application/json':
                    # Convert data to json before sending
                    kwargs['data'] = json.dumps(data)
                else:
                    kwargs['data'] = data
            return DoorLoopConnector.api_call(upper_name, self.get_url(endpoint, query_params), **kwargs)

        return f

    @staticmethod
    def api_call(upper_name, api_endpoint, **kwargs):
        def f(method_name, endpoint, **fkwargs):
            response = requests.request(method_name, endpoint, **fkwargs)
            return response
        return f(upper_name, api_endpoint, **kwargs)


class DoorLoopValidator:
    def __init__(self):
        pass

    def __call__(self, response):
        self.response = response
        return self

    def validate(self):
        status_code = self.response.status_code
        try:
            data = self.response.json()
        except Exception as e:
            logger.info(str(e))
            data = {}

        if isinstance(data, dict) and data.get('status') and (
                isinstance(data.get('status'), int) or data.get('status').isdigit()):
            status_code = int(data.get('status'))

        if status_code < 200 or status_code > 299:
            error_message = data.get('message') if data else None
            if not error_message and data and 'base' in data and isinstance(data['base'], list):
                data = ';'.join(data['base'])
            if not error_message and self.response.text:
                data = self.response.text
            logger.error(f'{status_code} Response: {data}')
        return data
