from django.urls import path
from app1.views import pagina_principal, contato, cliente

app_name = 'app1'

urlpatterns = [
    path('', pagina_principal),
    path('contato', contato),
    path('cliente', cliente, name='cliente'),
]