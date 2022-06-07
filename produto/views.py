from django.shortcuts import render, redirect
from produto.forms import ProdutoForm
from produto.models import Produto

# Create your views here.


def home(request):
    data = {}
    data['db'] = Produto.objects.all()
    return render(request, 'index.html', data)

#def form(request):
    #produto_form = ProdutoForm()
    #return render(request,'adicionar.html', {'produto_form':produto_form})

def form (request):
    data = {}
    data['form'] = ProdutoForm()
    return render(request, 'adicionar.html', data)

def create(request):
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home') 

#def save(request):
    #produto = ProdutoForm(request.POST)
    #f = produto.save()
    #return render(request,'adicionar.html', context={'produto':produto})
    
    
     
    
    
# Create a form instance from POST data.
#f = ArticleForm(request.POST)

# Save a new Article object from the form's data.
# new_article = f.save()
