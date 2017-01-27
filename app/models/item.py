from app import db


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)
    list_id = db.Column(db.Integer, db.ForeignKey('list.id'), index=True)
