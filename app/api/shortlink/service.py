from datetime import datetime
from flask import current_app

from app import db
from app.utils import err_resp, message, internal_err_resp
from app.models.short_link import ShortLink

from .utils import load_data

class ShortLinkService:
    @staticmethod
    def get_short_link(short_id):
        """ Get user data by username """
        if not (short_id := ShortLink.query.filter_by(shortId=short_id).first()):
            return err_resp("User not found!", "user_404", 404)

        try:
            short_link_info = load_data(short_id)

            resp = { "data" : short_link_info }
            
            return resp, 200

        except Exception as error:
            current_app.logger.error(error)
            return internal_err_resp()

    @staticmethod
    def register(data):
        """ Register url """

        url = data["url"]

        if ShortLink.query.filter_by(url=url).first() is not None:
            return err_resp("Url is already being used.", "url_taken", 403)

        try:
            new_short_link = ShortLink(
                shortId="test",
                url=url,
                createdAt=datetime.utcnow(),
            )

            db.session.add(new_short_link)

            short_link_info = load_data(new_short_link)

            db.session.commit()

            resp = { "data" : short_link_info }

            return resp, 201

        except Exception as error:
            current_app.logger.error(error)
            return internal_err_resp()