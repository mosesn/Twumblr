from pyramid.config import Configurator

from pyramid.session import UnencryptedCookieSessionFactoryConfig

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    my_session_factory = UnencryptedCookieSessionFactoryConfig('itsaseekreet')
    config = Configurator(settings=settings, session_factory = my_session_factory)
#    config.add_static_view('static', 'twumblr:static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_view('twumblr.views.get_twitter',
                    route_name='home',
                    renderer='templates/get_twitter.pt')
    
    config.add_route('gen_url', '/gen_url')
    config.add_view('twumblr.views.gen_url',
                    route_name='gen_url',
                    renderer='templates/gen_url.pt')
    
    config.add_route('remove_twitter', '/remove_twitter')
    config.add_view('twumblr.views.remove_twitter',
                    route_name='remove_twitter',
                    renderer='templates/remove_twitter.pt')
    
    config.add_route('oauth', '/tumblr_auth')
    config.add_view('twumblr.views.obtain_oauth',
                    route_name='oauth',
                    renderer='templates/oauthtemp.pt')

    config.add_route('css', '/test.css')
    config.add_view('twumblr.views.test',
                    route_name='css',
                    renderer='templates/test.pt')

    return config.make_wsgi_app()
