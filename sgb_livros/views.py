from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Livro
from django.contrib.auth.decorators import login_required

# Create your views here.
def livros(request):
    return render(request, 'livros.html')

@login_required
def salva_livro(request):
    titulo_livro = request.POST["titulo_livro"] #pegar nome do livro que esta no .HTML
    autor_livro = request.POST["autor_livro"]
    editora_livro = request.POST["editora_livro"]
    return render(request, 'livros.html', context={'titulo_livro':titulo_livro})

@login_required
def cadastra_livro(request):
    if request.method == 'POST':
        livro_id = request.POST['livro_id']
        titulo = request.POST['titulo']
        autor = request.POST['autor']
        ano_publicacao = request.POST['ano_publicacao']
        editora = request.POST['editora']

        if livro_id: #Edita Livro
            livro = livro_id
            livro.titulo = titulo
            livro.autor = autor
            livro.ano_publicacao = ano_publicacao
            livro.editora = editora
            livro.save()
        else: #salva um novo livro
            Livro.objects.create(
                titulo = titulo,
                autor = autor,
                ano_publicacao = ano_publicacao,
                editora = editora
            )

        return redirect('cadastra_livro')
    # objects é o gerenciamento do Django que serveparaconsultar no banco
    #all() é um comando que retorna todos os cadastros da tabela livro
    livros = Livro.objects.all()
    return render(request, 'livros.html', {'livros': livros})

@login_required
def exclui_livro(request, livro_id):
    # get_object_or_404() esta função busca no banco de dados
    # um objeto da tabela livro cujo campo id seja igual a livro_id.
    # Se encontrar, retorna o objeto e guarda na variavel livro.
    #  Se não encontrar, retorna um página 404
    livro = get_object_or_404(Livro, id=livro_id)
    livro.delete()
    return redirect('cadastra_livro')

@login_required
def edita_livro(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    livros = Livro.objects.all()

    if request.method == 'POST':
        livro.titulo = request.POST['titulo']
        livro.autor = request.POST['autor']
        livro.ano_publicacao = request.POST['ano_publicacao']
        livro.editora = request.POST['editora']
        livro.save()
        return redirect('cadastra_livro')
    return render(request, 'livros.html', {'livros': livros, 'livro_editar': livro})
