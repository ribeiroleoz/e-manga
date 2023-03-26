from django.urls import include, re_path
from emanga import views

urlpatterns = [
    re_path(r'^usuario$', views.usuarioApi),
    re_path(r'^usuario/([0-9]+)$', views.usuarioApi),
    re_path(r'^endereco$', views.enderecoApi),
    re_path(r'^endereco/([0-9]+)$', views.enderecoApi),
    re_path(r'^endereco/usuario/([0-9]+)$', views.enderecoApi),
    re_path(r'^cartao$', views.cartaoApi),
    re_path(r'^cartao/([0-9]+)$', views.cartaoApi),
    re_path(r'^cartao/usuario/([0-9]+)$', views.cartaoApi)
]