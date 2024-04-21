from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib import auth

# Create your views here.
def cadastro(request):
    print(f'*** User:{request.user} isAuth:{request.user.is_authenticated}')
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'A senha e confirmar_senha devem ser iguais')
            return redirect('/usuarios/cadastro')

        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, 'A senha deve possuir pelo menos 6 caracteres')
            return redirect('/usuarios/cadastro')

        # validar aqui se usuario ja existe no banco
        # o correto talvez fosse tratar o erro de retorno do banco

        # users = User.objects.all()
        users = User.objects.filter(username=username)
        if users.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um usuário cadastrado com esse username')
            return redirect('/usuarios/cadastro')

        user = User.objects.create_user(
            username=username, email=email, password=senha
        )

        print(f'{username} criado com sucesso')
        return redirect('/usuarios/login')


def login_view(request):
    print(f'*** User:{request.user} isAuth:{request.user.is_authenticated}')

    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get("senha")

        user = auth.authenticate(request, username=username, password=senha)

        if user:
            auth.login(request, user)
            return redirect('/pacientes/home')

        messages.add_message(request, constants.ERROR, 'Usuário ou senha incorretos')
        return redirect('/usuarios/login')

def sair(request):
    print(f'*** User:{request.user} isAuth:{request.user.is_authenticated}')
    auth.logout(request)
    return redirect('/usuarios/login')
