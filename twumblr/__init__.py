from pyramid.config import Configurator

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
#    config.add_static_view('static', 'twumblr:static', cache_max_age=3600)
    config.add_route('oauth', '/tumblr_auth')
    config.add_view('twumblr.views.obtain_oauth',
                    route_name='oauth',
                    renderer='templates/oauthtemp.pt')
    return config.make_wsgi_app()
