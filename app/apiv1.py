from flask import Blueprint
from flask_restx import Api

from .api.user.controller import api as ns1
from .api.shortlink.controller import api as ns2

blueprint = Blueprint('api', __name__, url_prefix='/api/1')
api = Api(blueprint,
    title='My Title',
    version='1.0',
    description='A description',
)

api.add_namespace(ns1)
api.add_namespace(ns2)