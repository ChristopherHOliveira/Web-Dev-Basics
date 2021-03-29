# importando o Flask (e session, com relação à expiração de cookies no navegador)
from flask import Flask, session

# acessando os arquivos 'controllers.py' nas pastas 'website' e 'admin'
# e importando as variáveis que funcionam como miniaplicações blueprint
from website.controllers import website_bp
from admin.controllers import admin_bp

# importando 'timedelta', com relação ao tempo de expiração de um cookie
from datetime import timedelta

# __name__ é substituído depois...
app = Flask(__name__)

# criando uma chave-super-secreta
app.secret_key = 'chave-super-secreta'

# registrando os blueprints
app.register_blueprint(website_bp)
app.register_blueprint(admin_bp, url_prefix='/admin')

# aplicando o limite de expiração do cookie da sessão
@app.before_request
def f_before_request():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(seconds=10)

#rodando a aplicação
app.run()