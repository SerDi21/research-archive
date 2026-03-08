from marshmallow import Schema, fields, validate


class PublicationSchema(Schema):
    id = fields.Int(dump_only=True)

    title = fields.Str(
        required=True,
        validate=validate.Length(min=3, max=255)
    )

    abstract = fields.Str(
        required=True,
        validate=validate.Length(min=10)
    )

    authors = fields.Str(required=True)
    keywords = fields.Str()
    created_at = fields.DateTime(dump_only=True)
    published = fields.Bool()