from flask import Flask, redirect, url_for
from views.cargo_views import cargo_bp
from views.departamento_views import departamento_bp
from views.funcionario_views import funcionario_bp


app = Flask(__name__)
app.config["SECRET_KEY"] = "minha-chave-super-secreta"


app.register_blueprint(cargo_bp)
app.register_blueprint(departamento_bp)  
app.register_blueprint(funcionario_bp)

@app.route("/")
def index():
    return redirect(url_for("cargo.listar"))

if __name__ == "__main__":
    app.run(debug=True)
