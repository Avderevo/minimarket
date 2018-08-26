from app.database import db


class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    img = db.Column(db.String(255), nullable=True)

    def __str__(self):
        return self.title


    @staticmethod    
    def get_category_menu():
        return Category.query.all()




class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255), nullable=False)
    short_name = db.Column(db.String(255), nullable=False)
    raw_description = db.Column(db.Text, nullable=False)
    img = db.Column(db.String(255), nullable=True)
    price = db.Column(db.String(25), nullable=False)
    color = db.Column(db.String(255), nullable=True)
    review_number = db.Column(db.Integer, nullable=True)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref=db.backref('product', lazy=True))

    def __str__(self):
        return self.short_name

