from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.core.exceptions import *
from datetime import datetime, timedelta, timezone

from .models import Quote

def index(request):
    return HttpResponseRedirect('blog')


class blog(generic.TemplateView):
    template_name = 'burgerblog/blog.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Quote'] = Quote.objects.all()
        return context


def quote_added(request):
    try:
        blogname = request.POST['blog_name']
        quotetext = request.POST['quote_text']
    except (KeyError):
        return HttpResponseRedirect("")

    else:
        quote = Quote()
        quote.blog_name = blogname
        quote.quote_text = quotetext
        quote.save()
        return HttpResponseRedirect("/burgerblog") 