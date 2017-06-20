from django.conf.urls import url
from noticias import views
urlpatterns = [
    url(r'^noticia/$', views.noticia_detalle, name='noticia_detalle'),

]