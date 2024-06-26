from django.urls import path
from apps.galeria.views import index, imagem, buscar, nova_imagem, editar_imagem, deletar_imagem, filtro, mais_vistas, mais_curtidas,surpreenda_me,toggle_favoritas,favoritas

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar', buscar, name='buscar'),
    path('nova-imagem', nova_imagem, name='nova_imagem'),
    path('editar-imagem/<int:foto_id>', editar_imagem, name='editar_imagem'),
    path('deletar-imagem/<int:foto_id>', deletar_imagem, name='deletar_imagem'),
    path('filtro/<str:categoria>', filtro, name='filtro'),
    path('mais-vistas', mais_vistas, name='mais_vistas'),
    path('mais-curtidas', mais_curtidas, name='mais_curtidas'),
    path('surpreenda-me', surpreenda_me, name='surpreenda_me'),
    path('toggle_favoritas/<int:foto_id>/', toggle_favoritas, name='toggle_favoritas'),
    path('favoritas', favoritas, name='favoritas'),
]