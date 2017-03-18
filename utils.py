from flask import Response, request


def add_basic_auth(blueprint, username, password, realm='RQ Dashboard'):
    '''Add HTTP Basic Auth to a blueprint.
    Note this is only for casual use!
    '''
    @blueprint.before_request
    def basic_http_auth(*args, **kwargs):
        auth = request.authorization
        if (auth is None or auth.password != password or auth
                .username != username):

            return Response(
                'Please login',
                401,
                {'WWW-Authenticate': 'Basic realm="{0}"'.format(realm)})
