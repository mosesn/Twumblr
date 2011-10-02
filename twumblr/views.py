from twumblr.models import DBSession
from twumblr.models import MyModel

def my_view(request):
    dbsession = DBSession()
    root = dbsession.query(MyModel).filter(MyModel.name==u'root').first()
    return {'root':root, 'project':'twumblr'}
