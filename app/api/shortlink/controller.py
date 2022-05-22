from flask_restx import Resource
from flask import request

from app.utils import validation_error

from .dto import ShortLinkDto
from .schema import RegisterSchema
from .service import ShortLinkService

api = ShortLinkDto.api
data_resp = ShortLinkDto.data_resp

register_schema = RegisterSchema()

@api.route('/')
class ShortLinkRegister(Resource):

    short_link_register = ShortLinkDto.short_link_register

    @api.expect(short_link_register, validate=True)
    @api.doc(
        "Register a specific url",
        responses={
            201: ("Short Link successfully created", data_resp),
            400: "Malformed data or validations failed.",
        },
    )
    def post(self):
        """ Short Link registration """
        # Grab the json data
        register_data = request.get_json()

        # Validate data
        if (errors := register_schema.validate(register_data)) :
            return validation_error(False, errors), 400

        return ShortLinkService.register(register_data)

@api.route('/<string:short_id>')
class ShortLinkGet(Resource):

    @api.doc(
        "Get a specific short link",
        responses={
            200: ("Short Link data successfully sent", data_resp),
            400: "Short Link not found!.",
        },
    )
    def get(self, short_id):
        """ Get a specific user's data by their username """
        return ShortLinkService.get_short_link(short_id)