from django.contrib import admin

# Register your models here.
from apps.produto.models import Produto

admin.site.register(Produto)