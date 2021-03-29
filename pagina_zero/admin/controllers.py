from flask import Blueprint, render_template, request, session, redirect, jsonify

admin_bp = Blueprint('admin',__name__, template_folder = 'templates')

# exemplo de armazenamento de notas para posterior exibição correta para cada usuário:
# (geralmente esses dados são pegos em um BD)
notas_usuarios = [
    [1,6,8], # notas do usuário 'admin' índice [0]
    [3,9,7] # notas do usuário 'christopher' índice[1]
]

# login
@admin_bp.route('/entrar', methods=['GET','POST'])
def f_entrar():

    # este if testa se o usuário já está logado ao entrar em /entrar,
    # redirecionando para a área logada se sim
    if 'usuario' in session: # se o usuário for autenticado:
        return redirect('area_logada')

    msg = ''

    # este 'if' vai ser iniciado quando, através do evento predefinido
    # no botão 'Entrar', for solicitado o método 'POST' na página
    if request.method == 'POST':

        # requisitando o formulário
        form = request.form

        # requisitando o valor do campo usuário
        v_usuario = form.get('usuario')

        # requisitando o valor do campo senha
        v_senha = form.get('senha')

        # exemplo de armazenamento de usuário e senha de usuários cadastrados:
        # (geralmente esses dados são pegos em um BD)
        # se o usuário for 'admin' e a senha 'admin':
        if v_usuario == 'admin' and v_senha == 'admin':

            # a sessão vai ser iniciada com o usuário respectivo
            session['usuario'] = 'Administrador'

        elif v_usuario == 'christopher' and v_senha == '1234':
            session['usuario'] = 'Christopher'

        else: # se o usuário e senha estiverem incorretos:
            msg = 'Usuário e/ou senha inválidos!' 

        # se tudo ok, redireciona para a área logada
        if 'usuario' in session:
            return redirect('area_logada')

    # retornando o template 'entrar.html' 
    return render_template('entrar.html', p_msg = msg)

@admin_bp.route('/area_logada')
def f_area_logada():
    notas = []

    if 'usuario' in session:
        if session['usuario'] == 'Administrador':

            notas = notas_usuarios[0] # pega a primeira lista da lista de notas do usuario
        elif session['usuario'] == 'Christopher':

            notas = notas_usuarios[1] # pega a segunda lista da lista de notas do usuario
    return render_template('area_logada.html', notas = notas)

# blueprint de saída
@admin_bp.route('/sair')
def f_sair():
    session.clear()
    return redirect('entrar')


# verificando se o usuário existe.
# para acessar, substituir <v_usuario> pelo str do usuário, no caminho.
@admin_bp.route('/verifica_usuario/<v_usuario>')
def verifica_usuario(v_usuario):

    # ex: se o conteudo de v_usuario estiver na lista:
    if v_usuario in ['admin','christopher']:
        msg1 = 'Usuário ' + v_usuario + ' existe.'

    # senão
    else:
        msg1 = 'Usuário ' + v_usuario + ' não existe.'

    # retornando os dados jsonificados (msg2)
    return jsonify(msg2= msg1)