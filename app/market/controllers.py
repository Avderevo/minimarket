from flask import (
    Blueprint,
    render_template,
    flash,
    abort,
    current_app,
)

from sqlalchemy.exc import SQLAlchemyError
from .models import Category, Product


module = Blueprint('market', __name__)


def log_error(*args, **kwargs):
    current_app.logger.error(*args, **kwargs)


@module.route('/', methods=['GET'])
def index():
    category_menu = Category.get_category_menu()
    category = Category.query.all()
    return render_template('market/index.html', category=category, category_menu=category_menu)


@module.route('/<string:category>', methods=['GET'])
def product_list(category):
    products = None
    try:
        category_menu = Category.get_category_menu()
        category = Category.query.filter_by(title=category).first()
        products = Product.query.filter_by(category_id=category.id).all()
        if products is None:
            flash('Нет product с таким идентификатором', 'danger')
            abort(404)
    except SQLAlchemyError as e:
        log_error('Error while querying database', exc_info=e)
        flash('Во время запроса произошла непредвиденная ошибка', 'danger')
        abort(500)
    return render_template('market/product-list.html', product_list=products, category=category, category_menu=category_menu)


@module.route('/<string:category>/<int:id>', methods=['GET'])
def product_detail(category, id):
    category_menu = Category.get_category_menu()
    product = None
    category = category
    try:
        product = Product.query.filter_by(id=id).first()
        if product is None:
            flash('Нет product с таким идентификатором', 'danger')
    except SQLAlchemyError as e:
        log_error('Error while querying database', exc_info=e)
        flash('Во время запроса произошла непредвиденная ошибка', 'danger')
        abort(500)
    return render_template('market/product.html', prod=product, category=category, category_menu=category_menu)

