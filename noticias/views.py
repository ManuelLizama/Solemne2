# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from noticias.models import Noticia
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
def index(request):
    """
    Pagina inicial.
    """
    return render(
        request,
        'index.html',
        {
        }
    )

def noticia_detalle(request):
    data = {}

    data['object_list'] = Noticia.objects.all().order_by('name')


    template_name = 'noticia_detalle.html'
    return render(request, template_name, data)


# Create your views here.
