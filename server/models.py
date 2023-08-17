from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'
     
     
    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError("no name provided")
        return name

    @validates('phone_number')
    def validate_phone_number(self, key, value):
        if not len(value) == 10:
            raise ValueError("Phone numbers must be 10 digits")
        return value

class Post(db.Model):
    __tablename__ = 'posts'
    # Add validations and constraints 

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())


    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'


    @validates('title')
    def validate_title(self, key, value):
        if value not in ["Won't Believe", "Secret", "Top", "Guess"]:
            raise ValueError('Title needs Clickbait')
        return value



    @validates('content')
    def validate_content(self, key, value):
        if not value or len(value) < 250:
            raise ValueError("must be atleast 250 characters long")
        return value
    

    @validates("summary")
    def validate_summary(self, key, summary):
        if summary and len(summary) >= 250:
            raise ValueError("summary maximum of 250 characters")
        return summary

    @validates('category')
    def validate_category(self, key, value):
        if value not in["Fiction", "Non-Fiction"]:
            raise ValueError('Invalid Category')
        return value