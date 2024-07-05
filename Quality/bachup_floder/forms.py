""" all forms """
from datetime import datetime
from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import (StringField, PasswordField,
                     SubmitField, BooleanField, TextAreaField, SelectField, DateField)

from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from Quality.models import User


class RegistrationUserForm(FlaskForm):
    """ Regstration form """
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        """ validate username """
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        """ validate email """
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    """ Login form """
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    """ Regstration form """
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Update Account')

    def validate_username(self, username):
        """Validate username on account update"""
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        """Validate email on account update"""
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')

class CreateTaskForm(FlaskForm):
    """Form to create """
    title = StringField('Title', validators=[DataRequired(), Length(min=1, max=255)])
    description = TextAreaField('Description')
    status = SelectField('Status', choices=[
        ('in progress', 'In Progress'), ('completed','Completed'),('pending', 'Pending')
        ], default='in progress')
    priority = SelectField('Priority', choices=[('low', 'Low'), ('medium', 'Medium'),
                                                ('high', 'High')], default='medium')
    due_date = DateField(
        'Due Date', validators=[DataRequired()], default=datetime.utcnow ,format='%Y-%m-%d')
    submit = SubmitField('Save Task')

class UpdateTaskForm(FlaskForm):
    """Form to update a task"""
    title = StringField('Title', validators=[DataRequired(), Length(min=1, max=255)])
    description = TextAreaField('Description')
    status = SelectField('Status', choices=[
        ('in progress', 'In Progress'), ('completed','Completed'),('pending', 'Pending')
        ], default='in progress')
    priority = SelectField('Priority', choices=[('low', 'Low'), ('medium', 'Medium'),
                                                ('high', 'High')], default='medium')
    due_date = DateField(
        'Due Date', validators=[DataRequired()], default=datetime.utcnow ,format='%Y-%m-%d')
    submit = SubmitField('Update Task')


class NoteForm(FlaskForm):
    """Form to create or update a note"""
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Save Note')

class NoteFormUpdate(FlaskForm):
    """Form to create or update a note"""
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Update Note')





class TaskCollaboratorForm(FlaskForm):
    """Form to add a collaborator to a task"""
    user_id = SelectField('User', coerce=int, validators=[DataRequired()])
    submit = SubmitField('Add Collaborator')


class RequestResetPassword(FlaskForm):
    """ request reset password """
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')
    def validate_email(self, email):
        """Validate email on account update"""
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user is None:
                raise ValidationError('There is no email, please Register.')

class RequestResetForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email. You must register first.')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')

class NCForm(FlaskForm):
    date_detection = DateTimeField('Date Detection', validators=[DataRequired()])
    origine = StringField('Origine', validators=[DataRequired()])
    etape_detection = StringField('Etape Detection', validators=[DataRequired()])
    declencheur = StringField('Declencheur', validators=[DataRequired()])
    provenance = StringField('Provenance', validators=[DataRequired()])
    designation = StringField('Designation', validators=[DataRequired()])
    version_formule = StringField('Version Formule', validators=[DataRequired()])
    code_mp = StringField('Code MP', validators=[DataRequired()])
    n_lot = StringField('N Lot', validators=[DataRequired()])
    dte_h_production = DateTimeField('Date/Heure Production', validators=[DataRequired()])
    dte_h_chargement = DateTimeField('Date/Heure Chargement', validators=[DataRequired()])
    enlevement = StringField('Enlevement', validators=[DataRequired()])
    transporteur = StringField('Transporteur', validators=[DataRequired()])
    matricule = StringField('Matricule', validators=[DataRequired()])
    qte_commandee = StringField('Qte Commandee', validators=[DataRequired()])
    qte_livree = StringField('Qte Livree', validators=[DataRequired()])
    qte_concernee = StringField('Qte Concernee', validators=[DataRequired()])
    qte_retour = StringField('Qte Retour', validators=[DataRequired()])
    lieu_stockage = StringField('Lieu Stockage', validators=[DataRequired()])
    equipement = StringField('Equipement', validators=[DataRequired()])
    motif = StringField('Motif', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    decision = StringField('Decision', validators=[DataRequired()])
    criticite = StringField('Criticite', validators=[DataRequired()])
    image = StringField('Image')
    commentaire = TextAreaField('Commentaire')
    statut_nc = StringField('Statut NC', validators=[DataRequired()])
    date_statut = DateTimeField('Date Statut', validators=[DataRequired()])
    necessite_traitement = BooleanField('Necessite Traitement')
    assigned_to = SelectField('Assigned To', coerce=int)
    submit = SubmitField('Submit')