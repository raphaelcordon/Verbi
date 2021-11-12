from flask import render_template, session, redirect, url_for, Blueprint, Response


ind = Blueprint('ind', __name__, url_prefix='')


@ind.route('/')
def index():

        return render_template('index.html')