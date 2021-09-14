from django.urls import path
from app1.views import pagina_principal, contato, cliente, produto, pedido

app_name = 'app1'

urlpatterns = [
    path('', pagina_principal),
    path('contato', contato, name='contato'),
    path('cliente', cliente, name='cliente'),
    path('produto', produto, name='produto'),
    path('pedido', pedido, name='pedido')
]