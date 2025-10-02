from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

# Create your views here.
def cadastra_usuario(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        nome_usuario = request.POST['nome_usuario']
        email = request.POST['email']
        senha = request.POST['senha']

        usuario = User.objects.filter(username=nome_usuario).first()

        if usuario:
            return HttpResponse('Usuário já cadastrado!')
        else:
            usuario = User.objects.create_user(username=nome_usuario, email=email, password=senha)
            usuario.save()
            return HttpResponse('Usuário cadastrado com sucesso!')

def loga_usuario(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        nome_usuario = request.POST['nome_usuario']
        senha = request.POST['senha']

        usuario = authenticate(username=nome_usuario, password=senha)

        if usuario:
            login(request, usuario)
            return HttpResponse('Usuário autenticado!')
        else:
            return HttpResponse('Usuário e/ou senha inválidos!')