from flask import Blueprint, Flask, flash, render_template, request
from flask_login import login_required

from ProfeTrack.models.user import User

bp = Blueprint("user", __name__, url_prefix="/user")


@bp.route("/create", methods=["GET", "POST"])  # type: ignore
@login_required
def create_user():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        email = request.form.get("email", "")
        type = request.form.get("type", "")

        if not username or not password or not email or not type:
            flash("Todos os campos devem ser preenchidos")
            return render_template("create_user.html")

        try:
            user = User.query.filter_by(email=email).first()
            if user:
                flash("Email em uso")
                return render_template("create_user.html")
        except Exception as e:
            flash(f"Erro inesperado: {e}")
            return render_template("create_user.html")

        try:
            user = User(username=username, password=password, email=email, type=type)  # type: ignore
            user.create_user(username, password, type, email)  # type: ignore
            return '<h1>Usário criado com sucesso</h1>'
        except Exception as e:
            flash(f"Erro inesperado: {e}")
            return render_template("create_user.html")
    else:
        return render_template("create_user.html")


def init_app(app):
    app.register_blueprint(bp)
