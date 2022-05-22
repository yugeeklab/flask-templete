from flask_restx import Namespace, fields


class ShortLinkDto:

    api = Namespace("short-links", description="Short link operations.")
    short_link = api.model(
        "Short Link object",
        {
            "shortId" : fields.String,
            "url": fields.String,
            "created_at": fields.DateTime,
        },
    )

    short_link_register = api.model(
        "User Register object",
        {
            "url": fields.String(required=True),
        },
    )

    data_resp = api.model(
        "Short Link Data Response",
        {
            "data": fields.Nested(short_link),
        },
    )