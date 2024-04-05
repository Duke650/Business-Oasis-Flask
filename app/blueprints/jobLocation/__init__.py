from flask import Blueprint

jobLocation = Blueprint("jobLocation", __name__)

from . import routes