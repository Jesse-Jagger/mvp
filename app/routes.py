from flask import render_template, url_for, flash, redirect, request, Blueprint, jsonify
from app import db, bcrypt
from app.forms import RegistrationForm, LoginForm, UpdateAccountForm
from app.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

@main.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            form = RegistrationForm(data=data, meta={'csrf': False})  # Disable CSRF for JSON requests
            if form.validate():
                hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
                user = User(first_name=form.username.data, other_names=form.other_name.data, last_name=form.last_name.data, username=form.username.data, email=form.email.data, phone_number=form.phone_number.data, password=hashed_password)
                db.session.add(user)
                db.session.commit()
                return jsonify(message='Your account has been created! You can now log in'), 201
            return jsonify(errors=form.errors), 400
        else:
            form = RegistrationForm()
            if form.validate_on_submit():
                hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
                user = User(first_name=form.username.data, other_names=form.other_name.data, last_name=form.last_name.data, username=form.username.data, email=form.email.data, phone_number=form.phone_number.data, password=hashed_password)
                db.session.add(user)
                db.session.commit()
                flash('Your account has been created! You can now log in', 'success')
                return redirect(url_for('main.login'))
    else:
        form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@main.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login unsuccessful. Please check email and password')
    return render_template('login.html', title='Login', form=form)

@main.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@main.route("/profile", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.phone = form.phone.data
        current_user.address = form.address.data
        current_user.last_name = form.last_name.data
        current_user.other_name = form.other_name.data
        current_user.first_name = form.first_name.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('main.home'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('profile.html', title='Account', form=form)