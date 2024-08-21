from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('name')
    def validates_names(self, key, name_input):
        if len(name_input) == 0:
            raise ValueError('Authors must have a name')
        
        name_validation = Author.query.filter_by(name=name_input).all()

        if name_validation:
            raise ValueError('No two authors must have the same name.')
        
        return name_input

    @validates('phone_number')
    def validates_phone_number(self, key, phone_num):
        cleaned_num = ''.join([integer for integer in phone_num if integer.isdigit()])

        if len(cleaned_num) != 10:
            raise ValueError('Author phone numbers must be exactly 10 digits')
        
        return phone_num



    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('content')
    def validates_content(self, key, content):
        if len(content) < 250:
            raise ValueError('Post content must be at least 250 characters long.')
        return content
        
    @validates('summary')
    def validates_summary(self, key, summary):
        if len(summary) > 250:
            raise ValueError('Post summary has a maximum of 250 characters.')
        return summary
        
    @validates('category')
    def validates_category(self, key, category):
        categories = ['Fiction', 'Non-Fiction']
        if category not in categories:
            raise ValueError('Post category must either be Fiction or Non-Fiction.')
        return category
    
    @validates('title')
    def validates_title(self, key, title):
        if len(title) == 0:
            raise ValueError("Each post must have a title")
        
        click_bait = ['Won\'t Believe', 'Secret', 'Top', 'Guess']

        click_bait_test = [bait for bait in click_bait if bait in title]
        
        if not click_bait_test:
            raise ValueError('Title must be sufficiently clickbait-y')

        return title


    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
