from google.appengine.ext import ndb
from engineauth import models
class CustomUser(models.User):
    @classmethod
    def _get_kind(cls):
        # Override the datastore entity name.
        # The string that is returned here will be used to name the entity
        # group in the datastore
        return 'EAUser'

class User(ndb.Model):
    email = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now=True)


class DataList(ndb.Model):
    type_name = ndb.StringProperty()
    description = ndb.TextProperty()
    link = ndb.TextProperty()


class UserProfile(ndb.Model):
    leadership_role = ndb.StringProperty()
    story = ndb.StringProperty()
    keyword = ndb.StringProperty()
    comment = ndb.StringProperty()
    user = ndb.KeyProperty(kind=User)

class TopListWord(ndb.Model):
    location = ndb.StringProperty()
    parent = ndb.StringProperty()
    size = ndb.StringProperty()
    color = ndb.StringProperty()

class UserDestribution(ndb.Model):
    task = ndb.StringProperty()
    hour = ndb.StringProperty()