from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from comunidadeImpressionadora.models import Usuario
from flask_login import current_user

class FormCriarConta(FlaskForm):
    username = StringField('Nome do Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 11)])
    confirmacao_senha = PasswordField('Confirmar senha', validators=[DataRequired(), EqualTo('senha')])
    botao_submit_criarconta = SubmitField('Criar Conta')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('E-mail já cadastrado. Cadastre-se com outro e-mail ou faça login para continuar')
    
    def validate_username(self, username):
        username = Usuario.query.filter_by(username=username.data).first()
        if username:
            raise ValidationError('Usuário já existente, tente outro nome ')


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 11)])
    lembrar_dados = BooleanField('Lembrar dados de Acesso')
    botao_submit_login = SubmitField('Login')


class FormEditarPerfil(FlaskForm):
    username = StringField('Nome do Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    foto_perfil = FileField('Atualizar Foto de Perfil', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'JPEG', 'JPEG'])])

    
        # Cursos
    curso_excel = BooleanField('Excel Avançado')
    curso_vba = BooleanField('Automação VBA')
    curso_powerbi = BooleanField('Dashboards Power BI')
    curso_python = BooleanField('Programação Python')
    curso_sql = BooleanField('SQL e Banco de Dados')
    curso_html_css_js = BooleanField('Desenvolvimento Web')
    curso_ciencia_dados = BooleanField('Ciência de Dados')

    
    # Botão de submit
    botao_submit_editarperfil = SubmitField('Salvar Alterações')
    
    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuario.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError('E-mail já cadastrado. Cadastre-se com outro e-mail ou faça login para continuar.')
            

class FormCriarPost(FlaskForm):
    titulo = StringField('Título do Post', validators=[DataRequired(), Length(2,140)])
    corpo = TextAreaField('Escreva seu Post Aqui', validators=[DataRequired()])
    botao_submit = SubmitField('Criar Post')


class FormEditarPost(FlaskForm):
    titulo = StringField('Título do Post', validators=[DataRequired(), Length(2,140)])
    corpo = TextAreaField('Edite seu Post Aqui', validators=[DataRequired()])
    botao_submit_editar = SubmitField('Salvar Alterações')
