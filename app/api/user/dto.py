from flask_restx import Namespace, fields


class UserDto:

    api = Namespace("user", description="User related operations.")
    user = api.model(
        "User object",
        {
            "email": fields.String,
            "name": fields.String,
            "username": fields.String,
            "joined_date": fields.DateTime,
        },
    )

    user_register = api.model(
        "User Register object",
        {
            "email": fields.String(required=True),
            "name": fields.String,
            "username": fields.String(required=True),
        },
    )

    data_resp = api.model(
        "User Data Response",
        {
            "status": fields.Boolean,
            "message": fields.String,
            "user": fields.Nested(user),
        },
    )