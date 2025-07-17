from flask import render_template, flash, request, redirect, url_for
from comunidadeImpressionadora import app, database
from comunidadeImpressionadora.forms import FormCriarConta, FormLogin
from comunidadeImpressionadora.models import Usuario

lista_usuarios = ['Lucas', 'João', 'Didi', 'Alessandra', 'Amanda']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/usuarios')
def usuarios():

    return render_template('usuarios.html', lista_usuarios=lista_usuarios)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_criar = FormCriarConta()

    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        flash(f"Login feito com sucesso no e-mail {form_login.email.data}", 'alert-success')
        return redirect(url_for('home'))

    if form_criar.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        usuario = Usuario(username=form_criar.username.data,email=form_criar.email.data,senha=form_criar.senha.data)
        database.session.add(usuario)
        database.session.commit()
        flash(f"Conta criada para o e-mail {form_criar.email.data}", 'alert-success')
        return redirect(url_for('home'))

    return render_template('login.html', form_login=form_login, form_criar=form_criar)