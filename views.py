# coding=utf-8
import os
import webapp2
import jinja2
import json
from google.appengine.ext import ndb
from forms import ProfileForm
from google.appengine.api import users
from models import DataList, UserProfile, UserDestribution, TopListWord, User
from webapp2_extras.appengine.users import login_required


def configure_jinja2_environment():
    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates'),
        extensions=['jinja2.ext.autoescape'],
        autoescape=True)


JINJA_ENVIRONMENT = configure_jinja2_environment()

class Jinja2Handler(webapp2.RequestHandler):
    """
        BaseHandler for all requests all other handlers will
        extend this handler

    """
    template_name = None
    @webapp2.cached_property
    def jinja2(self):
        return jinja2.get_jinja2(app=self.app)

    def get_messages(self, key='_messages'):
        try:
            return self.request.session.data.pop(key)
        except KeyError:
            return None

    def render_template(self, template_name, template_values={}):
        messages = self.get_messages()
        if messages:
            template_values.update({'messages': messages})
        self.response.write(self.jinja2.render_template(
            template_name, **template_values))

class DigitalizationView(Jinja2Handler):
    template_name = 'digitalization.html'

    def get_template_values(self):
        template_values = super(DigitalizationView, self).get_template_values()
        digitalization = DataList.query().filter(DataList.type_name == 'digitalization')
        template_values['digitalization_list'] = digitalization
        return template_values



class InformationView(WJinja2Handler):
    template_name = 'information.html'

    def get_template_values(self):
        template_values = super(InformationView, self).get_template_values()
        information = DataList.query().filter(DataList.type_name == 'information')
        template_values['information_list'] = information
        return template_values


class MotivationView(Jinja2Handler):
    template_name = 'motivation.html'

    def get_template_values(self):
        template_values = super(MotivationView, self).get_template_values()
        motivation = DataList.query().filter(DataList.type_name == 'motivation')
        template_values['motivation_list'] = motivation
        return template_values


class About(Jinja2Handler):
    template_name = 'about.html'


class Report1View(Jinja2Handler):
    template_name = 'report1.html'
    login_required = True

    def get_template_values(self):
        template_values = super(Report1View, self).get_template_values()
        report_data = TopListWord.query()
        template_values['report_data'] = report_data
        return template_values


class Report2View(Jinja2Handler):
    template_name = 'report2.html'
    login_required = True

    def get_template_values(self):
        template_values = super(Report2View, self).get_template_values()
        report_data = UserDestribution.query()
        template_values['report_data'] = report_data
        return template_values


class UserProfileView(Jinja2Handler):
    template_name = 'myprofile.html'
    login_required = True

    def get_template_values(self):
        template_values = super(UserProfileView, self).get_template_values()
        form = ProfileForm()
        template_values['form'] = form
        return template_values

    def save_profile(self):
        user_obj_key = ndb.Key(User, users.get_current_user().email())
        user_profile_obj = UserProfile(
            user=user_obj_key,
            leadership_role=self.request.get('country'),
            story=self.request.get('story'),
            keyword=self.request.get('keyword'),
            comment=self.request.get('comment'),
        )
        user_profile_obj.put()
        
    def post(self):
        form = ProfileForm(self.request.POST)
        success_message = ''
        if form.validate():
            self.save_profile()
            form = ProfileForm()
            success_message = 'Your request submited successfully'

        template = JINJA_ENVIRONMENT.get_template(self.get_template_name())
        template_value = self.get_template_values()
        template_value['success_message'] = success_message
        self.response.write(template.render(template_value))


app = webapp2.WSGIApplication(
    [
        ('/', About),
        ('/digitalization', DigitalizationView),
        ('/information', InformationView),
        ('/motivation', MotivationView),
        ('/report1', Report1View),
        ('/report2', Report2View),
        ('/MyProfile', UserProfileView),
    ],
    debug=True)
