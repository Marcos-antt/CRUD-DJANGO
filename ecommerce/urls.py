from django.contrib import admin
from django.urls import path
from produto.views import home, form, create

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('adicionar/', form, name='form'),
    path('create/', create, name='create'),

    
]
