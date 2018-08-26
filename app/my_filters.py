from flask import Blueprint


module = Blueprint('myfilters', __name__)


@module.app_template_filter('minilist')
def minilist(value):
    a = [i for i in value.split(', ')]
    return a[:6]


@module.app_template_filter('maxilist')
def maxilist(value):
    a = [i for i in value.split(', ')]
    return a[:12]
