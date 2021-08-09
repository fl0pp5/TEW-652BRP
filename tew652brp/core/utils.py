urls = [
    'login.ccp',
    'get_set.ccp',
]


def ccp_act(act, **params):
    def _ccp_act(func):
        def wrapper(session, url, data):
            data['ccp_act'] = act
            for param in params:
                data[param] = params[param]
            return func(session, url, data)
        return wrapper
    return _ccp_act


def make_url(base_url, action):
    return f'{base_url}/{action}'


def make_routes(base_url):
    return {url.split('.')[0]: make_url(base_url, url) for url in urls}
