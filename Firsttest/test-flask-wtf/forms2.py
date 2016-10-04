# -*- coding: UTF-8 -*-
"""(forms1.py) Flask-WTF Example 1: Login Form"""
from flask_wtf import Form  
      # import from flask_wtf, NOT wtforms
from wtforms import StringField, PasswordField  
      # import fields from wtforms
from wtforms.validators import InputRequired, Length
      # import field input validators from wtforms

# Define the LoginRorm class by sub-classing Form
class LoginForm(Form):
   # This form contains two fields with validators
   username = StringField(u'User Name:', validators=[InputRequired(), Length(max=20)])
   passwd = PasswordField(u'Password:', validators=[Length(min=4, max=16)])