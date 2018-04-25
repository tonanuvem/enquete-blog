from django.contrib import admin

# Register your models here.

from .models import Questao, Escolhas

admin.site.register(Questao)

admin.site.register(Escolhas)