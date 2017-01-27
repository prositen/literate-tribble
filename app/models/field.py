from app import db


class FieldType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)


class Field(db.Model):
    list_id = db.Column(db.Integer, db.ForeignKey('list.id'), index=True)
    field_type_id = db.Column(db.Integer, db.ForeignKey('fieldtype.id'), index=True)
    name = db.Column(db.String)
