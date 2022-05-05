from flask import Blueprint
from .controller import add_posts

posts_bp = Blueprint('posts_bp', __name__)

posts_bp.add_url_rule(rule="/posts", view_func=add_posts, methods=["POST"])
