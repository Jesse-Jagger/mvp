from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User
from flask_login import current_user

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    first_name = StringField('first_name', validators=[DataRequired()])
    other_name = StringField('other_name', validators=[DataRequired()])
    last_name = StringField('last_name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    address = StringField('Address', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Sorry, That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Sorry, That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    first_name = StringField('first_name', validators=[DataRequired()])
    other_name = StringField('other_name', validators=[DataRequired()])
    last_name = StringField('last_name', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Sorry, That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Sorry, That email is taken. Please choose a different one.')
            
    def validate_phone(self, phone):
        if phone.data != current_user.phone:
            user = User.query.filter_by(phone=phone.data).first()
            if user:
                raise ValidationError('Sorry, That phone number is taken. Please choose a different one.')
            
    def validate_address(self, address):
        if address.data != current_user.address:
            user = User.query.filter_by(address=address.data).first()
            if user:
                raise ValidationError('Sorry, That address is taken. Please choose a different one.')
    
    def validate_first_name(self, first_name):
        if first_name.data != current_user.first_name:
            user = User.query.filter_by(first_name=first_name.data).first()
            if user:
                raise ValidationError('Sorry, That first name is taken. Please choose a different one.')
            
    def validate_last_name(self, last_name):
        if last_name.data != current_user.last_name:
            user = User.query.filter_by(last_name=last_name.data).first()
            if user:
                raise ValidationError('Sorry, That last name is taken. Please choose a different one.')
            
    def validate_other_name(self, other_name):  
        if other_name.data != current_user.other_name:
            user = User.query.filter_by(other_name=other_name.data).first()
            if user:
                raise ValidationError('Sorry, That other name is taken. Please choose a different one.')
