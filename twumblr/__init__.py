from pyramid.config import Configurator

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
#    config.add_static_view('static', 'twumblr:static', cache_max_age=3600)
    config.add_route('oauth', '/tumblr_auth')
    config.add_route('home', '/')
    config.add_view('twumblr.views.obtain_oauth',
                    route_name='oauth',
                    renderer='templates/oauthtemp.pt')
    config.add_view('twumblr.views.gen_url',
                    route_name='home',
                    renderer='templates/gen_url.pt')
    return config.make_wsgi_app()
