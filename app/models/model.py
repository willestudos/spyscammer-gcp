import datetime
from mongoengine import Document, StringField, EmbeddedDocument, EmbeddedDocumentField


class MembersAccount(Document):
    name = StringField(required=True)
    username = StringField(required=True)
    email = StringField(required=True)
    password = StringField(required=True)


class IPData(EmbeddedDocument):
    ip = StringField(required=False)
    city = StringField(required=False)
    region_code = StringField(required=False)
    postal = StringField(required=False)
    latitude = StringField(required=False)
    longitude = StringField(required=False)
    org = StringField(required=False)


class DataScammer(Document):
    id_member = StringField(required=True)
    created_at = StringField(default=str(datetime.datetime.utcnow()), required=True)
    location = StringField(required=False)
    ip_data = EmbeddedDocumentField(IPData, required=False)
    selfie = StringField(required=False)

