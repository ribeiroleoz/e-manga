from django.urls import include, re_path
from emanga import views

urlpatterns = [
    re_path(r'^usuario$', views.usuarioApi),
    re_path(r'^usuario/([0-9]+)$', views.usuarioApi),
    re_path(r'^endereco$', views.enderecoApi),
    re_path(r'^endereco/([0-9]+)$', views.enderecoApi),
    re_path(r'^endereco/usuario/([0-9]+)$', views.enderecoApi),
    re_path(r'^pedido/([0-9]+)$', views.pedidoApi),
    re_path(r'^pedido', views.pedidoApi),
    re_path(r'^pagamento', views.pedidoApi),
    re_path(r'^pedidos/user/([0-9]+)$', views.getPedidosByUser)
]