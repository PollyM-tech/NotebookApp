from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

# helps sqlalchemy provide a consistent naming convention for constraints
# such as primary keys, foreign keys, indexes, etc.
# this is useful for migrations and debugging
naming_convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

# Set metadata with naming convention
metadata = MetaData(naming_convention=naming_convention)
db = SQLAlchemy(metadata=metadata)



class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.Text, nullable=False)
    email = db.Column(db.VARCHAR, nullable=False, unique=True)
    password = db.Column(db.VARCHAR, nullable=True)
    created_at = db.Column(db.TIMESTAMP, default=datetime.now())
    updated_at = db.Column(db.TIMESTAMP, onupdate=datetime.now())

    # Relationships
    categories = db.relationship("Category", back_populates="user", cascade="all, delete-orphan")
    entries = db.relationship("Entry", back_populates="user", cascade="all, delete-orphan")


class Category(db.Model, SerializerMixin):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    user_id = db.Column(
        db.Integer, db.ForeignKey("users.id", ondelete="cascade"), nullable=True
    )
    created_at = db.Column(db.TIMESTAMP, default=datetime.now())

    # Relationships
    user = db.relationship("User", back_populates="categories", uselist=False)
    # def to_dict(self):
    #     return{"id": self.id, "name": self.name, "created_at": self.created_at}
    serialize_rules = ("-user_id", "-user")


class Entry(db.Model):
    __tablename__ = "entries"

    id = db.Column(db.Integer, primary_key=True)
    note = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"),nullable=False)
    category_id = db.Column(db.Integer,db.ForeignKey("categories.id", ondelete="SET NULL"),nullable=True)
    created_at = db.Column(db.TIMESTAMP, default=datetime.now())
    updated_at = db.Column(db.TIMESTAMP, onupdate=datetime.now())
    deleted_at = db.Column(db.TIMESTAMP)

    # Relationships
    user = db.relationship("User", back_populates="entries", uselist=False)

