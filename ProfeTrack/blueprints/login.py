from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
)
from flask_login import login_required, login_user

from ProfeTrack.models.user import User

bp = Blueprint("login", __name__, url_prefix="/")


@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if email is None or password is None:
            flash("Email ou senha inválidos")
            return render_template("login.html")

        user = User.query.filter_by(email=email).first()
        print(getattr(user, "password", None))
        if not user:
            flash("Email ou senha inválidos")
            return render_template("login.html")

        if not user.verify_password(password):
            flash("Email ou senha inválidos")
            return render_template("login.html")

        login_user(user)
        flash("Login realizado com sucesso")
        return redirect("/home")
    else:
        return render_template("login.html")


@bp.route("/home")
@login_required
def home():
    return render_template("home.html")


def init_app(app):
    app.register_blueprint(bp)
