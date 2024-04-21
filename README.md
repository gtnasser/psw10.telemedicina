# criar ambiente virtual e ativar

python3 -m venv vhealing
vhealing\Scripts\activate

# instalar pillow para manipular imagens

pip install pillow  

# instalar django e criar um novo projeto

pip install django 
django-admin startproject healing .

# habilitar autosave no vscode
# file > autosave

file explorer:
healing -> pasta core do projeto
  settings.py -> configs gerais do projeto
  healing -> pasta core do projeto
  urls.py -> urls do roteador
  wsgi.py -> server do deploy
  asgi.py -> semelhante ao wsgi 
manage.py -> CLI do django

python manage.py runserver

# vamos criar 3 aplicativos para nosso sistema: autenticação (login), área do usuário, área do médico

# no aplicativo, temos os arquivos:

views.py -> processar os dados
models.py -> estruturas do banco de dados
tests.py -> testes automatizados
admin.py -> administração

# registrar o novo aplicativo no sistema. Em settings.py

INSTALLED_APPS = [
    ...
]

# definir uma pasta para armazenar os templates. Em settings.py

TEMPLATES = [
    {
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
    }
]

# criar esta pasta em cada aplicativo para amazenar os seus templates
# colocar nesta pasta o aquivo base.html
\templates

# criar esta pasta na raiz do projeto para armazenar templates globais
# colocar nesta pasta o arquivo cadastro.html
\usuarios\templates

# definir onde serão armazenados os arquivos estáticos (imagens, recursos, etc)
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'templates/static'),)
# STATIC_ROOT = os.path.join('static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# criar as pastas e os arquivos dentro de cada pasta

/templates/static
/media
/templates/static/geral/css
  base.css
/templates/static/geral/img
  logo.jpg
/templates/static/geral/js
/templates/static/usuarios/css
/templates/static/usuarios/img
  ilustracao.png
/templates/static/usuarios/js

# atualiza os codigos HTML importando e usando nas referencias, a tag {% static %} do django

# no formulario, associar uma ação ao confirmar o formulário

<form action="/usuarios/cadastro/">

# ou podemos usar a tag URL identificando pelo nome  definido em /usuarios/urls.py
# path('cadastro/', views.cadastro, name="cadastro"),

<form action="{% url 'cadastro' %}">

# banco de dados
# com o servidor parado, aplica as migracoes definidas nos aplicativos que ainda não foram executadas

python manage.py migrate

#  importar do banco de dados as tabelas e a classe User. Em views.py

from django.contrib.auth.models import User

# criar as messages do bootstrap. Em settings.py

from django.contrib.messages import constants

MESSAGE_TAGS = {
    constants.DEBUG: 'alert-primary',
    constants.ERROR: 'alert-danger',
    constants.SUCCESS: 'alert-success',
    constants.INFO: 'alert-info',
    constants.WARNING: 'alert-warning',
}

# para criar uma tabela, criar um model e herdar de models.model. Em usuario/models.py

class Especialidades(models.Model)

# depois, executar 'python makemigrations' para criar os arquivos nnnn_initial.py,
# que são instruçoes de como o banco deve criar as estruturas
# depois, executar 'python migrate' para criar as estruturas no banco de dados

# area administrativa
# http://127.0.0.1:8000/admin

# criar super usuario

python manage.py createsuperuser
ex: root/toor

# para visualizar uma tabela dentro da área administrativa. Em medico/admin.py

from .models import Especialidades
admin.site.register(Especialidades)

# para mostrar o valor de uma variavel no view. Em views.py
# definir um dicionario para passar para o view

        x = 1
        return render(request, 'cadastro_medico.html', {'teste': x})

# Em cadastro_medico.html








# ver

extensão Django Beautiful


# CL para recriar superuser

echo "from django.contrib.auth.models import User; User.objects.filter(email='admin@example.com').delete(); User.objects.create_superuser('admin@example.com', 'admin', 'nimda')" | python manage.py shell

echo "from django.contrib.auth.models import User; User.objects.filter(email='admin@example.com').delete(); User.objects.create_superuser('admin@example.com', 'admin', 'nimda')" | python manage.py shell
