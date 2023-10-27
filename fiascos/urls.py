from django.urls import path
from fiascos import views

urlpatterns = [
    path('', views.index, name='index'),
    path('entry', views.entry, name='entry'),
    path('working', views.working, name='working'),
    path('archive', views.archive, name='archive'),
    path('basepost/<int:product_id>', views.basepost, name='basepost')
]

