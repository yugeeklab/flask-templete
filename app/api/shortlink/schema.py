from marshmallow import Schema, fields

class ShortLinkSchema(Schema):
    class Meta:
        # Fields to expose, add more if needed.
        fields = ("shortId", "url", "createdAt")

class RegisterSchema(Schema):

    url = fields.Url()
