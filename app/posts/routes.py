from flask import Blueprint
from .controller import add_posts, get_posts

posts_bp = Blueprint('posts_bp', __name__)

posts_bp.add_url_rule(rule="/posts", view_func=add_posts, methods=["POST"])
posts_bp.add_url_rule(rule="/get-posts/<int:page>", view_func=get_posts,methods=["GET"])
