from django.urls import path
from . import views 

urlpatterns = [
    #path('', views.livros),
    #path("salva_livro" , views.salva_livro)
    path('', views.cadastra_livro, name='cadastra_livro'),
    path('excluir/<int:livro_id>', views.exclui_livro, name='exclui_livro'),
    path('editar/<int:livro_id>', views.edita_livro, name='edita_livro')
]
