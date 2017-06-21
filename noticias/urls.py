from django.conf.urls import url, include
from noticias import views
urlpatterns = [
    url(r'^(?P<pk>\d+)$', views.noticia_detalle, name='noticia_detalle'),
    url(r'^$', views.index, name='index'),
    
]