from flask import Blueprint, render_template, request

website_bp = Blueprint('website', __name__, template_folder = 'templates')

@website_bp.route('/ola/<parametro>')
def f_ola(parametro):
    # retornando uma mensagem normal e uma mensagem personalizável com o parâmetro digitado
    return '<h1>É galera, o flask funciona!</h1><br>' + '<p>Seu nome é ' + parametro + '</p>'

# pagina inicial
@website_bp.route('/')
def f_index():
    return render_template('index.html')

# aqui, ao entrar em http://127.0.0.1:5000/contato
@website_bp.route('/contato')
def f_contato():
    # carrega a pagina 'contato.html' através do 'render_template'
    # (por padrão deve estar localizada na pasta 'template)
    return render_template('contato.html')

# aqui vamos brincar mais com os parâmetros retornados, que serão trabalhados no código html com a ferramente Jinja
@website_bp.route('/motos')
def f_motos():
    nome = 'Christopher'
    listaMotos = ['Crypton 105','XTZ 125','XR 250 Tornado','XTZ 250 Lander','Versys-X 300']
    return render_template('motos.html', nome_usuario=nome, motos=listaMotos)