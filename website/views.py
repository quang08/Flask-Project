from flask import Blueprint, render_template, request, flash, jsonify

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h1>Test</h1>"