import random

from django.shortcuts import redirect

from .classes import *
from django.http import HttpResponse
from django.views.generic import TemplateView


class Head(TemplateView):
    template_name = 'head.html'
    g:Game
    def get(self, request, *args, **kwargs):
        self.g = Game ( )
        resp = super ( ).get ( request, *args, **kwargs )
        return resp

    def get_context_data(self, **kwargs):

        context = super ( ).get_context_data ( **kwargs )
        context['list'] = self.g.us.board
        context['us'] = self.g.ai.board
        context[self.g] = self.g

        return context

def Shot(self):
    print('dddd')
    return redirect('/?d=1')
#     self.g.us.move()