from django.urls import path
from django.conf.urls.static import static

from . import views

app_name = 'enquete'

urlpatterns = [
    # ex: /enquete/
    path('', views.index, name='index'),
    # ex: /enquete/5/
    path('<int:questao_id>/', views.detalhes, name='detalhes'),
    # ex: /enquete/5/resultado/
    path('<int:questao_id>/resultado/', views.resultado, name='resultado'),
    # ex: /enquete/5/vote/
    path('<int:questao_id>/votar/', views.votar, name='votar'),
] # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)