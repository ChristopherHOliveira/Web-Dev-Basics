from flask import Blueprint, render_template, request, session, redirect

admin_bp = Blueprint('admin',__name__, template_folder = 'templates')

# exemplo de armazenamento de notas, geralmente isso é pego em um BD...
notas_usuarios = [
    [1,6,8], # notas do usuário 'admin'
    [3,9,7] # notas do usuário 'christopher'
]

@admin_bp.route('/entrar', methods=['GET','POST'])
def f_entrar():
    # este if testa se o usuário já está logado e redireciona para a área logada se sim
    if 'usuario' in session: # se o usuário for autenticado:
        return redirect('area_logada')

    msg = ''

    if request.method == 'POST':

        # requisitando o formulário
        form = request.form

        # requisitando o valor do campo usuário
        v_usuario = form.get('usuario')

        # requisitando o valor do campo senha
        v_senha = form.get('senha')

        if v_usuario == 'admin' and v_senha == 'admin':
            session['usuario'] = 'Administrador'

        elif v_usuario == 'christopher' and v_senha == '1234':
            session['usuario'] = 'Christopher'

        else: # se o usuário e senha estiverem incorretos:
            msg = 'Usuário e/ou senha inválidos!' 

        if 'usuario' in session: # se o usuário for autenticado:
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
