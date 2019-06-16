from wtforms import Form, StringField, validators


class ProfileForm(Form):
    leadership_role = StringField('Your leadership role')
    story = StringField('My favourite story', [validators.InputRequired()])
    keyword = StringField('My favourite keyword', [validators.InputRequired()])
    comment = StringField('Recommendations', [validators.InputRequired()])
