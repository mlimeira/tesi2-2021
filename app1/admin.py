from django.contrib import admin
from app1.models import Cliente, Contato, Pedido, Produto

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Contato)
admin.site.register(Pedido)
admin.site.register(Produto)