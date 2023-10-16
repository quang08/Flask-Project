from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    # code for login function
    return


@auth.route('/logout')
@login_required
def logout():
    # code for logout function
    return


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    # code for sign up function
    return
