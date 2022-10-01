from flask import render_template, session, redirect, url_for, Blueprint, request, flash, Flask, Response


rcMain = Blueprint('rcMain', __name__, url_prefix='')


@rcMain.route('/raphaelcordon')
def raphaelcordon():

    return render_template('raphaelCordon/index.html')
