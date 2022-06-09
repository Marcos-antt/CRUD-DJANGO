from django.contrib import admin
from django.urls import path
from produto.views import home, form, create, edit, update, delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('adicionar/', form, name='form'),
    path('create/', create, name='create'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('update/<int:pk>', update, name='update'),
    path('delete/<int:pk>', delete, name='delete'),
   
]
