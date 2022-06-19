from django.shortcuts import render, redirect
from produto.forms import ProdutoForm
from produto.models import Produto

# Create your views here.


def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Produto.objects.filter(nome__icontains=search)  
    else:
        data['db'] = Produto.objects.all()
        data['db'] = Produto.objects.order_by('-id')
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = ProdutoForm()
    return render(request, 'adicionar.html', data)

def create(request):
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    
def edit(request, pk):
    data = {}
    data['db'] = Produto.objects.get(pk=pk)
    data['form'] = ProdutoForm(instance=data['db'])
    return render(request, 'adicionar.html', data)

def update(request, pk):
    data = {}
    data['db'] = Produto.objects.get(pk=pk)
    form = ProdutoForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Produto.objects.get(pk=pk)
    db.delete()
    return redirect('home')

#def save(request):
    #produto = ProdutoForm(request.POST)
    #f = produto.save()
    #return render(request,'adicionar.html', context={'produto':produto})
      
# Create a form instance from POST data.
#f = ArticleForm(request.POST)

# Save a new Article object from the form's data.
# new_article = f.save()

