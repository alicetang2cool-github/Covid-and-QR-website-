from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo



class StateForm(FlaskForm):
    States = SelectField('Select a State',choices = [('Los Angeles','Los Angeles'),('Alabama', 'Alabama'),('Alaska','Alaska'),('Arizona','Arizona'),('Arkansas','Arkansas'),
                                                    ('California','California'),('Colorado','Colorado'),('Connecticut','Connecticut'),('Delaware','Delaware'),
                                                    ('Florida','Florida'),('Georgia','Georgia'),('Hawaii','Hawaii'),('Idaho','Idaho'),
                                                    ('Illinois','Illinois'),('Indiana','Indiana'),('Iowa','Iowa'),('Kansas','Kansas'),
                                                    ('Kentucky','Kentucky'),('Louisiana','Louisiana'),('Maine','Maine'),('Maryland','Maryland'),
                                                    ('Massachusetts','Massachusetts'),('Michigan','Michigan'),('Minnesota','Minnesota'),('Mississippi','Mississippi'),
                                                    ('Missouri','Missouri'),('Montana','Montana'),('Nebraska','Nebraska'),('Nevada','Nevada'),
                                                    ('New Hampshire','New Hampshire'),('New Jersey','New Jersey'),('New Mexico','New Mexico'),('New York','New York'),
                                                    ('North Carolina','North Carolina'),('North Dakota','North Dakota'),('Ohio','Ohio'),('Oklahoma','Oklahoma'),
                                                    ('Oregon','Oregon'),('Pennsylvania','Pennsylvania'),('Rhode Island','Rhode Island'),('South Carolina','South Carolina'),
                                                    ('South Dakota','South Dakota'),('Tennessee','Tennessee'),('Texas','Texas'),('Utah','Utah'),
                                                    ('Vermont','Vermont'),('Virginia','Virginia'),('Washington','Washington'),('West Virginia','West Virginia'),
                                                    ('Wisconsin','Wisconsin'),('Wyoming','Wyoming')])
    submit = SubmitField('Search')