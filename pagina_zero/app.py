# importando o Flask
from flask import Flask

# acessando os arquivos 'controllers.py' nas pastas 'website' e 'admin'
# e importando as variáveis que funcionam como miniaplicações blueprint
from website.controllers import website_bp
from admin.controllers import admin_bp

app = Flask(__name__)

# criando uma chave secreta
app.secret_key = 'chave-super-secreta'

#registrando blueprints

app.register_blueprint(website_bp)

app.register_blueprint(admin_bp, url_prefix='/admin')

#rodando a aplicação
app.run()