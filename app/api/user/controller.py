from flask_restx import Resource
from flask import request

from app.utils import validation_error

from .service import UserService
from .dto import UserDto
from .schema import RegisterSchema

api = UserDto.api

user = UserDto.user
data_resp = UserDto.data_resp

register_schema = RegisterSchema()

@api.route("/<string:username>")
class UserGet(Resource):
    @api.doc(
        "Get a specific user",
        responses={
            200: ("User data successfully sent", data_resp),
            404: "User not found!",
        },
    )
    def get(self, username):
        """ Get a specific user's data by their username """
        return UserService.get_user_data(username)

@api.route('/')
class UserRegister(Resource):

    user_register = UserDto.user_register

    @api.expect(user_register, validate=True)
    @api.doc(
        "Register a specific user",
        responses={
            201: ("User successfully created", data_resp),
            400: "Malformed data or validations failed.",
        },
    )
    def post(self):
        """ User registration """
        # Grab the json data
        register_data = request.get_json()

        # Validate data
        if (errors := register_schema.validate(register_data)) :
            return validation_error(False, errors), 400

        return UserService.register(register_data)