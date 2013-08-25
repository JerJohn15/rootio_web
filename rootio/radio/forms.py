# -*- coding: utf-8 -*-

from flask.ext.wtf import Form
from wtforms import HiddenField, SubmitField
from wtforms import StringField
from wtforms_components import TimeField
from wtforms.ext.sqlalchemy.orm import model_form
from .models import Station, Program, Person

#define field help text here, instead of in model info
StationFormBase = model_form(Station, base_class=Form, field_args={
        'name':{'description':'Name or callsign of station'},
        'frequency':{'description':'Station broadcast frequency'},
        'phone':{'description': 'Station cloud telephone number'},
        'contact':{'description': 'Primary local contact'},
    },
    exclude=['owner_id',]) #this will be added in the view
class StationForm(StationFormBase):
    submit = SubmitField(u'Save')

class ProgramForm(Form):
    #can't use model_form, because it won't create from wtforms_component TimeField
    name = StringField(description="") #different syntax here, pass description directly to field constructor
    length = TimeField()
    language = StringField()
    #program_type = 
    submit = SubmitField(u'Save')

PersonFormBase = model_form(Person, base_class=Form)
class PersonForm(PersonFormBase):
    submit = SubmitField(u'Save')
