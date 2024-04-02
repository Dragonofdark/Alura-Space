from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Fotografia
from django.contrib import messages
from apps.galeria.forms import FotografiaForm
import random
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para visualizar o site.')
        return redirect('login')

    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada=True)
    return render(request, 'galeria/index.html', {'cards': fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    fotografia.mais_vistas += 1
    fotografia.mais_curtidas += 1
    fotografia.save()
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para visualizar o site.')
        return redirect('login')
     
    fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, 'galeria/index.html', {'cards': fotografias})

def nova_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para visualizar o site.')
        return redirect('login')
    form = FotografiaForm
    if request.method == 'POST':
        form = FotografiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fotografia cadastrada com sucesso!')
            return redirect('index')
        
    return render(request, 'galeria/nova_imagem.html', {'form': form})

def editar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    form = FotografiaForm(instance=fotografia)

    if request.method == 'POST':
        form = FotografiaForm(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fotografia editada com sucesso!')
            return redirect('index')

    return render(request, 'galeria/editar_imagem.html', {'form': form, 'foto_id': foto_id})

def deletar_imagem(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request, 'Deleção realizada com sucesso!')
    return redirect('index')

def filtro(request, categoria):
     fotografias = Fotografia.objects.order_by('data_fotografia').filter(publicada=True, categoria=categoria)
     return render(request, 'galeria/index.html', {'cards': fotografias})

def mais_vistas(request):
    mais_vista = Fotografia.objects.order_by('-mais_vistas')[:10] 
    return render(request, 'galeria/mais_vistas.html', {'mais_vistas': mais_vista})

def mais_curtidas(request):
    mais_curtida = Fotografia.objects.order_by('-mais_curtidas')[:10]
    return render(request, 'galeria/mais_curtidas.html', {'mais_curtidas': mais_curtida})

def surpreenda_me(request):
    imagens = Fotografia.objects.all()
    imagem_aleatoria = random.choice(imagens)
    return render(request, 'galeria/surpreenda_me.html', {'imagem': imagem_aleatoria})

@login_required
def toggle_favorita(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.toggle_favorita(request.user)
    return JsonResponse({'status': 'success'})