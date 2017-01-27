from flask_wtf import Form
from wtforms_alchemy import model_form_factory
# The variable db here is a SQLAlchemy object instance from
# Flask-SQLAlchemy package
from app import db
from app.models.item import Item
from app.models.list import List
from app.models.user import User, Role

BaseModelForm = model_form_factory(Form)


class ModelForm(BaseModelForm):
    @classmethod
    def get_session(cls):
        return db.session


__all__ = ["List", "Item", "User", "Role"]
