from flask import Flask, render_template, flash, redirect, url_for
from flask_login import current_user, login_required, logout_user, login_user
from werkzeug.security import generate_password_hash, check_password_hash

from form import RegistrationForm, LoginForm, UpdateAccountForm
from models import User, db
from models import app


@app.route('/')
def index():
    return render_template('index.html', is_user_logged_in=current_user.is_authenticated, user=current_user)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        if len(form.password.data) < 8:
            flash('Password must be at least 8 characters long.', 'danger')
            return redirect(url_for('register'))
        hashed_password = generate_password_hash(form.password.data)
        new_user = User(name=form.name.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('RegisterPage.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Login unsuccessful. Please check your email and password.', 'danger')
            return render_template('LoginPage.html', form=form, user=current_user)

    return render_template('LoginPage.html', form=form, user=current_user)


@app.route('/update_account', methods=['GET', 'POST'])
@login_required
def update_account():
    form = UpdateAccountForm()

    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('index'))

    form.name.data = current_user.name
    form.email.data = current_user.email

    return render_template('UpdatePage.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=5001)
