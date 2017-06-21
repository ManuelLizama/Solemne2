# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from noticias.models import Noticia
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
def index(request):
    
    data = {}

    data['object_list'] = Noticia.objects.all().order_by('created')
    
    return render(request,'index.html',data)

def noticia_detalle(request, pk):
    noticia = get_object_or_404( Noticia, pk=pk)
    template_name = 'noticia_detalle.html'
    return render(request, template_name, {'noticia':noticia})


# Create your views here.
