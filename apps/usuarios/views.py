from django.shortcuts import render, redirect
from apps.usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()

            usuario = auth.authenticate(
                request,
                username=nome,
                password=senha
            )
        if form is not None:
            auth.login(request, usuario)
            messages.success(request, f'{nome} seja bem-vindo, seu login foi um sucesso!')
            return redirect('index')
        else:
            messages.error(request, 'Erro ao efetuar o login, Usuário inexistente ou nome de usuario e senha incorretos.')
            return redirect('login')

    return render(request, 'usuarios/login.html', {'form': form})

def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)
        
        if form.is_valid():
            
            nome = form['nome_cadastro'].value()
            email = form['email'].value()
            senha = form['senha_1'].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Usuário já existente, escolha outro nome de usuario.')
                return redirect('cadastro')
            
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, 'Usuário Cadastrado com sucesso, redirecionando para a pagina de login.')
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {'form': form})

def logout (request):
    auth.logout(request)
    messages.success(request, 'Logout realizado com sucesso')
    return redirect('login')